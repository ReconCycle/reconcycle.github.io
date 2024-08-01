# Robot module
The robot control module is based on vendor-provided `franka_ros`[^1], which integrates the robot's API `libfranka`[^2] into the ROS ecosystem.

[^1]: [franka_ros documentation](https://frankaemika.github.io/docs/franka_ros.html)
[^2]: [libfranka documentation](https://frankaemika.github.io/docs/libfranka.html)

## Robot state publisher

The `franka_control_node` acts as a robot state publisher, providing the current joint state and estimated external wrench to topics using standard ROS messages.

Robot states specific to the Franka Emika Panda robot arm are published using `franka_msgs`. These states include, among others, the current robot mode (kinesthetic guidance, robot motion using an external program, robot motion using internal controller, reflex, error recovery), contact level activation, collision threshold status, and compensated external load.

The ROS node `franka_control_node` also provides the following ROS services:

- `SetJointImpedance` and `SetCartesianImpedance` specify joint or Cartesian stiffness for the robot's internal controller (damping is automatically derived from the stiffness).
- `SetEEFrame` specifies the transformation from the Panda's flange frame to the tool center point (TCP).
- `SetForceTorqueCollisionBehavior` and `SetFullCollisionBehavior` set thresholds for external forces in Cartesian and joint space to configure the collision reflex and contact detection.
- `SetLoad` sets an external load (e.g., caused by a grasped object) that the robot controller should compensate.

Most common gripper actions (`Grasp`, `Move`, `Open`) for the Panda hand gripper are also implemented in the `franka_control_node`.

![Integration of `ros_control` controllers into the ReconCycle architecture](/figures/control/ros-control-overview.png)
*Figure 1: Integration of `ros_control` controllers into the ReconCycle architecture.*

## `ros_control` and action servers

Controllers are implemented using `ros_control` on a dedicated computer running real-time Linux (Franka ROS Controller in Figure 1). The `ros_control` framework provides a hardware abstraction layer (`RobotHW`) that enables standardized access to actuators and comes with a common interface (`ControllerBase`) to write robot-agnostic controllers[^3].

[^3]: [ros_control documentation](https://wiki.ros.org/ros_control)

The robot middleware is represented by the robot's hardware interface. For the Franka Emika Panda robot, this interface is implemented by the `franka_hw` ROS package using the `libfranka` library.

This scheme allows the usage of standard ROS controllers and tools (such as MoveIt!, Play Motion, or RQT joint trajectory controller GUI).
In addition, custom implementations of joint and Cartesian space impedance controllers expose an action server interface for different robot motion modes.

![Clients can send action goals (motion parameters) or cancel them. Action server periodically sends status update and feedback information. When the execution is finished or interrupted, it reports the end result.](/figures/control/ros-action-server.png)
*Figure 2: Clients can send action goals (motion parameters) or cancel them. The action server periodically sends status updates and feedback information. When the execution is finished or interrupted, it reports the end result.*

The benefit of using ROS-provided action servers to trigger robot motion is the ability to cancel the request during execution and to get periodic feedback on how the request is progressing. Upon acceptance, the action goal's status is set to active if there are no other action goals (e.g., motions) waiting for execution. If an action goal is preempted, the robot does not enter an emergency state and does not require any restart procedure. The client receives appropriate result messages to handle the preemption in its scheme and continue with another action if desired. This enables integration with the state machine framework presented in Section 3.4.

## Motion generation

To achieve the desired robot motion, new desired joints must be calculated at every sample time. We implemented various trajectory generation strategies to meet the most common robot motion needs in the context of automated disassembly:

- Joint space point-to-point trajectory with trapezoidal velocity profile[^4] (`JointTrapVel` action server in Figure 1)
- Cartesian space straight line point-to-point motion & quaternion SLERP trajectory[^5] with minimum jerk time evolution (`CartLinTask` action server in Figure 1)
- Joint space point-to-point trajectory with trapezoidal velocity profile, with the initial and final pose provided in Cartesian space and transformed into joint space using inverse kinematics (`JointTrapVelCartTarget` action server in Figure 1)
- Dynamic movement primitive (DMP) in joint space[^6] (`JointDMP` action server in Figure 1)
- Cartesian space DMP[^7] (`CartDMP` action server in Figure 1)
- Direct joint angle control (e.g., using MoveIt! in Figure 1)

[^4]: [Lynch, Park. Modern Robotics: Mechanics, Planning, and Control](https://modernrobotics.northwestern.edu/)
[^5]: [Shoemake, Ken. "Animating rotation with quaternion curves."](https://dl.acm.org/doi/10.1145/325165.325242)
[^6]: [Ijspeert et al. "Dynamical Movement Primitives: Learning attractor models for motor behaviors."](https://doi.org/10.1162/neco_a_00393)
[^7]: [Ude et al. "Orientation in Cartesian space dynamic movement primitives."](https://doi.org/10.1109/ICRA.2014.6907291)

To generate a motion according to the selected strategy, a new action goal (motion parameters) has to be sent to an appropriate action server.

`JointTrapVel`, `JointTrapVelCartTarget`, and `JointDMP` action servers calculate the joint configuration at each sample time. The underlying `joint_impedance_controller` calculates appropriate joint torques and sends them to the robot's low-level controller using `franka_hw` and `libfranka` as shown in Figure 1.

`CartLinTask` and `CartDMP` action servers calculate task-space positions and orientations at each sample time. The underlying Cartesian impedance controller calculates appropriate joint torques and sends them to the robot's low-level controller using `franka_hw` and `libfranka` as shown in Figure 1.

Using third-party motion generators or tools for direct joint angle control is also possible through the standard ROS interfaces.
```
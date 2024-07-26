### Soft actuators

The integration of soft actuators into robotic systems is crucial for enhancing adaptability and flexibility in handling various tasks, particularly in complex domains like electronic waste recycling. Unlike traditional rigid grippers, soft actuators offer superior adaptiveness and robustness, enabling them to accommodate the diverse shapes and sizes of electronic devices.

The qbSoftHand is used in various grasping tasks. Please refer to the [qbSoftHand](https://cloud.reconcycle.eu/s/gNzm2Y3CP5MksXk) and [qbSoftHand 2 Research](https://cloud.reconcycle.eu/s/5JxzPaCanpNxB2W) general user manuals.  [Version 6 of `qbdevice-api` package](https://bitbucket.org/qbrobotics/qbdevice-api-6.x.x/src/production/) contains the API-level library for qbSoftHand. [Version 7](https://bitbucket.org/qbrobotics/qbdevice-api-7.x.x/src/production/) targets the upgraded  qbSoftHand 2.
The compatible ROS drivers are documented in a ROS Wiki entry on [qbhand](https://wiki.ros.org/Robots/qbhand) package.


To meet the requirements of specific tasks involved in disassembly, an upgraded VSA gripper has been developed.
For installation and usage information, please refer to the [general user manual for qb SoftClaw](https://cloud.reconcycle.eu/s/4ytTpcwNkJ74X6t).
The API is documented in the [linked git repository](https://bitbucket.org/qbrobotics/api-test-sc-v7/src/main/) and on the ROS Wiki: http://wiki.ros.org/Robots/qbmove.

<!--- maybe something about the simulation? --->

#### qb SoftHand Research
The qb SoftHand Research is an anthropomorphic robotic hand based on soft robotics. It is flexible, adaptable, and safe for interaction with objects and humans. It has 19 kinematic degrees of freedom but only one motor for actuation. The hand grasps objects without changing control actions, ensuring simplicity and flexibility. Integrated with a 24 VDC motor and elastic ligaments, the hand's fingers open and close efficiently. It uses the RS485 communication protocol and is integrated into the ReconCycle workcell via a ROS node, performing tasks like grasping heat cost allocators and handling plastic enclosures.

#### qb SoftHand Evolution
The qb SoftHand 2 improves on the original with a two-motor transmission system, allowing multiple finger postures by combining pulley movements. This design incorporates the second human hand synergy, enabling precise grasps like the "pinch grasp" for small objects such as batteries, while maintaining the ability to grasp larger objects.

#### qb SoftClaw 

The qb SoftClaw consists of two fingers: a mobile finger driven by the qbmove Advanced’s shaft, which performs soft movements to grasp objects without damaging critical parts, and a fixed finger directly connected to the frame. Variable stiffness systems are incorporated to enhance safety and functionality in unstructured environments. These systems transform input torques and velocities into torque, velocity, stiffness, and stiffness velocity at the output shaft.

The qb SoftClaw has a force range of 0.5 to 64.0 N and a stiffness range of 0.07 to 11.5 N/mm. It has a closing time of 0.5 seconds, dimensions of 81x90x165 mm, and weighs 0.78 kg.

It offers flexibility in finger geometry and interfaces, enabling the use of various tools and pads.

##### Pad Exchange System
The magnetic pad exchange system allows for quick setup and maintenance. Pads can be attached using magnets or screws, depending on the task's requirements. A variety of soft pads with different dimensions and shapes are available, ensuring the most suitable pad is used for each task.

##### Tool Exchange System
The tool exchange system divides the fixed finger into two parts: the housing connected to the qbmove Advanced and the removable finger tool. The interface allows free insertion and secure locking without screws or pins. The assembly sequence involves insertion, rotation, and locking, facilitated by compression springs. This system supports various tool designs for different disassembly operations, such as screwdrivers, levers, and hooks.

# Robot Operation Manual

## Franka Emika Robot overview

Franka Emika Robot, also known as the *Panda robot*, is a 7 d.o.f. robotic arm, that is integrated in the [robot module](https://reconcycle.github.io/hardware/modules.html#robot-module). 

<img src="/figures/modules/franka_module-nobg.png" width="300px" />

The module also includes an external activation device, a robot control unit and a real-time Linux server. The robot control unit runs a web user interface called *Desk* and provides a *Franka control interface (FCI)*.
The Linux server is connected into the overall ReconCycle network via ROS and runs [custom controllers](https://reconcycle.github.io/developer_guide/robot_module.html), that use FCI to forward motion commands into robot's control unit. 

<img src="/figures/control/Franka_Network_Overview.png" width="300px" />

Depening on the internal state of the robot, the LED indicators on the robot can have different colors:

<img src="/figures/control/Panda_led.png" width="300px" />

Below we provide a quick guide to operate the robot and access is basic functionality. A more comprehensive user manual of the robot is availiable from the robot's internal GUI, called *Desk* from the sidebar menu.

## Accessing Desk 

Franka Desk is robot's internal GUI. You can think of it as a replacement for teach pendant. It can be accessed via browser at the IP address of the robot, which is printed on each robot module.

The user inferaface is composed of thre sections (main pane, with currently running task; bottom pane with task and app overview and sidebar with status overview):
<img src="/figures/control/desk.png" width="300px" />


## Unlocking the robot

The robot is configured to boot automatically, when it is connected to the power suply. In order to use it, you should first unlock its brakes. This can be done through the Desk.

1. Navigate to the robot's web interface (Desk) in your browser of choice
2. Wait until the robot is initialized (LEDs should stop blinking and light yellow)
3. Unlock the joints by pressing "Click to unlock the joints" modal window, confirming with "Open" or search for the unlock icon in the sidebar.
4. If necessary, gain control by pressing the "o" button physically on the robot's wrist.

Now, the robot's LED should blink white and you should be able to freely move the robot around by pressing the two buttons on the robot wrist.

## Activating external control

In order to enable external control of the robot though controllers developed within the ReconCycle project, FCI should be acivated using the "Activate FCI" link in the sidebar.
This is necessary for running any of the disassembly scripts discussed in the remainder of tis user manual.

Additionaly, this interface shuld be enabled using the External Activation device. You might need to press and release the button until the LEDs on the robot light blue.

## Running ReconCycle controllers

## Using Robot Blockset library

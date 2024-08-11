# ROS managment of Raspberry GPIOs

//Not finished

The ROS periphery interface allows users to quickly integrate existing cell periphery into the ROS-based software system. To make the micro-computer
ROS-compatible, a Pi image with Ubuntu 16.04 and pre-installation of ROS is
mounted. Installation procedure for a Raspberry Pi image is described in Section 3.1. As the peripheral elements should enable swapping, the ROS instance on the micro-computer runs automatically when the periphery interface receives
power. Standard ROS communication protocols are used to send and receive
commands on the periphery interface. The commands are then further relayed
to the peripheral element it controls through a proxy program, which is specific to the peripheral element


## Raspi ROS
//Not finished


Besides robot manipulation capabilities, the implementation of disassembly processes in the
ReconCycle cell requires the availability of various support functions, which are provided by
different auxiliary devices. For example, the robot module needs to be able to activate or
deactivate the pneumatic tool changer mounted on the top of the robot. For modules that
include an activation unit such as a clamp or a cutter, we need to be able to send activation
signals and to check the state of the device. 
We selected Raspberry Pi 4 as the archetypical
module’s microcomputer. Raspberry Pi provides us with the ability to generate control signals
and read the sensor values by attaching the auxiliary devices (equipment) to the GPIOs of
the Raspberry Pi. When the auxiliary equipment is connected to the GPIOs of the Raspberry
Pi, each GPIO in use must be properly configured by a suitable software library. Since the
auxiliary equipment attached to each individual module needs to work in synchronization with
the robots and the auxiliary equipment of other modules, we need to be able to control the
equipment globally throughout the cell. 
Therefore we have prepared a ROS package [17] that
wraps the developed software library for configuring and controlling GPIOs in a ROS node.
This way we enable the configuration and control of auxiliary devices through ROS services.
The cell programmer no longer needs to deal with GPIOs but can control and communicate
with the auxiliary equipment through ROS interfaces.





https://github.com/ReconCycle/raspi_ros



For the control and managment of Raspberries GPIOs are used two ROS nodes
running on each individual Raspberry microcomputer. The first ROS node is "Equipment Server", which configures control of the GPIOs connected equipment according to the module configuration file and forwards control commands from ROS services to the connected equip-
ment. The second ROS node is "Equipment Manager", which allows a user to modify the module’s configuration file via a ROS service.

### Equipment Server


When the "Equipment Server" node is started, it first reads the individual module’s configuration file actual_config, which is stored locally on the module’s microcomputer, and then configures the required GPIOs. The configuration file must contain information which additional equipment is attached to the module and to which GPIOs it is connected. Once GPIOs are configured, the "Equipment Server" creates a separate ROS service for each GPIO to control it. The names of the created ROS services are defined in the configuration file. In operation, the "Equipment Server" accepts the commands sent to its ROS services and controls the equipment connected to the GPIOs accordingly. Currently we have three different GPIO configurations and control interactions that "Equipment Server" can handle. The first possible configuration is a digital output where a service call can set the digital state of the GPIO, making it suitable for controlling devices such as pneumatic valves. The next configuration is a digital input that allows the digital state of devices such as digital sensors to be read on a service call. The last is a configuration that, according to the value in the service call, controls PWM signals that can be used to control devices such as step motors. The node also has a restart service that – when triggered – closes all active services, releases the pin’s hardware interface, and reads the configuration file again. Then it starts with the newly read configuration.

### Equipment Manager

//Not finished

When switching from one disassembly process to another, we often need to change, add or remove various auxiliary equipment attached to the modules. 

The "Equipment Manager" node allows us in these cases to quickly change the "Equipment Server" configuration according to the changes in the auxiliary equipment. We change the configuration by sending the new desired configuration to the "Equipment Manager" ROS service. When the Equipment Manager receives the new desired configuration, it overwrites the actual_config file and restarts the "Equipment Server" by calling the node’s restart service. In this way, the "Equipment Server" reconfigures itself according to the new configuration file. Two additional "Equipment Manager" ROS services allow the user to read the current active configuration from the module and obtain an empty configuration template with default parameter values. The configuration files are of type yaml. They are human readable and can thus be modified manually.



## Raspi ROS Terminal Client


Instead of writing or correcting configuration files manually, the `ROS package <https://github.com/ReconCycle/raspi-ros-client>` offers
a more user-friendly approach to handling configuration files. This package contains
a client that can communicate with the "Equipment Manager". When the client is started,
it opens a terminal window user-interface that guides the user through creating or modifying
configuration files. At the beginning, the client searches for all "Equipment Managers" from the
different modules in its reach and offers the user to select the one he wants to configure. In the
next steps, the user can choose whether to modify the currently active configuration file or start
over with a blank template. According to the selected option, the client then reads the correct
configuration file from the "Equipment Manager". When changing the configuration, the user
only needs to answer the questions about the various parameter values asked by the terminal
guide. When the user is satisfied with the desired configuration, the client automatically changes
the yaml file and sends it to the module "Equipment Manager".





## RQT
//Not finished

## MSGS
//Not finished
https://github.com/ReconCycle/digital_interface_msgs


## Docker

To simplify the installation and process control of our ROS package on the module’s microcomputer, the ROS package is packed into the Docker container [15] and prepared for the
automatic setup of the system [18].



//Not finished
https://github.com/ReconCycle/raspi-reconcycle-docker

Integral part of:

https://github.com/ReconCycle/raspberry_reconcycle_init



These auxiliary devices are controlled by the modules' microcomputers. When the designed module is connected to the ROS network for the first time, the "Equipment Manager" allows easy configuration of the new equipment, which can then be controlled via the "Equipment Server".

The last two modules serve as a mounting platform for the two Franka Emika Panda robots. When the module with the robot is connected to the ReconCycle cell via Plug-and-Produce connectors, the robot control computer mounted in the module launches the robot control action servers, which are needed to control the robot via the ReconCycle cell ROS network. The auxiliary devices on the robot modules, such as tool changers and tools mounted on the robot, are controlled by the module's microcomputer, just like the auxiliary equipment on the other two modules.






**Table of contents:**

```{toctree}
:maxdepth: 2

raspi_rqt

```

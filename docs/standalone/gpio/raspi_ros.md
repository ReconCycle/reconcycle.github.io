# ROS managment of Raspberry Pi GPIOs



Raspberry Pi is microcomputer with the ability to generate control signals
and read the sensor values by attaching the auxiliary devices (equipment) to the GPIOs of
the Raspberry Pi. When the auxiliary equipment is connected to the GPIOs of the Raspberry
Pi, each GPIO in use must be properly configured by a suitable software library. Since the
auxiliary equipment attached to each individual microcomputer needs to work in synchronization with
the robots and the auxiliary equipment on other microcomputers, there is need to be able to control the
GPIOs of invidiual microcomputer globally throughout the cell. 





## Raspi ROS

Raspi ROS is the ROS package [ROS package](https://github.com/ReconCycle/raspi_ros) that
wraps the developed software library for configuring and controlling Raaspberry GPIOs in a ROS node.
This way enables the configuration and control of auxiliary devices through ROS services.
The cell programmer no longer needs to deal with GPIOs but can control and communicate
with the auxiliary equipment through ROS interfaces.


For the control and managment of Raspberries GPIOs are used two ROS nodes
running on each individual Raspberry microcomputer. The first ROS node is "Equipment Server", which configures control of the GPIOs connected equipment according to the module configuration file and forwards control commands from ROS services to the connected equip-
ment. The second ROS node is "Equipment Manager", which allows a user to modify the module’s configuration file via a ROS service.

### Equipment Server


When the "Equipment Server" node is started, it first reads the individual module’s configuration file actual_config, which is stored locally on the module’s microcomputer, and then configures the required GPIOs. The configuration file must contain information which additional equipment is attached to the module and to which GPIOs it is connected. Once GPIOs are configured, the "Equipment Server" creates a separate ROS service for each GPIO to control it. The names of the created ROS services are defined in the configuration file. In operation, the "Equipment Server" accepts the commands sent to its ROS services and controls the equipment connected to the GPIOs accordingly. Currently we have three different GPIO configurations and control interactions that "Equipment Server" can handle. The first possible configuration is a digital output where a service call can set the digital state of the GPIO, making it suitable for controlling devices such as pneumatic valves. The next configuration is a digital input that allows the digital state of devices such as digital sensors to be read on a service call. The last is a configuration that, according to the value in the service call, controls PWM signals that can be used to control devices such as step motors. The node also has a restart service that – when triggered – closes all active services, releases the pin’s hardware interface, and reads the configuration file again. Then it starts with the newly read configuration.

### Equipment Manager

 
The "Equipment Manager" node allows to quickly change the "Equipment Server" configuration according to the changes in the auxiliary equipment. It changes the configuration by sending the new desired configuration to the "Equipment Manager" ROS service. When the Equipment Manager receives the new desired configuration, it overwrites the actual_config file and restarts the "Equipment Server" by calling the node’s restart service. In this way, the "Equipment Server" reconfigures itself according to the new configuration file. Two additional "Equipment Manager" ROS services allow the user to read the current active configuration from the module and obtain an empty configuration template with default parameter values. The configuration files are of type yaml. They are human readable and can thus be modified manually.


### Installation

To make the micro-computer ROS-compatible, a Pi image with Ubuntu 16.04 and pre-installation of ROS is
mounted.
To simplify the installation and process control of Raspi-ROS package on the module’s microcomputer, the ROS package is packed into the [Docker container](https://github.com/ReconCycle/raspi-reconcycle-docker)  and prepared for the
 [automatic setup](https://github.com/ReconCycle/raspberry_reconcycle_init) of the system.
The used microcomputer is Raspberry Pi 4.



## Raspi ROS Terminal Client


Instead of writing or correcting configuration files manually, the [ROS package](https://github.com/ReconCycle/raspi-ros-client) offers
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


## Raspi-ros RQT tool

[Raspi-ros rqt tool](https://github.com/ReconCycle/rqt_raspi_ros.git) is an extension of the Raspi-ros terminal client. The tool allows you to modify templates through a graphical interface or directly control GPIOs for simulations."





**Table of contents:**

```{toctree}
:maxdepth: 2

raspi_rqt

```

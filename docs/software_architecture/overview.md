# Modular software architecture

To facilitate the implementation of modular reconfigurable workcells, we developed a software architecture that reflects hardware modularity and enables plug-and-produce connectivity within the workcell.
As the backbone, Robot Operating System (ROS) is used. It provides standardized interfaces to robots, sensors, grippers, and peripheral hardware elements and enables plug-and-produce connectivity and communication within the cell. Furthermore, toolchains for quick and efficient setup and programming on the workcell (task-level programming based on FlexBE, skill specification and workcell calibration by kinesthetic teaching) are integrated into the overall software architecture. 

The proposed design enables that the cell's functionalities can be expanded without disrupting the existing software architecture. This is supported by making use of Docker containers for the integration of new software modules. In the Docker containers, new modules can be deployed with all the necessary libraries without causing conflicts with any preexisting software packages. Developers can thus integrate new software without the need to reprogram any of the existing modules, which also eases the deployment of new hardware in the cell.

```{image} /figures/software/modules_2022.png
:alt: software reflects hardware modularity
:class: bg-primary
:width: 300px
:align: center
```

## Design guidelines 

## Integration of new peripheral devices

To support disassembly processes in the ReconCycle cell, various peripheral devices are integrated alongside robot manipulation capabilities. For example, the robot module must be able to activate or deactivate the pneumatic tool changer mounted on top of the robot. Devices such as clamps or cutters require activation signals and state checks. We use Raspberry Pi 4 as the standard microcomputer. It provides control signals and reads sensor values by connecting peripheral devices to its GPIOs. Each GPIO must be properly configured using a suitable software library.

For global control and synchronization of peripheral equipment, we developed a ROS package that wraps the software library for configuring and controlling GPIOs. This allows configuration and control of peripheral devices through ROS services, eliminating the need for direct GPIO management. It consists of:
1. **Equipment Server**: Configures GPIOs based on the module's configuration file and forwards control commands from ROS services to the connected equipment.
2. **Equipment Manager**: Allows modification of the module's configuration file via a ROS service.

To ease configuration management, we developed a ROS package with a user-friendly interface for handling configuration files. The interface communicates with the Equipment Manager, guiding the user through creating or modifying configuration files. For simplified deployment, the ROS package is packed into a Docker container.

- [Equipment Server Documentation](https://reconcycle.github.io/standalone/gpio/raspi_ros.html#equipment-server)
- [Equipment Manager Documentation](https://reconcycle.github.io/standalone/gpio/raspi_ros.html#equipment-manager)
- [Configuration Management Client Documentation](link_to_document)
- [Docker Container Setup Documentation](link_to_document)

## Integration of new robots

## Development of new robot skills

## Task-level programming

Due to a well-developed graphical user interface, FlexBE framework has been employed in the ReconCycle project to facilitate the creation of complex robot behaviors for disassembly tasks without manual coding. This section provides an overview of FlexBE states and behaviors. Each state represents a specific action or step in a robot’s behavior. Behaviors in the FlexBE frame-work are essentially state machines, meaning that behaviors are constructed by connecting individual states through transitions.

We have prepared corresponding FlexBE states for executing robot trajectories, controlling peripheral machinery, manipulating process data, etc., including:

- executing robot motions (in Cartesian or joint space),
- reading from and writing to the skill library (e.g., storing data acquired by kinesthetic teaching and initializing desired robot movements),
- triggering functionalities on peripheral devices (e.g., moving pneumatic grippers, vise, cutter) and operating the CNC milling machine,
- performing tool-changing process,
- obtaining results from the vision processing pipeline, including semantic scene analysis and action prediction.

## Helping tools



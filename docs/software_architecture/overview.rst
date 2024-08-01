Modular software architecture
=====================================

To facilitate the implementation of modular reconfigurable workcells, we developed a software architecture that reflects hardware modularity and enables plug-and-produce connectivity within the workcell.
As the backbone, Robot Operating System (ROS) is used. It provides standardized interfaces to robots, sensors, grippers, and peripheral hardware elements and enables plug-and-produce connectivity and communication within the cell. Furthermore, toolchains for quick and efficient setup and programming on the workcell (task-level programming based on FlexBE, skill specification and workcell calibration by kinesthetic teaching) are integrated into the overall software architecture. 

The proposed design enables that the cell's functionalities can be expanded without disrupting the existing software architecture. This is supported by making use of Docker containers for the integration of new software modules. In the Docker containers, new modules can be deployed with all the necessary libraries without causing conflicts with any preexisting software packages. Developers can thus integrate new software without the need to reprogram any of the existing modules, which also eases the deployment of new hardware in the cell.

Design guidelines 
-----------------

Integration of new peripheral devices
-------------------------------------

Integration of new robots
-------------------------

Development of new robot skills
-------------------------------

Task-level programming
----------------------

Due to a well-developed graphical user interface, FlexBE framework has been employed in the ReconCycle project to facilitate the creation of complex robot behaviors for disassembly tasks without manual coding. This section provides an overview of FlexBE states and behaviors. Each state represents a specific action or step in a robot’s behavior. Behaviors in the FlexBE frame-work are essentially state machines, meaning that behaviors are constructed by connecting individual states through transitions.

We have prepared corresponding FlexBE states for executing robot trajectories, controlling peripheral machinery, manipulating process data, etc., including:

- executing robot motions (in Cartesian or joint space),
- reading from and writing to the skill library (e.g., storing data acquired by kinesthetic teaching and initializing desired robot movements),
- triggering functionalities on peripheral devices (e.g., moving pneumatic grippers, vise, cutter) and operating the CNC milling machine,
- performing tool-changing process,
- obtaining results from the vision processing pipeline, including semantic scene analysis and action prediction.


Helping tools
--------------------------



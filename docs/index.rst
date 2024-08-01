======================================
Welcome to ReconCycle project documentation!
======================================

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Overview

   hardware/overview
   software_architecture/overview

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Manuals

   user_guide/index
   developer_guide/index
   tutorials/index

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Standalone tools

   standalone/urdf_converter/urdf_converter
   standalone/gpio/raspi_ros
   standalone/kinesthetic/index

.. meta::
   :description lang=en: Documentation for the software and hardware developed within the ReconCycle project.


ReconCycle aims to substantially reduce human effort and increase the accuracy and efficiency of recycling. As ReconCycle uses highly compliant robots, humans will be able to operate together with the machines to complete the missing steps. This reduces automation complexity further and brings this project into a feasible regime.

Documentation is organized as follows. The *Overview* section highlights key components, including the physical aspects of the system and the modular software architecture, which describes the flexible and scalable software framework supporting the project.
The *Manuals* section includes detailed user guides on hardware setup, the simulation system, the robot skill library, and the vision system. It also provides developer documentation for implementing new robotic skills and visual routines, along with example programs and tutorials for programming new disassembly tasks.
The section on *Standalone tools* describes standalone applications and scripts designed to support the implementation of common tasks within the ReconCycle ecosystem. These tools aim to improve the overall efficiency of programming the system. They include tools to create URDF models from CAD files in STEP format, and Raspberry GPIO configuration utilities, among others.

References
==========

If you use ReconCycle hardware or software elements in your work, please consider citing the following papers:

- M. Simonič, R. Pahič, T. Gašpar, S. Abdolshah, S. Haddadin, M. G. Catalano, F. Wörgötter and A. Ude. "Modular ROS-based software architecture for reconfigurable, Industry 4.0 compatible robotic workcells," 2021 20th International Conference on Advanced Robotics (ICAR), Ljubljana, Slovenia, 2021, pp. 44-51, doi: 10.1109/ICAR53236.2021.9659378.
- P. Radanovič, J. Jereb, I. Kovač and A. Ude. "Design of a Modular Robotic Workcell Platform Enabled by Plug & Produce Connectors," 2021 20th International Conference on Advanced Robotics (ICAR), Ljubljana, Slovenia, 2021, pp. 304-309, doi: 10.1109/ICAR53236.2021.9659345.

Links
=====

- `Project website <https://reconcycle.eu>`_
- `GitHub repositories <https://github.com/reconcycle>`_
- `Youtube channel <https://youtube.com/@reconcycle>`_
- `Follow us at LinkedIn <https://www.linkedin.com/company/reconcycle>`_
- `Internal Nextcloud repository <https://cloud.reconcycle.eu>`_


Funding
=======

.. image:: figures/main/rosin_eu_flag.jpg
   :width: 100px
   :align: left

This project has received funding from the European Union's `Horizon 2020 research and innovation programme under grant agreement No. 871352 <https://cordis.europa.eu/project/id/871352>`_.

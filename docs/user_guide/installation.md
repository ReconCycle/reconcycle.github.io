# Workcell Installation Manual

## Overview of Docker images

The ReconCycle workcell components are implemented within a set of Docker images containing key components, which facilitates quick setup & deployment. The [reconcycle dockers](http://github.com/ReconCycle/reconcycle_dockers) repository contains the information required to build Docker images (using Dockerfiles), and run/instantiate them to create Docker containers (using Compose files).

A brief description of Docker images and their functionality:

1. roscore - runs the ROS master server
2. reconcycle-base - base image for various other downstream images
3. reconcycle-rviz - enables visualization of the ReconCycle workcell
4. reconcycle-flexbe - runs the FlexBe software stack or runs scripts
5. reconcycle-moveit - runs the MoveIt ROS package to enable motion planning
6. qb-vsa - runs the software for controlling qbRobotic Variable Stiffness Gripper

### Vision system:

1. ros-basler - enables interfacing Basler camera with ROS network
2. ros-realsense - enables interfacing Realsense camera(s) with ROS network

### Robot control:

1. reconcycle-controller - contains the JointImpedance and CartesianImpedance controllers for the Franka Emika Panda robots

### Peripheral devices (CNC machine and Raspberry PIs within the modular tables):

1. reconcycle-cnc - enables controlling the CNC machine over ROS
2. reconcycle-raspi - enables controlling (pneumatic) valves within the workcell tables and on the robots, using a Raspberry PI's GPIO pins

## Overview of ReconCycle packages

In general, ReconCycle components can also be run outside of a Docker container, however in this case dependency management is more difficult.
A brief description of packages and their purpose:

1. [robotblocket_python](https://repo.ijs.si/leon/robotblockset_python) - enables control of Franka Emika Panda robots using Python code
2. [rbs_action_server](https://github.com/ReconCycle/rbs_action_server) - enables control of Franka Emika Panda over ROS
2. [disassembly_toolkit](https://github.com/ReconCycle/disassembly_toolkit) - contains robotic skills, various utilities for controlling the workcell, and scripts to run demos
3. [reconcycle_flexbe](https://github.com/ReconCycle/reconcycle_flexbe) - contains the FlexBe states and behaviors to enable Task-level programming
4. [vision_pipeline](https://github.com/ReconCycle/vision_pipeline) - contains the Vision System elements
5. [ros_vision_pipeline](https://github.com/ReconCycle/ros_vision_pipeline) - enables interfacing the Vision System with the ROS network
6. [context_action_framework](https://github.com/ReconCycle/context_action_framework) - contains elements to enable interfacing/receiving results from the Vision System using ROS
7. [cnc_manager](https://github.com/ReconCycle/cnc_manager) - enables control of the CNC mill over ROS
8. [workcell_lifecycle_manager](https://github.com/ReconCycle/workcell_lifecycle_manager) - utilities to start and stop the entire workcell and the components

## Installation Prerequisites

Using a Linux-based operating system (distribution) is recommended. For example, [Ubuntu](https://ubuntu.com/) can be used as it's known to be a user-friendly and well-supported distribution. We recommend using a Long-term Support (LTS) release, so key security updates will be available for several years to come.

To run the Docker images/containers, Docker must be installed as per [instructions](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository). Installation using the APT repository is recommended.

For computers running the Vision system, using a modern nvidia graphics card is required (nvidia 1080Ti or better) to speed up the processing of images. The [CUDA toolkit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) must be installed as per instructions.

For computers running robot controllers, it is necessary to apply a real-time kernel patch.

## Building Docker images

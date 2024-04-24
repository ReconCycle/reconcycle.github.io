Workcell Installation Manual
============================

Overview
---------------

The ReconCycle workcell components are implemented as a set of Docker images containing key components, which facilitates quick setup & deployment. The [reconcycle-dockers](https://github.com/ReconCycle/reconcycle_dockers) repository contains the information required to build Docker images (using the Dockerfiles), and run/instantiate them to create Docker containers (using Compose files).

A brief description of Docker images and their functionality:
1. roscore - runs the ROS master server
2. reconcycle-base - base image for various other downstream images
3. reconcycle-rviz - enables visualization of the ReconCycle workcell
4. reconcycle-flexbe - runs the FlexBe software stack or runs scripts
5. reconcycle-moveit - runs the MoveIt ROS package to enable motion planning
6. qb-vsa - runs the software for controlling qbRobotic Variable Stiffness Gripper

Vision system:
1. ros-basler - enables interfacing Basler camera with ROS network
2. ros-realsense - enables interfacing Realsense camera(s) with ROS network

Robot control:
1. reconcycle-controller - contains the JointImpedance and CartesianImpedance controllers for the Franka Emika Panda robots

Installation Prerequisites
---------------
Using a Linux-based operating system (distribution) is recommended. For example, [Ubuntu](https://ubuntu.com/) can be used as it's known to be a user-friendly and well-supported distribution. We recommend using a Long-term Support (LTS) release, so key security updates will be available for several years to come.

For computers running the Vision system, using a modern nvidia graphics card is required (nvidia 1080Ti or better) to speed up the processing of images. The [CUDA toolkit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) must be installed as per instructions.

To run the Docker images/containers, Docker must be installed as per [instructions](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository). Installation using the APT repository is recommended.




.. toctree::
    workcell_visualization/index
    flexbe/index
    vision_pipeline/index
    robot_controllers/index

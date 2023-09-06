Manual
===============

Conversion of STEP file to URDF package will be demonstrated on the example of simple robotic arm [] and using docker image.


Envirotment praparation
-----------


First we need to download the builded docker:

.. code-block:: bash

    docker pull ghcr.io/reconcycle/urdf-from-step:latest


The we download the example case adn delete already solution

.. code-block:: bash

    git clone https://github.com/ReconCycle/urdf-from-step-examples.git

    mkdir input_step_files
    cp urdf-from-step-examples/examples/robot_arm/input_step_files/robot_arm.step input_step_files/
    mkdir output_ros_urdf_packages

Prepare two folders, first with step file, second for created urdf package. For example we gona take step of simple robot arm: this



Conversion
------------



The prepared step file is turned to the corresponding ROS package containing URDF like this:

.. code-block:: bash

    docker run  -v ~/input_step_files:/input_step_files -v ~/output_ros_urdf_packages:/output_ros_urdf_packages  --rm ghcr.io/reconcycle/urdf-from-step:latest roslaunch urdf_from_step build_urdf_from_step.launch step_file_path:="/input_step_files/robot_arm.step" urdf_package_name:="robot_arm"
 
 
Its normal tha node dies: REQUIRED process [urdf_creator-2] has died! process has finished cleanly





Run builed package
----------------------
The created package needs to be added to the catkin workspace for building, sourcing, and launching:


.. code-block:: bash

    mkdir -p ~/ros_ws/src 
    cp -r ~/output_ros_urdf_packages/robot_arm ~/ros_ws/src/robot_arm
    cd ros_ws
    catkin build robot_arm
    source devel/setup.bash
    roslaunch robot_arm load_urdf.launch

Gui for joint state publisher starts up

Visualization
-----------


Like this:
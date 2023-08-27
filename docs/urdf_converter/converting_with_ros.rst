Conversion
===============


Runing
-----------

The prepared step file is turned to the corresponding ROS package containing URDF like this:

.. code-block:: bash

    roslaunch urdf_from_step build_urdf_from_step.launch step_file_path:="/input_step_files/robot_arm.step" urdf_package_name:="robot_arm"


The created package needs to be added to the catkin workspace for building, sourcing, and launching:

.. code-block:: bash

    catkin build robot_arm
    cd catkin_ws
    source devel/setup.bash
    roslaunch robot_arm load_urdf.launch

Run with docker
-----------



First pull the builded docker

.. code-block:: bash

    docker pull ghcr.io/reconcycle/urdf-from-step:latest


Prepare two folders, first with step file, second for created urdf package. For example we gona take step of simple robot arm: this



.. code-block:: bash

    roslaunch urdf_from_step build_urdf_from_step.launch step_file_path:="/input_step_files/robot_arm.step" urdf_package_name:="robot_arm"



Visualization
-----------


Like this:
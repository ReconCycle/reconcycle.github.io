Development manual
===============


Run with development compose:

.. code-block:: bash

    cd docker-compose/devel/
    docker-compose up

Run with development directly:

.. code-block:: bash

    docker run -it -v ~/urdf_from_step:/ros_ws/src/urdf_from_step -v ~/input_step_files:/input_step_files -v ~/output_ros_urdf_packages:/output_ros_urdf_packages ghcr.io/reconcycle/urdf-from-step:latest

rename step to test.step

Inside docker

.. code-block:: bash

    catkin build urdf_from_step
    roslaunch urdf_from_step build_urdf_from_step.launch step_file_path:="/input_step_files/robot_arm.step" urdf_package_name:="robot_arm"


Build release docker image:

.. code-block:: bash
    
    docker build -t ghcr.io/reconcycle/urdf-from-step:latest .

Test release docker image:

.. code-block:: bash

    docker run -it  -v ~/input_step_files:/input_step_files -v ~/output_ros_urdf_packages:/output_ros_urdf_packages  ghcr.io/reconcycle/urdf-from-step:latest roslaunch urdf_from_step build_urdf_from_step.launch step_file_path:="/input_step_files/robot_arm.step" urdf_package_name:="robot_arm"

Push release docker image:

.. code-block:: bash

    docker image push ghcr.io/reconcycle/urdf-from-step:latest
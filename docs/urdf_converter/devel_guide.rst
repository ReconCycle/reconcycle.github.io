Development manual
===============


Run with development compose:

.. code-block:: bash

    cd docker-compose/devel/
    docker-compose up

.. code-block:: bash

    docker run urdf-from-step:latest .......
    docker run -it -v /home/rok/catkin_ws/src/urdf_from_step:/ros_ws/src/urdf_from_step -v /home/rok/Documents/urdf-from-step-examples/examples/robot_arm/input_step_files:/input_step_files -v /home/rok/Documents/urdf-from-step-examples/examples/robot_arm/output_ros_urdf_packages:/output_ros_urdf_packages urdf-from-step:latest


Push builded docker image:

.. code-block:: bash
    
    docker build -t ghcr.io/reconcycle/urdf-from-step:latest .

    docker image push ghcr.io/reconcycle/urdf-from-step:latest



    docker run -it  -v ~/input_step_files:/input_step_files -v ~/output_ros_urdf_packages:/output_ros_urdf_packages  ghcr.io/reconcycle/urdf-from-step:latest roslaunch urdf_from_step build_urdf_from_step.launch step_file_path:="/input_step_files/robot_arm.step" urdf_package_name:="robot_arm"

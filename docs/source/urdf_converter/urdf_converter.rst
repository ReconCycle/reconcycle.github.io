URDF from STEP
===================================


This is ROS package for automated conversion of STEP models to URDF format. 
The program takes as input the STEP file (left images) of the desired robot or robot-like maschine and creates a new ROS package. 
The package created contains the URDF description, the STL mesh files required by URDF description, and the ROS launch file to load the data into the ROS for visualization (center images) and control (right images).


urdf-from-step-examples
-------------
Package manuals and examples of input and output data for package urdf_from_step.

## robot_arm example

Preparation of STEP file is on the example of a simple robot arm described [hier](https://github.com/ReconCycle/urdf-from-step-examples/tree/main/documentation/step_file_creation).

Instructions regarding conversion from STEP to URDF are provided in [hier](https://github.com/ReconCycle/urdf-from-step-examples/tree/main/documentation/step_to_urdf_conversion).

Instructions for URDF visualization are provided [hier](https://github.com/Re+conCycle/urdf-from-step-examples/tree/main/documentation/visualization).


<img src="./documentation/step_file_creation/figures/robot_arm_cad_with_cs.PNG" 
     height="200"   >  <img src="./documentation/visualization/figures/rviz tf center.png" 
     height="200"   >  <img src="./documentation/visualization/figures/rviz moved.png" 
     height="200"   >  

.. image:: figures_creating_step/robot_arm_cad_with_cs.PNG
   :width: 700px

.. image:: figures_creating_step/rviz_tf_center.png
   :width: 700px

.. image:: figures_creating_step/rviz_moved.png
   :width: 700px


.. note::

   This project is under active development.



.. toctree::
   :maxdepth: 1

   docker_use
   creating_step_file

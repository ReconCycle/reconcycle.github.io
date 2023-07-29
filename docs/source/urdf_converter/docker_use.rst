URDF
=====

Working principle2
-----------------

This is ROS package for automated conversion of STEP models to URDF format. 
The program takes as input the STEP file (left images) of the desired robot or robot-like maschine and creates a new ROS package. 
The package created contains the URDF description, the STL mesh files required by URDF description, and the ROS launch file to load the data into the ROS for visualization (center images) and control (right images).

Working principle
-----------------


The URDF file is generated in the following steps. First, the STEP file is loaded and its contents are analyzed using tools from the Open Cascade Technology (OCCT) library [1]. The analysis looks for keywords such as "joint" and "link" in the part names or in the assembly names in the model design tree. The instances with these keywords in their names represent the corresponding "joint" and "link" building blocks of URDF. The remaining part names containing the keyword encode the connections between individual URDF elements and their names in the URDF file. Once these instances and their connections have been identified, the correct local transformation between them must be computed from the values of their base coordinate systems in the STEP file. The calculated local transformations are transformed accordingly into the coordinate system values of the "joint" and "link" URDF definitions. The instances that do not have keywords in their names represent geometric shapes. They are transformed into the STL mesh specified in the appropriate local coordinate system according to the given URDF tree structure. From the collected and computed URDF data, the XML in URDF format is created using the urdfdom parser library. Finally, everything is stored in a newly created ROS package.


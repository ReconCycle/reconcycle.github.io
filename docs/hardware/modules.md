### ReconCycle Modules

#### Robot Module

Franka Emika Robot system includes the Arm and its Control. The force sensitive and agile arm features 7 DOF with torque sensors at each joint, industrial-grade pose repeatability of +/- 0.1 mm and negligible path deviation even at high velocities. It comes with a payload of 3 kg, a reach of 855 mm and a workspace coverage of 94.5%.

FCI is an interface allowing for low-level programming and control schemes, providing the current status of the robot and enabling its direct torque control, at 1 kHz. On top of the C++ interface libfranka, integration with the most popular ecosystems ROS, ROS 2 and MATLAB & Simulink.

<img src="https://www.eurobin-project.eu/images/IKR_FR3_noFE_v2-1.png" width="373" height="549">

#### Vise Module

The vise module in our ReconCycle system is designed to adapt to different products. This section details the construction that enables this adaptability, the design constraints considered, and some limitations of the system.

The overall design of the vise is depicted in Figure 10. Externally, the vise appears as a simple housing with four sliding jaws. Internally, a system of linear guides and actuators, shown in Figure 11, along with the control system located in the archetypical module, ensures that the inserted object is always centered in the vise.

To keep the automation of disassembly tasks affordable, the system does not use encoders. Instead, simple directional pneumatic 5/3 valves control the motion. The vise operates by synchronizing the movement of two opposing jaws using independent speed controllers. The pneumatic system's inherent property ensures pressure equilibrium across all parts, moving towards the midpoint with equal but opposing forces. This system is less precise than systems using proportional pneumatic valves with position encoders, but this does not pose a problem for the disassembly procedure. Devices entering the process are often imprecise, requiring computer vision (detailed in ReconCycle deliverable D2.1) to correct positioning inaccuracies. The combined synergies of hardware adaptability, tool design, computer vision, and intelligent robot control allow us to overcome challenges in deploying automated solutions in unpredictable environments.

ReconCycle focuses on the disassembly of small electronic appliances such as heat cost allocators and fire alarms. The vise's work area capacity should be determined by the largest product dimensions in these device families. The largest dimension within the heat cost allocator family is 130 mm in length and 50 mm in width. The largest fire alarm in our collection has a diameter of 110 mm. Allowing for some breathing room, a vise with a maximum opening of 140x115 mm should handle all relevant devices. The vise design is scalable and can be easily upgraded to accommodate larger device families with minimal investment in time and money.


#### Cutter Module 

The cutter module is a critical component of the ReconCycle workcell, designed to separate lithium batteries from other components while keeping the batteries undamaged. The workcell's adaptability allows it to disassemble various types of devices within the same family and entirely different device types. Each device has a unique casing, different PCB layouts, and varying battery locations, shapes, and sizes (see Figure 12). This necessitates a highly adaptable process for this crucial step.

The cutter module performs its task by cutting away the PCB around the battery until only the battery and a small but acceptable portion of the PCB remain. Some devices require a single cut, while others may need two or three cuts to completely separate the battery. The robot inserts the PCB/battery assembly into the cutting chamber, the blade lowers, and the separated battery and PCB parts slide down the ramp, ready to be sorted by the robot. Despite its apparent simplicity, several issues need to be addressed for an effective cutting process.

The cutter, shown in Figure 13, is designed to handle a wide variety of PCB/battery combinations. The frame is made of welded steel tubing, featuring linear guides for the blade and a fixed cutting surface. A pneumatic cylinder at the top of the frame provides the necessary cutting force. The blade is housed in a stainless steel casing at the back and transparent protective plastic at the front to contain the cutting process's outcomes, while still providing a sufficiently wide workspace for robot access in different configurations.

Inside the cutting chamber is a hardened steel blade capable of cutting through tough PCB composite, metal conductors, and other PCB parts. An adjustable end-stop behind the blade ensures precise insertion of the PCB/battery assembly, allowing for accurate cutting and minimal PCB remnants on the battery leads. The chamber and cutting surface are regularly cleaned with compressed air, ensuring that everything entering the cutter exits it properly sorted and ready for disposal.


#### CNC Module

#### Vision Module
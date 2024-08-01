# Context Action Framework

This package provides a collection of common class definitions that feature extractors (e.g., in vision pipeline) and action predictors should use.

## Introduction

The system is split into the following components:

- Context
- Action Blocks:
  - Cut Block
  - Lever Block
  - Move Block
  - Push Block
  - Turn Over Block
  - Vice Block
  - Vision Block

## Context

The context is defined as the state of the system including the work-cell module that is being operated in, the positions of objects in the system, and the state of the robots and the modules.

These are all specified as enums in [types.py](https://github.com/ReconCycle/context_action_framework/blob/main/src/context_action_framework/types.py).


The modules are:
- vision
- panda1
- panda2
- vice
- cutter

The robots are:
- panda1
- panda2

The End effectors are:
- soft hand
- soft gripper
- screwdriver

The Cameras are:
- basler
- realsense

The Labels of objects are:
- hca
- hca_empty
- smoke_detector
- smoke_detector_insides
- smoke_detector_insides_empty
- battery
- pcb
- internals
- pcb_covered
- plastic_clip
- wires
- screw
- battery_covered
- gap

The faces of the HCAs and smoke detectors are:
- front
- back
- side 1
- side 2

The actions are:
- none
- start
- end
- cut
- lever
- move
- push
- turn over
- vision
- vice

These are all specified as enums in [types.py](https://github.com/ReconCycle/context_action_framework/blob/main/src/context_action_framework/types.py).

## Device Names

![Diagram](./device_chart.png)

HCA names:

1. kalo2
2. minol
3. kalo
4. techem
5. ecotron
6. heimer
7. caloric
8. exim
9. ista
10. qundis
11. enco
12. kundo
13. qundis2

Smoke detector names:
1. senys
2. fumonic
3. siemens
4. hekatron
5. kalo
6. fireangel
7. siemens2
8. zettler
9. honeywell
10. esser

The context action framework provides a function `lookup_label_precise_name` to get the device name given the device number. See [types.py](https://github.com/ReconCycle/context_action_framework/blob/main/src/context_action_framework/types.py).


## ROS Detection Message Format

The context action framework provides the `Detection` class, defined in [types.py](https://github.com/ReconCycle/context_action_framework/blob/main/src/context_action_framework/types.py). There are two helper functions `detections_to_ros` and `detections_to_py` to convert a python `Detection` object to a ROS [`Detection.msg`](https://github.com/ReconCycle/context_action_framework/blob/main/msg/Detection.msg) and from ROS message back to python object.

Each detection has the following attributes:
- id (int): index in detections list
- tracking_id (int): unique ID per label that is stable across frames.

- label (Label): hca/smoke_detector/battery...
- label_face (LabelFace/None): front/back/side1/side2
- label_precise (str/None): 01/01.1/02...
- label_precise_name (str/None): kalo/minal/fumonic/siemens/...
- score (float): segmentation confidence

- tf_px (Transform): transform in pixels
- box_px (array 4x2): bounding box in pixels
- obb_px (array 4x2): oriented bounding box in pixels
- center_px (array 2): center coordinates in pixels
- polygon_px (Polygon nx2): polygon segmentation in pixels

- tf (Transform): transform in meters
- box (array 4x3): bounding box in meters
- obb (array 4x3): oriented bounding box in meters
- center (array 3): center coordinates in meters
- polygon (Polygon nx3): polygon segmentation in meters

- obb_3d (array 8x3): oriented bounding box with depth in meters

- parent_frame (str): ROS parent frame name
- table_name (str/None): table name of detection location
- tf_name (str): ROS transform name corresponding to published detection TF

some of the parameters are given both in pixel coordinates and in real-world coordinates. The pixel coordinates correspond to the pixels on the image. The Real-world coordinates are either w.r.t. the work surface bottom left corner, or to the camera.

The **ID** is the index of this detection in the list of detections.

The **tracking ID** is the ID given to the tracked detection that remains constant over multiple images, so long as the component is being tracked successfully.

The **label** is the class of the component or device.

The **face label** is the face of the device that is showing. It can be viewed as the discrete orientation of the device w.r.t. the camera. The possible faces are: front, back, side1, side2. \red{actually side1, side2, were used in the beginning of the project but not used much and therefore later examples in the data did not include this.}

The **precise label** is the classification of the HCA front/back and smoke detector front/back.

The **score** is the confidence score given by the segmentation network for the component.

The **transform** is the 6D position and rotation of the centre of the component.

The **box** is the bounding box of component.

The **obb** is the oriented bounding box of the component.

The **center** is the centre position of the component.

The **polygon** is the polygon mask of the component.

The **OBB 3D** is the 3D oriented bounding box of the component.

When depth estimation is not available, a hard-coded height value is used. This height value is dependent on the object, since we know that the height of HCAs lies between 25-30mm and the height of smoke detectors lies between 30-60mm.
<!-- , see \autoref{table:smoke_detector_hca_size_range}. -->


## Action Blocks

An action block is a high level specification of an operation that can be carried out on the Reconcycle cells. The action block can be a physical movement, an information extractor from the physical environment, or a combination of the two.

Action blocks are high level blocks and an action block can consist of multiple actions, for example, the cut block moves an object into the cutter, and then the cutter is activated to cut the object.


### [Cut Block](https://github.com/ReconCycle/context_action_framework/blob/main/msg/CutBlock.msg)

The cut block should specify the initial position of the object and the cutter module, where the object is to be cut.

[CutBlock.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/CutBlock.msg):
- enum from_module
- Transform from_tf
- enum to_module
- Transform to_tf
- array obb_3d
- enum robot
- int end_effector

[CutDetails.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/CutDetails.msg):
- bool success

### [Lever Block](https://github.com/ReconCycle/context_action_framework/blob/main/msg/LeverBlock.msg)

The lever block should specify from where to where to carry out the levering action and with which end effector and robot.

[LeverBlock.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/LeverBlock.msg):
- enum module
- Transform from_tf
- Transform to_tf
- array obb_3d
- enum robot
- enum end_effector

[LeverDetails.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/LeverDetails.msg):
- bool success

### [Move Block](https://github.com/ReconCycle/context_action_framework/blob/main/msg/MoveBlock.msg)

The move block specifies the start and end positions of an object and which end effector and robot should do the moving.

[MoveBlock.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/MoveBlock.msg):
- enum from_module
- Transform from_tf
- enum to_module
- Transform to_tf
- array obb_3d
- enum robot
- enum end_effector

[MoveDetails.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/MoveDetails.msg):
- bool success

### [Push Block](https://github.com/ReconCycle/context_action_framework/blob/main/msg/PushBlock.msg)

The push block specifies the start and end positions of the pushing action and with which robot and end effector the push action should be carried out with.

[PushBlock.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/PushBlock.msg):
- enum module
- Transform from_tf
- Trnasform to_tf
- array obb_3d
- enum robot
- enum end_effector

[PushDetails.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/PushDetails.msg):
- bool success

### [Turn Over Block](https://github.com/ReconCycle/context_action_framework/blob/main/msg/TurnOverBlock.msg)

The turn over block specifies the position and 3d oriented bounding box of the object that should be picked up, rotated 180 degrees, and placed down again, with the specified robot and end effector.

[TurnOverBlock.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/TurnOverBlock.msg):
- enum module
- Transform tf
- array obb_3d
- enum robot
- enum end_effector

[TurnOverDetails.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/TurnOverDetails.msg):
- bool success

### [Vice Block](https://github.com/ReconCycle/context_action_framework/blob/main/msg/ViceBlock.msg)

The vice block specifies whether the vice should clamp and turn over or only clamp, or only turn over.

[ViceBlock.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/ViceBlock.msg):
- enum module
- bool clamp
- bool turn_over

[ViceDetails.msg](https://github.com/ReconCycle/context_action_framework/blob/main/msg/ViceDetails.msg):
- bool success

### [Vision Block](https://github.com/ReconCycle/context_action_framework/blob/main/msg/VisionBlock.msg)

The vision block specifies whether gap detections should be carried out, which camera to use and above which module. Gap detection is only possible with the realsense camera and also only the realsense camera can be moved to a specified position.

The gap detection is useful for levering actions. The parts detection is useful for moving actions. All coordinates of parts are given in world coordinates with respect to the module.

The parts detection uses a neural network called Yolact for parts segmentation. It uses a kalman filter for tracking and reidentification.

The gap detection uses the depth image and a classical clusturing approach to determine gaps in the device.

The vision details are a list of detections and gaps (if gap detections were requested and available).

[VisionBlock](https://github.com/ReconCycle/context_action_framework/blob/main/msg/VisionBlock.msg):
- enum camera
- enum module
- transform tf
- bool gap_detection

[VisionDetails](https://github.com/ReconCycle/context_action_framework/blob/main/msg/VisionDetails.msg):
- bool gap_detection
- Detection[] detections
- Gap[] gaps

A detection is defined as the whole or part of a device.

[Detection](https://github.com/ReconCycle/context_action_framework/blob/main/msg/Detection.msg):
- int id
- int tracking_id
- enum label
- float score
- Transform to_px
- array box_px
- array obb_px
- array obb_3d_px
- Transform tf
- array box
- array obb
- array obb_3d
- array polygon_px

[Gap](https://github.com/ReconCycle/context_action_framework/blob/main/msg/Gap.msg):
- int id
- Transform from_tf
- Transform to_tf
- float from_depth
- float to_depth
- array obb
- array obb_3d

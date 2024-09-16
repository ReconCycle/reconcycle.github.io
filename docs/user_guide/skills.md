# Skill Library 

##Overview

Commonly used robot (or peripheral machine) operations/[skills](https://github.com/ReconCycle/disassembly_toolkit/tree/main/disassembly_pipeline/skills) are encapsulated within Skill classes, so they can be easily used either stand-alone or within a FlexBe state. An [abstract base skill](https://github.com/ReconCycle/disassembly_toolkit/blob/main/disassembly_pipeline/skills/base_skill.py) is also defined.

Common guidelines for developing skills are:

1. Skills should accept a robot object and peripheral objects as inputs, and only optionally instantiate them if not provided
2. Skills should make minimal assumptions about the state of the environment
3. Skills should prefer to take the Vision system's Detection objects as inputs
4. Higher-level skills may include execution of several primitive skills (e.g. the Move skill consists of Pick-up and Drop skills)

All skills inherit from `BaseSkill` and every skill is called with the `on_enter` method

##Available skills
The list of available skills, their descriptions and input arguments is below:

# Class/Method Overview

### Class: `BaseSkill`
Abstract base class for all skills, defining the framework for skill execution.
- **`__init__`**: Initializes the skill with keyword arguments.
- **`on_enter_pddl_`**: Passes arguments from PDDL to the skill's `on_enter`.
- **`on_enter`**: Abstract method, must be implemented by subclasses.

### Class: `ChangeTool`
Handles robot tool changing.

### Class: `SkillExecutionResult`
Data class to store the result of skill execution, including success status and any modified variables.

### Class: `CheckClampedObjectPDDLWrapper`
PDDL wrapper for verifying if an object is clamped securely for further operations.

### Class: `CheckClampedObject`
Skill for checking if an object is securely clamped in the CNC machine.

### Function: `find_hekatron_rotation`
Determines the orientation of the clamped object.

### Function: `move_to_look_pose`
Moves the robot to a position for inspecting the object.

### Function: `move_back`
Returns the robot to its initial position after inspection.

### Class: `CNCCutSmokeDetectorPDDLWrapper`
PDDL wrapper for cutting a smoke detector using a CNC machine.
- **`__init__`**: Initializes the skill name and arguments.
- **`pddl_init`**: Sets up the PDDL problem, defining actions and their preconditions.
- **`pddl_loop`**: Continuously updates the PDDL environment during operation.

### Class: `ChangeRobotToolPDDLWrapper`
PDDL wrapper for robot tool changing.
- **`__init__`**: Defines the tool-changing logic and arguments for the PDDL environment.
- **`pddl_init`**: Modifies the PDDL problem to reflect robot-tool relations.
- **`pddl_loop`**: Dynamically updates the PDDL problem during execution.

### Class: `DrillBatteryContacts`
- **`__init__`**: Initializes the skill for drilling battery contacts.

### Class: `DropObjectPDDLWrapper`
PDDL wrapper for dropping an object with a robot.
- **`__init__`**: Defines the action name, arguments, and description.
- **`pddl_init`**: Adds actions for dropping an object at a location.
- **`pddl_loop`**: Dynamically updates the PDDL environment during execution

### Class: `JMoveAboveTable`
Moves a robot with an eye-in-hand camera to a location above a table.
- **`__init__`**: Loads the pose database.
- **`on_enter`**: Moves the robot to a specific location.

### Class: `DrillBatteryContactsPDDLWrapper`
PDDL wrapper for drilling battery contacts.
- **`__init__`**: Initializes the skill for drilling with descriptions and arguments.
- **`pddl_init`**: Sets up the PDDL problem for drilling.
- **`pddl_loop`**: Updates the problem dynamically during execution

### Class: `ExceptionHandlingSkillWrapper`
Provides exception handling and retry mechanisms for skills.
- **`on_enter`**: Re-executes a skill if a failure is detected.
- **`vision_loop`**: Runs a vision-based loop to check object detection and execute recovery actions

### Function: `perform_DMP`
Performs a dynamic movement primitive (DMP) using either joint or Cartesian space.
- **`perform_DMP`**: Loads and executes a DMP trajectory on a robot. Supports both joint and Cartesian trajectories

### Class: `SelectCameraPDDLWrapper`
PDDL wrapper for selecting a camera.
- **`__init__`**: Defines the camera selection skill and maps camera names to topics.
- **`pddl_init`**: Adds camera objects and actions to the PDDL problem.
- **`pddl_loop`**: Dynamically updates the PDDL problem during execution.

### Class: `ClampPDDLWrapper`
PDDL wrapper for clamping an object.
- **`__init__`**: Defines the clamping skill.
- **`pddl_init`**: Sets up actions for clamping in the PDDL environment.
- **`pddl_loop`**: Continuously updates the PDDL environment.

### Class: `UnclampPDDLWrapper`
PDDL wrapper for unclamping an object.
- **`__init__`**: Defines the unclamping skill.
- **`pddl_init`**: Adds actions for unclamping in the PDDL problem.
- **`pddl_loop`**: Dynamically updates the PDDL problem

### Class: `DropObject`
A skill for dropping an object at a specified location.
- **`__init__`**: Loads configuration for drop locations and initializes the robot.
- **`on_enter`**: Moves the robot to the drop location and drops the object.

### Class: `EstimateBatteryContactPose`
Estimates the position for drilling battery contacts.
- **`on_enter`**: Detects battery contacts and generates drill points for drilling.

### Class: `DrillTask`
A data class for representing drilling tasks.
- **`__post_init__`**: Ensures that valid drilling parameters are provided.

### Class: `KaloRemotusOpening`
A skill for opening the KaloRemotus smoke detector using the QB VSA gripper.
- **`__init__`**: Initializes the skill with specific robot and gripper parameters.
- **`on_enter`**: Executes the process of opening the smoke detector.

### Class: `QBKaloDisassembly`
A class that contains all the steps needed to open the KaloRemotus smoke detector.
- **`step_1_move_to_init`**: Moves the robot to the initial position.
- **`step_2_cartesian`**: Switches to Cartesian control and moves the robot to a specific pose.
- **`step_3_detect_gap`**: Detects the gap in the smoke detector using force control.
- **`step_4_rotate_while_pushing_down`**: Rotates the tool while applying downward force.
- **`step_5_rotate_vertical`**: Rotates the tool to a vertical position.
- **`step_6_B`**: Pushes into the smoke detector while rotating

### Class: `Levering`
Skill for levering out a PCB from an HCA object.
- **`__init__`**: Initializes the levering skill with action arguments and description.
- **`get_valid_args_regex`**: Returns a valid regex for PDDL arguments based on object classes.
- **`pddl_init`**: Static method to modify the PDDL environment.
- **`pddl_loop`**: Dynamic method to update the PDDL problem

### Class: `LeveringPDDLWrapper`
PDDL wrapper for the levering skill.
- **`__init__`**: Initializes the PDDL action for levering with robot, location, and object arguments.
- **`pddl_init`**: Adds the levering action and its preconditions to the PDDL problem.
- **`pddl_loop`**: Dynamically updates the PDDL environment

### Class: `LinearPneumaticCuttingPDDLWrapper`
PDDL wrapper for using a pneumatic guillotine-style cutter.
- **`__init__`**: Defines the action for removing a battery from a PCB by cutting, with pose and type arguments.
- **`pddl_init`**: Adds a cutting action and preconditions for location and object to the PDDL problem.
- **`pddl_loop`**: Continuously updates the PDDL environment during execution

### Class: `PinpushPDDLWrapper`
PDDL wrapper for pushing a pin out of an object.
- **`__init__`**: Defines the action for pushing a pin from an object with robot object, location, and type arguments.
- **`pddl_init`**: Adds the pin-pushing action with its preconditions to the PDDL problem.
- **`pddl_loop`**: Dynamically updates the PDDL problem

### Class: `RobotHomingPDDLWrapper`
PDDL wrapper for homing a robot.
- **`__init__`**: Initializes the homing action with a robot argument.
- **`pddl_init`**: Adds the homing action and its effects to the PDDL problem.
- **`pddl_loop`**: Continuously updates the PDDL environment during execution

### Class: `MoveObjectPDDLWrapper`
PDDL wrapper for moving an object to a new location.
- **`__init__`**: Defines the action for moving an object with robot, location, and object arguments.
- **`pddl_init`**: Adds the move action and preconditions to the PDDL problem.
- **`pddl_loop`**: Updates the PDDL environment dynamically

### Class: `LookAtTable`
Skill for moving a robot with an eye-in-hand camera to inspect a table.
- **`__init__`**: Initializes the skill with a TF manager and configuration file.
- **`on_enter`**: Moves the robot to look at a specific table and subframe.

### Class: `RobotHoming`
Skill for homing a robot.
- **`on_enter`**: Moves the robot to its home position.
- **`execute`**: Placeholder for execution.
- **`on_exit`**: Placeholder for exiting the skill

### Class: `PickupDetectorTop`
Skill for picking up a smoke detector object using a robot's gripper.
- **`__init__`**: Initializes the skill with robot parameters, gripper settings, and movement configuration.
- **`on_enter`**: Moves the robot to pick up the smoke detector based on the provided object class and location.

### Class: `PickupObject`
Skill for picking up objects with a robot gripper.
- **`__init__`**: Initializes the pickup skill with robot settings, offset, and controller options.
- **`on_enter`**: Executes the pick-up sequence based on object class, location, and robot settings.
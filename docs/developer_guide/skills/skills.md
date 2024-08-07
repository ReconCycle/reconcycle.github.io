State and skill development
======

How to develop a new FlexBE state
--------------------

FlexBE states for custom actions can be developed by starting from the [generic state template](https://github.com/ReconCycle/reconcycle_flexbe/blob/main/reconcycle_flexbe_states/src/reconcycle_flexbe_states/example_state.py). 

The state can be constructed by defining the intialization parameters, input and output keys, and the commands that should be executed in each class method, i.e. each phase of the state.

Documentation of a FlexBE state that takes a name of the joint configuration as input, reads the corresponding joint values from the database and performs the robot motion, is shown below:

```python
class CallJointTrap(EventState):

    '''
    Calls JointTrapVelAction server

    ># joints_data string/int      The name of the joint configuration in MongoDB

    #< joint_values []             The data read from MongoDB from specific id (entry_name)

    <= continue                    Motion executed successfully
    <= failed                      Failed
    '''
```

| Type         | Identifier  | Purpose                                        |
|--------------|-------------|------------------------------------------------|
| Parameter    | --          | Argument to the state constructor, parametrizing the state instantiation. |
| Input Key    | >#          | Runtime data required by this state.          |
| Output Key   | #>          | Runtime data provided by this state.          |
| Outcome      | <=          | Possible result of execution.                 |

### Automatic state generation using Jinja

The above mentioned FlexBE states are typically associated with a ROS service or action server and can be realized (developed) using FlexBE's integrated proxies for ROS interfaces. However, most disassembly operations involve multiple steps. We have prepared a Python library of convenience functions called the *Disassembly Toolkit*, available at the [repository](https://github.com/reconcycle/disassembly_toolkit).

To enable simple creation of FlexBE states for these functions, we developed a template for new FlexBE states along with a Python script that generates code for their implementation. This approach allows for the development of complex high-level behaviors while concealing the low-level implementation details from the user. We thus prepared a Jinja template that automatically generates a FlexBE state with all the required building blocks, based on the provided initial parameters. 

We established a spreadsheet to catalog the required input parameters for each function within the *Disassembly Toolkit* library that we implemented using FlexBE. A few examples of spreadsheet entries, consisting of a function name and the function's input parameters, are displayed in the table below. To define the state generation process, a custom state name is chosen, along with the name of one of the existing method from *Disassembly Toolkit*, state parameters, and method parameters. Task specific parameters that are needed for the execution of a specific disassembly procedure can be passed as state parameters. The state parameters should include the required method parameters, which are used as inputs to individual functions of the disassembly cycle controller. Besides the provided input state parameters, the state can also make use of the global user data structure, which is available during the behavior execution.

| Method name      | State name    | Method parameters        | State parameters                          |
|------------------|---------------|--------------------------|-------------------------------------------|
| set_ee_config    | SetEEConfig   | ee_config                | robot name, end effector configuration    |
| cartesian_move   | CMove         | pose, duration, max. vel.| robot name, pose, duration                |
| joint_move       | JMove         | joints, duration, max. vel.| robot name, joints, duration             |
| error_recovery   | ErrorRecovery | /                        | robot name                                |

**Table 1:** Example of table entries for automatic generation of FlexBE states. For each method in the *Disassembly Toolkit* Python library, the state name and a set of input parameters are defined, which is needed to generate a state from the Jinja template.


How to develop a new skill
--------------------

Skills are similar to FlexBE states, but can be used as standalone functions in Python scripts. They can also be used within a FlexBE state, where they multiple skills may be combined. A selection of skills can be found at the [disassembly toolkit repository](https://github.com/ReconCycle/disassembly_toolkit/tree/main/disassembly_pipeline/skills). Their structure is similar to FlexBE states, but can be adapted as desired to include more functionalities. Creation of new skills can be done by adapting the [base skill](https://github.com/ReconCycle/disassembly_toolkit/blob/main/disassembly_pipeline/skills/base_skill.py) according to the desired functionality.

An example of a skill that performs an action of dropping an object to a specified location is shown below.

```python
import numpy as np
import json
import os
import time
import copy
from disassembly_pipeline.utils.tf_utils import GenericTransformListener
from .base_skill import BaseSkill
from robotblockset_python.transformations import *
from unified_planning.shortcuts import *

class DropObject(BaseSkill):
    def __init__(self, robot= None, 
                 name = "drop",
                 using_controller = 'JointPositionTrajectory',
                 move_above_z = 0.05,
                 description = "Use robot to drop an object."):
        
        """Generic function to drop an object with whichever gripper."""

        self.robot = robot
        
        self.Name = name
        self.using_controller = using_controller
        self.move_above_z = move_above_z
        self.description = description
    
        self.tflistener = GenericTransformListener()
        self.tf2x = self.tflistener.tf2x
        
    def on_enter(self, **kwargs):

        r = kwargs['robot']

        drop_location = kwargs['location']

        drop_tf_base_frame = drop_location.base_frame
        drop_tf = drop_location.drop_tf

        # Get drop position in robot base frame
        T1 = x2t(self.tf2x(r.Base_link_name, drop_tf_base_frame))

        drop_T = T1@drop_tf

        # Keep the robot EE orientation, for now
        r.GetState()
        drop_T[0:3, 0:3] = x2t(r.x)[0:3, 0:3]

        drop_T_above = copy.deepcopy(drop_T)
        drop_T_above[2, -1] += self.move_above_z

        # Fix for when we are using more than 2 controllers.
        if r._control_strategy != self.using_controller:
            r.Switch_controller(start_controller =  self.using_controller)

        r.error_recovery()

        if self.using_controller == 'CartesianImpedance':
            # Set low cart stiffness for moves
            r.SetCartesianStiff_helper(m=0.9, n=0.75)


        r.CMove(x = t2x(drop_T), t = 3, v_max_factor = 0.4, a_max_factor = 0.4)
        r.gripper.open(1, 10000, sleep=False, wait_for_result=False)

        return 0

    def execute(self):
        0
    def on_exit(self):
        0

    def pddl_init(self, problem, pddl_to_world_obj_links):
        """ Modify the PDDL problem, static means it runs when the PDDL env is initialized (add objects, predicates/fluents, operators...)."""

        # Other needed fluents
        holding = problem.fluent('holding')
        ontable = problem.fluent('on_table')
        clear = problem.fluent('clear')

        robot_type = UserType('robot')
        location_type = UserType('location')
        physical_object_type = UserType('physical_object')

        drop = InstantaneousAction('drop', robot = robot_type, loc=location_type, obj = physical_object_type)
        robot = drop.parameter('robot')
        loc = drop.parameter('loc')
        obj = drop.parameter('obj')

        drop.add_precondition(holding(obj, robot))

        drop.add_effect(holding(obj, robot), False)
        drop.add_effect(clear(obj), False)
        drop.add_effect(ontable(obj, loc), True)

        problem.add_action(drop)

        return problem, pddl_to_world_obj_links

    def pddl_loop(self, problem, pddl_to_world_obj_links):
        """ Modify the PDDL problem, dynamic means it runs in a loop (add objects, predicates/fluents)."""
        return problem, pddl_to_world_obj_links
```
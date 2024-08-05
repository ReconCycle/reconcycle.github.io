State and skill development
======

How to develop a new FlexBE state
--------------------

FlexBE states for custom actions can be developed by starting from the [generic state emplate](https://github.com/ReconCycle/reconcycle_flexbe/blob/main/reconcycle_flexbe_states/src/reconcycle_flexbe_states/example_state.py). 

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

Skills are similar to FlexBE states, but can be used as standalone functions in Python scripts or called from within a FlexBE state. A selection of skills can be found at the [disassembly toolkit repository](https://github.com/ReconCycle/disassembly_toolkit/tree/main/disassembly_pipeline/skills). Their structure is similar to FlexBE states, but can be adapted as desired to include more functionalities.

An example of a simple skill that performs waving with a robot arm is demonstrated below.

```python
from disassembly_pipeline.skills.base_skill import BaseSkill

class Armwave(BaseSkill):
    def __init__(self, name = "wave_robot_arm",
                 description = "The robot will wave to greet guests/bystanders. Arguments: Object, agent(robot).",):
       

        self.Name = name
        self.description = description

    @abstractmethod
    def on_enter(self, **kwargs):
        """ Function to call when first starting the skill."""
        
        robot = kwargs['robot']

        out = demo_armwave(robot)

        return out

    @abstractmethod
    def execute(self, **kwargs):
        """ Function that GETS CALLED periodically(possibly with high freq) during skill execution. """
        0

    @abstractmethod
    def on_exit(self, **kwargs):
        """ Function that gets called after the skill finishes."""
        0
        
    @abstractmethod
    def pddl_init(self, problem):
        """ Modify the PDDL problem, static means it runs when the PDDL env is initialized (add objects, predicates/fluents, operators...)."""
        0

    @abstractmethod
    def pddl_loop(self, problem):
        """ Modify the PDDL problem, dynamic means it runs in a loop (add objects, predicates/fluents)."""
        0

    
def demo_armwave(robot, n_repetitions = 3):
    """ """
    ### PARAMS
    max_vel = 3
    max_acc = 3
    
    assert robot.gripper.Name == 'softhand'
    
    p1_q_init = (-0.043995, -0.430550, -0.409195, -1.916245, -0.226683, 1.558691, 0.353183)

    p1_q1 = (0.130702, -0.795076, -0.402820, -1.999278, -0.049360, 2.756914, 0.444195)
    p2_q2 = (0.474790, -0.761872, -0.905444, -2.005180, -0.047051, 2.928837, 0.941880)
    p2_q3 = (0.480880, -0.810580, -0.485103, -2.139690, -1.024069, 3.103375, 0.833179) 
    ### END PARAMS
    
    if robot._control_strategy == 'CartesianImpedance':
        robot.Switch_between_cart_imp_and_joint_imp()
    robot.error_recovery()
    
    robot.gripper.open()

    robot.JMove(p1_q_init, t = 4)
    robot.JMove(p1_q1, t = 2)
    
    for i in range(0,n_repetitions):    
        robot.JMove(p2_q2, t = 1, max_vel = max_vel, max_acc = max_acc)
        #robot.JMove(p1_q1, t = 2)
        robot.JMove(p2_q3, t = 1, max_vel = max_vel, max_acc = max_acc)

    robot.JMove(p1_q1, t = 2)

    robot.JMove(p1_q_init, t = 4)
```
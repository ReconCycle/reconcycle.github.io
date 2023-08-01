Instalation
=====


Because of the challenging installation of the required python package [pythonOCC-core](https://github.com/tpaviot/pythonocc-core) is highly recommended to use a docker image.


Docker
------


Docker repository source is [hier](https://github.com/ReconCycle/urdf-from-step-docker).

Builded docker image is [hier](https://github.com/ReconCycle/urdf-from-step-docker/pkgs/container/urdf-from-step).

Pulling builded docker image:

.. code-block:: bash
    docker pull ghcr.io/reconcycle/urdf-from-step:latest







## Usage


The examples and manuals are provided [hier](https://github.com/ReconCycle/urdf-from-step-examples).

Preparation of STEP file is on the example of a simple robot arm described [hier](https://github.com/ReconCycle/urdf-from-step-examples/tree/main/documentation/step_file_creation).

The prepared step file is turned to the corresponding ROS package containing URDF like this:

```bash
roslaunch urdf_from_step build_urdf_from_step.launch step_file_path:="/input_step_files/robot_arm.step" urdf_package_name:="robot_arm"

```
The created package needs to be added to the catkin workspace for building, sourcing, and launching:

```bash
catkin build robot_arm
cd catkin_ws
source devel/setup.bash
roslaunch robot_arm load_urdf.launch
```


More detailed instructions regarding conversion from STEP to URDF are provided in [hier](https://github.com/ReconCycle/urdf-from-step-examples/tree/main/documentation/step_to_urdf_conversion).

Where also the instructions for URDF visualization are provided [hier](https://github.com/ReconCycle/urdf-from-step-examples/tree/main/documentation/visualization).

## References

* [1] pythonocc: Thomas Paviot. (2022). pythonocc (7.7.0). Zenodo. https://doi.org/10.5281/zenodo.3605364


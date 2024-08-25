# UrdfComposer



UrdfComposer is an [RViz plugin](https://github.com/ReconCycle/rviz_plugin_urdf_composer.git) that enables the simple composition of complex URDF xacros from the elemental xacros created with the ROS package [urdf_from_step](https://github.com/ReconCycle/urdf_from_step). It works by using a special xacro file that, in correspondence with parameters in a YAML file, includes elemental xacros in the desired configuration.


Tool is started with:
```bash
roslaunch rviz_plugin_urdf_composer urdf_composer.launch
```

The composed xacros can be created from scratch using the 'Initialize empty config file' button, or an existing xacro can be modified by selecting 'Select config YAML file'.

<img src="/standalone/urdf_converter/figures_rviz/tool.png" />

For example, the configuration file reconcyle_4x4.yaml was selected to load a configuration of four elemental Reconcyle modules in the following configuration shown in the image:

<img src="/standalone/urdf_converter/figures_rviz/loaded_4x4.png" />

After the initial configuration is loaded or during creation, each element can be deleted by pressing the 'Delete selected element' button, such as this camera desk module

<img src="/standalone/urdf_converter/figures_rviz/deliting_element.png" />

Adding a new elemental part to the composition is initiated by pressing the 'Select component URDF file' button. This opens a popup window where the appropriate file needs to be selected. The desired module for adding must be defined with the ROS package created using the urdf_from_step package. Inside this package, the xacro URDF file located in the URDF folder needs to be chosen. In this case, the Reconcyle module with the vise was selected:

<img src="/standalone/urdf_converter/figures_rviz/moving_part.png" />

Once loaded, the parent coordinate system from an already composed element needs to be chosen in the 'Choose assembly tf:' section. All tf coordinate systems from all composed elements are available for selection. Additionally, the child coordinate system on the new element needs to be selected in the 'Choose component tf:' section. Similar to the assembly, all tf coordinate systems from this element can be chosen. The desired transformation between the two coordinate systems can then be defined using markers visible in the previous image or more precisely by adjusting the values in the 'MOVING PART' section. A unique namespace name also needs to be chosen, enabling multiple elemental components to be added to the same composition. The current element is added by pressing the 'Add URDF' button, and the next desired element can then be manipulated:


<img src="/standalone/urdf_converter/figures_rviz/adding_aditional.png" />

Finally, the new composition description is saved by pressing the 'Save current config' button.
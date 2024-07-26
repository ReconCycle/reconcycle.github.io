### Archetypical module

Each module consists of a steel frame that provides rigidity and structural integrity. The frame includes an aluminum work surface, which facilitates the easy mounting of module-specific equipment. Additionally, the frame is mounted on castors to enable easy transportation of the module.

#### Electrical and Network Connectivity
Within the frame, there is basic electric wiring that distributes power to the module’s electronics, such as network switches and low voltage DC power supplies. The module also includes network wiring that connects the devices within the module (computers, cameras, controllers, etc.) and integrates them into the cell’s network through "Plug & Produce" (PnP) connectors.

#### Adding Equipment
Modules can be customized by adding additional equipment according to specific requirements. This includes computers, cameras, and controllers, which can be easily integrated to achieve the module’s desired functionality.

#### Software and Connectivity
Each module is equipped with sufficient computational hardware to run ROS nodes, exposing each module’s data and functionalities to the cell’s ROS environment. This allows the modules to be controlled by the top-level task scheduling software as soon as they are connected to the cell. The PnP connectors provide additional functionalities, such as pneumatic air or electric power, as required.

#### Computational Hardware
Each module includes a Raspberry Pi 4 micro-computer equipped with a "PoE Hat" to enable power via Power over Ethernet (PoE), reducing the need for separate power supplies. Additionally, each module contains a PoE-enabled network switch to connect devices like cameras to the network and supply power via PoE.


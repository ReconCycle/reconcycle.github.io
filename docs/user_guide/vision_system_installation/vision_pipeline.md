# Vision Pipeline

The [ros_vision_pipeline](https://github.com/ReconCycle/ros_vision_pipeline) is the docker container for the [vision_pipeline](https://github.com/ReconCycle/vision_pipeline).

## Installation

Folder structure:
```
ros_vision_pipeline/
vision_files/
├─ datasets/
├─ vision_pipeline/
```

1. Clone [ros_vision_pipeline](https://github.com/ReconCycle/ros_vision_pipeline):
```bash
git clone git@github.com:ReconCycle/ros_vision_pipeline.git
```
2. We pull all the submodules that are used in the catkin_ws. This includes the context action framework.
```
git submodule update --init --recursive
```

In the `docker-compose.yml` file, the volumes should be set correctly.

3. Clone [vision_pipeline](https://github.com/ReconCycle/vision_pipeline):
```bash
git clone git@github.com:ReconCycle/vision_pipeline.git
```

3. Copy the directory from the Nextcloud Reconcycle repository [git-data/vision-pipeline/data](https://cloud.reconcycle.eu/f/21297) to the `vision-pipeline/data_limited` folder.
4. `cp config.example.yaml config.yaml`

## Running The Pipeline

Run:
```bash
$ cd ros_vision_pipeline
$ docker-compose up -d
```

or
```bash
$ docker exec -it ros_vision_pipeline bash
```


## Prerequisites

You need to install the Nvidia graphics drivers and the CUDA toolkit. The Nvidia drivers are also bundled with CUDA, but I had trouble installing it this way.

### Installing Nvidia graphics drivers

Prequisites:
```
sudo apt install build-essential libglvnd-dev pkg-config
```
Now [download here the nvidia drivers](https://www.nvidia.com/Download/index.aspx) and run as root to install. The Nvidia drivers require gcc-9 which is what ubuntu ships with by default.

- You may need to disable the built in display driver: [disable display driver](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-nouveau)

### Installing CUDA toolkit

Install **CUDA 11.3** on your host system. Go to [Cuda Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) then click on **CUDA Toolkit 11.3**. Select your operating system and download the runfile. Run the runfile using `sudo`.

- You may need gcc version 8 to run CUDA 11.3. If so, run: `sudo apt install gcc-8 g++-8`. [Guide here](https://linuxize.com/post/how-to-install-gcc-on-ubuntu-20-04/) on how to switch gcc versions.

There is an installation guide for CUDA from nvidia [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-installation). You can have a look at it for reference.

### Docker running as root

First you need to install nvidia-container-runtime, [instructions here](https://nvidia.github.io/nvidia-container-runtime/) and run:
```
sudo apt-get install nvidia-container-runtime
```

Edit `/etc/docker/daemon.json` to contain:

```
{
    "default-runtime":"nvidia",
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```

Then: `sudo systemctl daemon-reload`

Check if runtime is added sucessfully:
`docker info|grep -i runtime`

### Docker running rootless (probably not what you want to do)

Do the same except put the file here: `~/.config/docker/daemon.json`.

Then: `systemctl --user daemon-reload`

Check if runtime is added sucessfully:
`docker info|grep -i runtime`

ONLY INSTALL DOCKER AFTER DOING THESE STEPS IF YOU ARE RUNNING ROOTLESS!

## Running Docker container

Make sure you have everything set up from the previous sections. Install [docker-compose](https://docs.docker.com/compose/install/).

Edit the `docker-compose.yml` file and remove the ROS master and Rviz if you already have these running elsewhere. In principle the `docker-compose.yml` file in its current state will provide you with a ROS master, and Rviz that can be accessed via the browser through the `novnc` container.

The container is running in `host` mode because this is the easiest way to give it access to the Basler camera. The `ROS_IP` needs to be set correctly. Do this by running `$ hostname -I` on the host and setting the `ROS_IP` to this IP (take the first one if it gives multiple IP addresses).
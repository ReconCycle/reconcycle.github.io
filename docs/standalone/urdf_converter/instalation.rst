Installation
=====


Because of the challenging installation of the required python package `pythonOCC-core <https://github.com/tpaviot/pythonocc-core>`_ is highly recommended to use a docker image.


Docker
------

The Docker repository source is available `here <https://github.com/ReconCycle/urdf-from-step-docker>`_ and can be built locally:

.. code-block:: bash

    git clone https://github.com/ReconCycle/urdf-from-step-docker.git
    cd urdf-from-step-docker
    docker build -t urdf-from-step .



Build docker image is available `here <https://github.com/ReconCycle/urdf-from-step-docker/pkgs/container/urdf-from-step>`_, and can be directly pulled like this:  

.. code-block:: bash

    docker pull ghcr.io/reconcycle/urdf-from-step:latest








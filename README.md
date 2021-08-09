# basic-test

```
docker run -it --device /dev/dri:/dev/dri \
               -v ${PWD}:/home/openvino/workdir \
               openvino/ubuntu18_data_dev:2021.4 \
               /bin/bash
```
docker pull 
docker run -it --device /dev/dri:/dev/dri \
               quay.io/devcloud/object-detection:2021.4_gpu
```
docker build -t ojjsaw/cpu-gpu-test:ubuntu18 .
docker build -t ojjsaw/cpu-gpu-test:ubuntu20 .
docker build -t ojjsaw/cpu-gpu-test:rhel8 .

docker run -it ojjsaw/cpu-gpu-test:latest
docker run -it -e DEVICE=CPU ojjsaw/cpu-gpu-test:latest
docker run -it --device /dev/dri:/dev/dri -e DEVICE=GPU --entrypoint /bin/bash ojjsaw/cpu-gpu-test:latest

docker run -it --device /dev/dri:/dev/dri -e DEVICE=GPU ojjsaw/cpu-gpu-test:latest


docker run -itu root:root --rm -v /var/tmp:/var/tmp --device /dev/dri:/dev/dri -e DEVICE=GPU --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb ojjsaw/cpu-gpu-test:latest
```


python3 docker_openvino.py build \
        --distribution runtime \
        --product_version 2021.4 \
        -os ubuntu20 \
        --build_arg no_samples=True

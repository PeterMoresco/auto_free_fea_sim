# How to install podman on Ubuntu 18.04


First u go to [here](https://clouding.io/hc/en-us/articles/360011382320-How-to-Install-and-Use-Podman-on-Ubuntu-18-04) and follow the instructions. They're pretty simple.
Then u go [here](https://github.com/containers/podman/blob/master/test/registries.conf) and puts this file on the /home/$(USER)/.config/containers/registries.conf
In the libpod.conf edit "cgroup_manager" and "events_logger" by [this](https://dev.to/bowmanjd/using-podman-on-windows-subsystem-for-linux-wsl-58ji), andd do the other stuff too.
The shadow-utils are installed like:
```
sudo apt install libvshadow-utils
```

To test just do:
```
podman run -it docker.io/library/alpine:latest
```

There u go, that's all u need.


# How to install podman on Ubuntu 18.04


First you go to [here](https://clouding.io/hc/en-us/articles/360011382320-How-to-Install-and-Use-Podman-on-Ubuntu-18-04) and follow the instructions. They're pretty simple.    
Then you go [here](https://github.com/containers/podman/blob/master/test/registries.conf) and puts this file on the /home/$(USER)/.config/containers/registries.conf.    
In the libpod.conf edit "cgroup_manager" and "events_logger" by [this](https://dev.to/bowmanjd/using-podman-on-windows-subsystem-for-linux-wsl-58ji), and follow the instructions in the article.        
The shadow-utils are installed like:
```
sudo apt install libvshadow-utils
```

To test just run:
```
podman run -it docker.io/library/alpine:latest
```

There you go, that's all you need.


# Prologue

This is a post to help the beginners to build the pwn enviroment.
Remember to keep the same enviroment with the server end or you would waste tons of hours.

# MY DEVICES
- Windows Laptop
- Intel Macbook Pro

# Windows
On windows, I use WSL(20.04), docker(16.04, 18.04, 20.04, and 22.04) and vmwares(16.04, 18.04, 20.04, and 22.04).
If you don't have big disk, you can try to use [pwn_debug][1] to build all the enviroment on one system. If you have enough disk space, building the VMs is a better choice before you know the `libc` and `ld`.

# Intel MAC

On MAC, I use vmware and docker, too.

# How to set up a VM


The procedure to build the VMs, assuming we already have vmare or visual studio.

1. Download the image from `https://releases.ubuntu.com/16.04/`, the desktop versions would give better using experience. (replace the version in url with the version you want to install)
2. Create a new vm on vmware or VBox. You can keep the defualt setting.
3. Run the corresponding [scripts][2] to install pwn related tools

# How to set up  docker env
Chose one:
```
docker pull n132/pwn:16.04
docker pull n132/pwn:18.04
docker pull n132/pwn:20.04
docker pull n132/pwn:22.04
```

Or you can build your own image (replace the 22.04 with the ubuntu version of your target)
```
docker pull library/ubuntu:22.04
docker run -it library/ubuntu:22.04 /bin/bash 
# install tools, there is a expamle in ./Docker/Ubuntu22.04.sh
docker commit u22 n132/pwn:22.04
docker push n132/pwn:22.04
```



[1]: https://github.com/ray-cp/pwn_debug
[2]: ./VM/
[2]: ./Docker/Ubuntu22.04.sh

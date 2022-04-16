gcc ./fs/exp.c -masm=intel --static -o ./fs/exp &&\
cd fs &&\
find . | cpio -o --format=newc > ../rootfs.cpio &&\
cd .. &&\
./start.sh
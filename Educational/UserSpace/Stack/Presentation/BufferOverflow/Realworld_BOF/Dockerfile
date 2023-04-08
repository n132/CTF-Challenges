FROM ubuntu:20.04


RUN  apt-get update && \
        apt-get -y dist-upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get install ca-certificates gcc make bison wget libglib2.0-dev -y 

WORKDIR /tmp

RUN	wget https://versaweb.dl.sourceforge.net/project/nbd/nbd/3.23/nbd-3.23.tar.gz && \
	tar -xvf nbd-3.23.tar.gz && \
	cd nbd-3.23 && \
	./configure --enable-debug && \
	make && \
	make install


COPY rootfs.ext2 /
COPY start.sh /

expose 10809

CMD ["/start.sh"]


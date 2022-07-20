# update
apt update
apt install vim gdb wget git curl nmap zsh python pip -y
# remove useless software
# install ipython
apt-get install ipython3 -y
# install pwntools
# apt-get install python2.7 python-dev git libssl-dev libffi-dev build-essential -y
pip3 install pwntools
# install on-my-zsh   
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

apt-get install gcc-multilib -y
# install peda pwngdb
cd ~/
git clone https://github.com/longld/peda.git ~/peda
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
# install one_gadget
apt install ruby ruby-dev gem -y
gem install one_gadget
gem install seccomp-tools
# install libc-database
#git clone https://github.com/niklasb/libc-database
#cd libc-database
#./get

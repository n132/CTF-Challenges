# update
apt update
apt install vim ipython3 gdb wget gcc-multilib git curl nmap zsh python pip -y --no-install-recommends
# install pwntools
pip3 install pwntools
# install on-my-zsh   
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

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

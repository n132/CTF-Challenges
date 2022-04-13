# update
apt update
apt install vim gdb wget git curl nmap zsh python-pip -y
# install pip
apt install python -y
# install ipython
apt-get install ipython -y
# install pwntools
pip install --upgrade pwntools
# install on-my-zsh   
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

apt-get install gcc-multilib -y
# install peda pwngdb
cd ~/
git clone https://github.com/longld/peda.git ~/peda
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
# install one_gadget
apt install gem ruby ruby-dev -y
gem install one_gadget
gem install seccomp-tools
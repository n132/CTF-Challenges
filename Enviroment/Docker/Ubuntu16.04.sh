# update
apt update
apt install vim gdb wget git curl nmap zsh python-pip -y
# install ipython
apt-get install ipython
# install pwntools
apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
pip install --upgrade pwntools
# install zsh   
apt-get install zsh git gcc-multilib -y
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# install peda+pwngdb
cd ~/
git clone https://github.com/longld/peda.git ~/peda
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
# install one_gadget
apt install gem ruby ruby-dev -y
gem install one_gadget
gem install seccomp-tools
# install libc-database
# git clone https://github.com/niklasb/libc-database

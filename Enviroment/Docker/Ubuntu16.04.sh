# update
apt update
apt install zsh git gcc-multilib vim gdb wget git curl zsh python-pip ipython python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential -y
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python ./get-pip.py
/usr/local/bin/pip install --upgrade pwntools
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

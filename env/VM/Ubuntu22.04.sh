sudo passwd
sudo apt update
sudo apt install vim gdb wget git curl nmap zsh python3 pip -y
# install pip & ipython 
sudo apt-get install ipython3 -y
sudo apt-get install gcc-multilib -y
# install pwntools
pip3 install pwntools
# install on-my-zsh   
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# install peda pwngdb
cd 
git clone https://github.com/longld/peda.git ~/peda
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
# install one_gadget
sudo apt install gem ruby ruby-dev -y
sudo gem install one_gadget
sudo gem install seccomp-tools

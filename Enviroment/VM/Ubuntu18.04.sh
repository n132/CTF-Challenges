# Passwd
sudo passwd
# update
sudo apt update
sudo apt install vim gdb wget git curl nmap zsh python-pip -y
# remove useless software
sudo apt remove libreoffice-common thunderbird totem rhythmbox simple-scan gnome-mahjongg aisleriot gnome-mines cheese transmission-common gnome-orca deja-dup
sudo apt autoremove -y
# install pip
sudo apt install python -y
# install ipython
sudo apt-get install ipython -y
# install pwntools
sudo pip install --upgrade pwntools
# install on-my-zsh   
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# sudo apt-get install gcc-multilib
# sudo apt-get install qemu
# install peda pwngdb
cd ~/
git clone https://github.com/longld/peda.git ~/peda
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
# install pwndbg
#git clone https://github.com/pwndbg/pwndbg
#cd pwndbg
#./setup.sh
# install one_gadget
sudo apt install gem ruby ruby-dev -y
sudo gem install one_gadget
sudo gem install seccomp-tools
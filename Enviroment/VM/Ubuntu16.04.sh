# Passwd
sudo passwd
# update
sudo apt update
sudo apt install vim gdb wget git curl nmap zsh python-pip -y
# remove useless software
sudo apt remove libreoffice-common unity-webapps-common thunderbird totem rhythmbox simple-scan gnome-mahjongg aisleriot gnome-mines cheese transmission-common gnome-orca webbrowser-app deja-dup
sudo apt autoremove
# install ipython
sudo apt-get install ipython
# install pwntools
sudo apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
sudo pip install --upgrade pwntools
# install zsh   
sudo apt-get install zsh git gcc-multilib -y
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# sudo apt-get install qemu
# install peda+pwngdb
cd ~/
git clone https://github.com/longld/peda.git ~/peda
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
# install one_gadget
sudo apt install gem ruby ruby-dev -y
sudo gem install one_gadget
sudo gem install seccomp-tools
# install libc-database
#git clone https://github.com/niklasb/libc-database

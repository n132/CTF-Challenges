export DEBIAN_FRONTEND=noninteractive 
export TZ=Etc/UTC
apt-get -y update && apt-get -y install vim gdb wget git curl zsh python3 tmux ipython3  python3-pip gcc-multilib python3-pwntools -y
echo Y | sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
cd && git clone https://github.com/longld/peda.git ~/peda && git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
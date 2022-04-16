# Author: n132
# Download Kernel Templates

from subprocess import Popen, PIPE

exp_address     = "https://raw.githubusercontent.com/n132/CTF-Challenges/main/Cheatsheet/Kernel/exp.c"
boot_address    = "https://raw.githubusercontent.com/n132/CTF-Challenges/main/Cheatsheet/Kernel/boot.sh"
make_address    = "https://raw.githubusercontent.com/n132/CTF-Challenges/main/Cheatsheet/Kernel/Makefile"

def download_templates():
    queue = [exp_address,boot_address,make_address]
    for item in queue:
        Popen(["wget",item],stdout=PIPE, stderr=PIPE)
    print("[*] Got the Templates")
def permission():
    Popen(["chmod","+x","boot.sh"],stdout=PIPE, stderr=PIPE)
if __name__ == "__main__":
    download_templates()
    permission()
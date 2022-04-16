# Author: n132
# Download Kernel Templates

import subprocess

exp_address     = "https://raw.githubusercontent.com/n132/CTF-Challenges/main/Cheatsheet/Kernel/exp.c"
boot_address    = "https://raw.githubusercontent.com/n132/CTF-Challenges/main/Cheatsheet/Kernel/boot.sh"
make_address    = "https://raw.githubusercontent.com/n132/CTF-Challenges/main/Cheatsheet/Kernel/Makefile"

def download_templates():
    queue = [exp_address,boot_address,make_address]
    for item in queue:
        subprocess.Popen(["wget",item])
    print("[*] Got the Templates")

if __name__ == "__main__":
    download_templates()
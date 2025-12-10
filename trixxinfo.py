import platform
import os
import sys
import shutil

# --- Colors ---
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def get_size(bytes, suffix="B"):
    # Converts bytes to GB/MB
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def print_banner():
    clear_screen()
    print(GREEN + BOLD + r"""
  _____     _            ___        __      
 |_   _| __(_)_  ____   |_ _|_ __  / _| ___ 
   | || '__| \ \/ /\ \/ /| || '_ \| |_ / _ \
   | || |  | |>  <  >  < | || | | |  _| (_) |
   |_||_|  |_/_/\_\/_/\_\___|_| |_|_|  \___/ 
    """ + RESET)
    print(YELLOW + "    >>> System & Device Monitor <<<" + RESET)
    print("-" * 45)

def show_info():
    # Gather Info
    uname = platform.uname()
    total, used, free = shutil.disk_usage("/")
    
    print(CYAN + " [ DEVICE INFORMATION ]" + RESET)
    print(f" {BOLD}System:{RESET}    {uname.system}")
    print(f" {BOLD}Node Name:{RESET} {uname.node}")
    print(f" {BOLD}Release:{RESET}   {uname.release}")
    print(f" {BOLD}Version:{RESET}   {uname.version}")
    print(f" {BOLD}Machine:{RESET}   {uname.machine}")
    print(f" {BOLD}Processor:{RESET} {uname.processor}")
    
    print("\n" + CYAN + " [ PYTHON ENVIRONMENT ]" + RESET)
    print(f" {BOLD}Version:{RESET}   {sys.version.split()[0]}")
    print(f" {BOLD}Executable:{RESET} {sys.executable}")

    print("\n" + CYAN + " [ STORAGE STATS ]" + RESET)
    print(f" {BOLD}Total:{RESET}     {get_size(total)}")
    print(f" {BOLD}Used:{RESET}      {get_size(used)} ({RED}{used / total * 100:.1f}%{RESET})")
    print(f" {BOLD}Free:{RESET}      {get_size(free)} ({GREEN}{free / total * 100:.1f}%{RESET})")
    
    print("-" * 45)

def main():
    print_banner()
    show_info()
    input(YELLOW + "Press Enter to exit..." + RESET)

if __name__ == "__main__":
    main()


import socket
import sys
import time
import os

# --- Colors ---
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    print(CYAN + BOLD + r"""
  _____     _           ____            _   
 |_   _| __(_)_  ____  |  _ \ ___  _ __| |_ 
   | || '__| \ \/ /\ \/ / |_) / _ \| '__| __|
   | || |  | |>  <  >  <|  __/ (_) | |  | |_ 
   |_||_|  |_/_/\_\/_/\_\_|   \___/|_|   \__|
    """ + RESET)
    print(YELLOW + "    >>> Target Port Scanner <<<" + RESET)
    print("-" * 45)

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Fast timeout
        result = s.connect_ex((target, port))
        s.close()
        if result == 0:
            return True
        return False
    except:
        return False

def main():
    print_banner()
    target_input = input(BOLD + "Enter Target (IP or Domain): " + RESET)
    
    # Resolve domain to IP
    try:
        target_ip = socket.gethostbyname(target_input)
    except socket.gaierror:
        print(RED + "\n[!] Could not resolve hostname." + RESET)
        sys.exit()

    print(YELLOW + f"\n[*] Scanning Target: {target_ip}" + RESET)
    print(YELLOW + "[*] Please wait..." + RESET)
    print("-" * 45)

    # List of common ports to scan
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP (Web)",
        110: "POP3",
        443: "HTTPS (Web)",
        3306: "MySQL",
        8080: "HTTP Proxy"
    }
    
    open_ports = 0
    
    for port, name in common_ports.items():
        if scan_port(target_ip, port):
            print(GREEN + f"[+] Port {port} ({name}) is OPEN" + RESET)
            open_ports += 1
        else:
            # We don't print closed ports to keep it clean
            pass
            
    print("-" * 45)
    if open_ports == 0:
        print(RED + "No common ports found open." + RESET)
    else:
        print(CYAN + f"Scan Complete. Found {open_ports} open ports." + RESET)

if __name__ == "__main__":
    main()


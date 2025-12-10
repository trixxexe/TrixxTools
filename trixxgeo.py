import sys
import time
import requests
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
    # ASCII Art for TrixxGeo
    print(RED + BOLD + r"""
  _____     _            
 |_   _| __(_)_  ____  __
   | || '__| \ \/ /\ \/ /
   | || |  | |>  <  >  < 
   |_||_|  |_/_/\_\/_/\_\
  ____           
 / ___| ___  ___ 
| |  _ / _ \/ _ \
| |_| |  __/ (_) |
 \____|\___|\___/ 
    """ + RESET)
    print(YELLOW + "    >>> TrixxGeo Intelligence Tool <<<" + RESET)
    print(CYAN + "          System: ONLINE" + RESET)
    print("-" * 45)

def get_ip_data(ip=None):
    # If ip is None, the API returns the user's own IP info
    url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
    
    print(YELLOW + "\n[*] Establishing connection to satellite..." + RESET)
    time.sleep(1)
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # This is where the error was. Ensure the lines below are indented!
        if data['status'] == 'fail':
            print(RED + "\n[!] Could not fetch data: " + data.get('message', 'Unknown Error') + RESET)
            return

        # Formatting Output
        print(GREEN + "\n[+] DATA RETRIEVED SUCCESSFULLY:" + RESET)
        print("-" * 45)
        print(f"{BOLD}Target IP:{RESET}    {data.get('query')}")
        print(f"{BOLD}Country:{RESET}      {data.get('country')} ({data.get('countryCode')})")
        print(f"{BOLD}Region:{RESET}       {data.get('regionName')}")
        print(f"{BOLD}City:{RESET}         {data.get('city')}")
        print(f"{BOLD}ISP:{RESET}          {data.get('isp')}")
        print(f"{BOLD}Coordinates:{RESET}  {data.get('lat')}, {data.get('lon')}")
        print(f"{BOLD}Timezone:{RESET}     {data.get('timezone')}")
        print("-" * 45)

    except Exception as e:
        print(RED + f"\n[!] Connection Error: {e}" + RESET)

def main():
    while True:
        print_banner()
        print("  1. Show MY Public IP & Info")
        print("  2. Lookup a Target IP Address")
        print("  3. Exit")
        print("-" * 45)
        
        choice = input(CYAN + "trixxgeo > " + RESET)

        if choice == '1':
            get_ip_data() # No argument means check my own
            input(YELLOW + "\nPress Enter to continue..." + RESET)

        elif choice == '2':
            target = input(BOLD + "\nEnter Target IP: " + RESET)
            if target.strip() == "":
                print(RED + "IP cannot be empty!" + RESET)
                time.sleep(1)
            else:
                get_ip_data(target)
                input(YELLOW + "\nPress Enter to continue..." + RESET)

        elif choice == '3':
            print(RED + "\nShutting down TrixxGeo..." + RESET)
            break
        else:
            print(RED + "Invalid Selection!" + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main()


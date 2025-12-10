import requests
import os
import sys

# --- Colors ---
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    print(CYAN + BOLD + r"""
  _____     _            __        __   
 |_   _| __(_)_  ____    \ \      / /__ 
   | || '__| \ \/ /\ \/ / \ \ /\ / / _ \
   | || |  | |>  <  >  <   \ V  V /  __/
   |_||_|  |_/_/\_\/_/\_\   \_/\_/ \___|
    """ + RESET)
    print(YELLOW + "    >>> Real-Time Weather Uplink <<<" + RESET)
    print("-" * 45)

def get_weather():
    city = input(BOLD + "Enter City Name (Leave blank for auto): " + RESET)
    
    print(YELLOW + "\n[*] Fetching satellite data..." + RESET)
    
    try:
        # ?0 means current weather only, T means no colors (we handle terminal)
        # Actually wttr.in handles colors beautifully for terminals
        url = f"https://wttr.in/{city}?0"
        response = requests.get(url)
        
        if response.status_code == 200:
            print("\n" + response.text)
        else:
            print(RED + "\n[!] Service Unavailable." + RESET)
            
    except Exception as e:
        print(RED + f"\n[!] Connection Error: {e}" + RESET)

def main():
    while True:
        print_banner()
        get_weather()
        choice = input(CYAN + "Check another city? (y/n): " + RESET)
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()


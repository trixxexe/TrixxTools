import requests
import os
import time

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
  _____     _            _   _      _ 
 |_   _| __(_)_  ____   | | | |_ __| |
   | || '__| \ \/ /\ \/ / | | | '__| |
   | || |  | |>  <  >  <| |_| | |  | |
   |_||_|  |_/_/\_\/_/\_\\___/|_|  |_|
    """ + RESET)
    print(YELLOW + "    >>> Instant Link Shortener <<<" + RESET)
    print("-" * 45)

def shorten_url():
    print(BOLD + "Paste your long URL below:" + RESET)
    long_url = input(GREEN + "> " + RESET)
    
    if not long_url:
        print(RED + "Error: URL cannot be empty!" + RESET)
        return

    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    
    print(YELLOW + "\n[*] Shortening..." + RESET)
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            short_url = response.text
            print(GREEN + "\n[+] SUCCESS! Here is your short link:" + RESET)
            print("-" * 45)
            print(CYAN + BOLD + short_url + RESET)
            print("-" * 45)
        else:
            print(RED + "[!] Failed to shorten. Check the URL." + RESET)
    except Exception as e:
        print(RED + f"[!] Connection Error: {e}" + RESET)

def main():
    while True:
        print_banner()
        shorten_url()
        
        choice = input(YELLOW + "Shorten another? (y/n): " + RESET)
        if choice.lower() != 'y':
            print("Exiting TrixxUrl...")
            break

if __name__ == "__main__":
    main()


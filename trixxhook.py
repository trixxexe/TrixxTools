import requests
import time
import os
import sys

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
    print(RED + BOLD + r"""
  _____     _            _   _             _    
 |_   _| __(_)_  ____   | | | | ___   ___ | | __
   | || '__| \ \/ /\ \/ / |_| |/ _ \ / _ \| |/ /
   | || |  | |>  <  >  <|  _  | (_) | (_) |   < 
   |_||_|  |_/_/\_\/_/\_\_| |_|\___/ \___/|_|\_\
    """ + RESET)
    print(YELLOW + "    >>> Discord Webhook Messenger <<<" + RESET)
    print("-" * 45)

def send_message():
    url = input(CYAN + "Enter Webhook URL: " + RESET)
    
    # Basic validation
    if "discord" not in url:
        print(RED + "\n[!] That doesn't look like a Discord URL." + RESET)
        return

    print(GREEN + "\n(Type 'exit' to quit messaging)" + RESET)
    
    while True:
        msg = input(BOLD + "\nMessage > " + RESET)
        
        if msg.lower() == 'exit':
            break
        if msg.strip() == "":
            continue
            
        data = {
            "content": msg,
            "username": "TrixxBot"
        }
        
        try:
            result = requests.post(url, json=data)
            if 200 <= result.status_code < 300:
                print(GREEN + " [Sent]" + RESET)
            else:
                print(RED + f" [Failed: {result.status_code}]" + RESET)
        except Exception as e:
            print(RED + f" [Error: {e}]" + RESET)

def main():
    print_banner()
    print(YELLOW + "WARNING: Do not spam. You can get API banned." + RESET)
    print("-" * 45)
    send_message()

if __name__ == "__main__":
    main()


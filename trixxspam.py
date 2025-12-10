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
    print(RED + BOLD + r"""
  _____     _            ____                        
 |_   _| __(_)_  ____   / ___| _ __   __ _ _ __ ___  
   | || '__| \ \/ /\ \/ \___ \| '_ \ / _` | '_ ` _ \ 
   | || |  | |>  <  >  < ___) | |_) | (_| | | | | | |
   |_||_|  |_/_/\_\/_/\_\____/| .__/ \__,_|_| |_| |_|
                              |_|                    
    """ + RESET)
    print(YELLOW + "    >>> Mass Text Multiplier <<<" + RESET)
    print("-" * 45)

def generate_spam():
    message = input(BOLD + "Enter message to repeat: " + RESET)
    if not message:
        print(RED + "Message cannot be empty!" + RESET)
        return

    try:
        count = int(input(BOLD + "How many times? (e.g. 100): " + RESET))
    except ValueError:
        print(RED + "Enter a valid number!" + RESET)
        return

    # Create the spam
    # Adding a space or newline between repetitions?
    sep = input(BOLD + "Separate by Newline? (y/n): " + RESET).lower()
    separator = "\n" if sep == 'y' else " "
    
    final_text = (message + separator) * count
    
    print(YELLOW + "\n[*] Generating..." + RESET)
    time.sleep(1)
    
    # Save to file option
    save = input(CYAN + "Save to file for easy copying? (y/n): " + RESET).lower()
    
    if save == 'y':
        with open("spam.txt", "w") as f:
            f.write(final_text)
        print(GREEN + f"\n[+] Saved to 'spam.txt'! Open it to copy." + RESET)
    else:
        print("-" * 45)
        print(final_text)
        print("-" * 45)
        print(GREEN + "[+] Done." + RESET)

def main():
    print_banner()
    generate_spam()

if __name__ == "__main__":
    main()


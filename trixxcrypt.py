import base64
import os
import sys
import time
import random
import string

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
    print(GREEN + BOLD + r"""
  _______   _           ____                  _ 
 |__   __| (_)         / ___|  _ __  _   _  | |_ 
    | | ___| |____  __| |     | '__|| | | | | __|
    | |/ _ \ |\ \/ / \ \/ /   | |   | |_| | | |_ 
    |_|\___/_|/_/\_\/_/\_\    |_|    \__, |  \__|
                                     |___/       
    """ + RESET)
    print(YELLOW + "    >>> Secure Message Encrypter <<<" + RESET)
    print("-" * 45)

def encrypt_text():
    print(CYAN + "\n--- ENCRYPTION MODE ---" + RESET)
    text = input(BOLD + "Enter message to hide: " + RESET)
    if not text:
        print(RED + "Input cannot be empty!" + RESET)
        return
    
    # Encode to bytes, then base64, then back to string
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    encoded_str = encoded_bytes.decode("utf-8")
    
    print("\n" + GREEN + "SUCCESS! Here is your secret code:" + RESET)
    print(YELLOW + "-" * 45)
    print(encoded_str)
    print("-" * 45 + RESET)
    print("(Copy the code above and send it to your friend)")

def decrypt_text():
    print(CYAN + "\n--- DECRYPTION MODE ---" + RESET)
    code = input(BOLD + "Paste the secret code here: " + RESET)
    if not code:
        print(RED + "Input cannot be empty!" + RESET)
        return
        
    try:
        # Decode bytes back to string
        decoded_bytes = base64.b64decode(code)
        decoded_str = decoded_bytes.decode("utf-8")
        
        print("\n" + GREEN + "SUCCESS! The hidden message is:" + RESET)
        print(YELLOW + "-" * 45)
        print(decoded_str)
        print("-" * 45 + RESET)
    except:
        print(RED + "\n[!] Invalid Code! Could not decrypt." + RESET)

def generate_password():
    print(CYAN + "\n--- PASSWORD GENERATOR ---" + RESET)
    try:
        length = int(input("Enter password length (e.g., 12): "))
    except ValueError:
        print(RED + "Please enter a number!" + RESET)
        return

    # Combine letters, digits, and symbols
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(length))
    
    print("\n" + GREEN + "Your Strong Password:" + RESET)
    print(YELLOW + password + RESET)

def main():
    while True:
        print_banner()
        print("  1. Encrypt Message (Hide)")
        print("  2. Decrypt Message (Read)")
        print("  3. Generate Strong Password")
        print("  4. Exit")
        print("-" * 45)
        
        choice = input(CYAN + "trixxcrypt > " + RESET)

        if choice == '1':
            encrypt_text()
            input(YELLOW + "\nPress Enter to continue..." + RESET)
        elif choice == '2':
            decrypt_text()
            input(YELLOW + "\nPress Enter to continue..." + RESET)
        elif choice == '3':
            generate_password()
            input(YELLOW + "\nPress Enter to continue..." + RESET)
        elif choice == '4':
            print(RED + "\nExiting..." + RESET)
            break
        else:
            print(RED + "Invalid Option!" + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main()


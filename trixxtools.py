import os
import sys
import time

# --- Colors for the interface ---
R = '\033[31m' # Red
G = '\033[32m' # Green
C = '\033[36m' # Cyan
W = '\033[0m'  # White (Reset)

def clear_screen():
    os.system('clear')

def banner():
    clear_screen()
    print(f"{C}")
    print(r"""
  _______   _            _______          _     
 |__   __| | |          |__   __|        | |    
    | |_ __| |___  ____    | | ___   ___ | |___ 
    | | '__| / \ \/ /\ \   | |/ _ \ / _ \| / __|
    | | |  | |>  >  <  >  <| | (_) | (_) | \__ \
    |_|_|  |_/_/\_/\_\/_/\_\_|\___/ \___/|_|___/
    """)
    print(f"{G}       [ TrixxTools Framework v1.0 ]{W}")
    print(f"{R}       [ Created by Trixx ]{W}\n")

def run_tool(filename):
    """Executes the python script and waits before returning"""
    if os.path.exists(filename):
        print(f"\n{G}[*] Starting {filename}...{W}\n")
        os.system(f"python {filename}")
        print(f"\n{C}[*] Execution finished.{W}")
        input(f"{G}Press Enter to return to menu...{W}")
    else:
        print(f"\n{R}[!] Error: File {filename} not found!{W}")
        time.sleep(2)

def show_menu():
    while True:
        banner()
        print(f"{C}[1]{W} Calculator      {C}[6]{W} Port Scanner (trixxport)")
        print(f"{C}[2]{W} Encryption Tool {C}[7]{W} SMS/Spam Tool (trixxspam)")
        print(f"{C}[3]{W} Geo Locator     {C}[8]{W} URL Shortener (trixxurl)")
        print(f"{C}[4]{W} Web Hooker      {C}[9]{W} Weather Info (trixxweather)")
        print(f"{C}[5]{W} System Info     {C}[0]{W} EXIT")
        print("-" * 50)
        
        try:
            choice = input(f"{G}trixx > {W}")
            
            if choice == '1':
                run_tool('calculator.py')
            elif choice == '2':
                run_tool('trixxcrypt.py')
            elif choice == '3':
                run_tool('trixxgeo.py')
            elif choice == '4':
                run_tool('trixxhook.py')
            elif choice == '5':
                run_tool('trixxinfo.py')
            elif choice == '6':
                run_tool('trixxport.py')
            elif choice == '7':
                run_tool('trixxspam.py')
            elif choice == '8':
                run_tool('trixxurl.py')
            elif choice == '9':
                run_tool('trixxweather.py')
            elif choice == '0':
                print(f"\n{R}Exiting TrixxTools...{W}")
                sys.exit()
            else:
                print(f"\n{R}Invalid selection!{W}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n{R}Exiting...{W}")
            sys.exit()

if __name__ == "__main__":
    show_menu()

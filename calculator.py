import os
import time

# --- Colors for Termux ---
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    # Fixed ASCII Art: Stacked to fit phone screens
    print(CYAN + BOLD + r"""
  ____  _ _                   
 |  _ \(_) |_ __ _ _ __ ___   
 | |_) | | __/ _` | '_ ` _ \  
 |  _ <| | || (_| | | | | | | 
 |_| \_\_|\__\__,_|_| |_| |_| 
   ____      _       _            
  / ___|   _| | __ _| |_ ___  _ __ 
 | |  | | | | |/ _` | __/ _ \| '__|
 | |__| |_| | | (_| | || (_) | |   
  \____\__,_|_|\__,_|\__\___/|_|   
    """ + RESET)
    print(YELLOW + "   >>> The Ultimate Termux Calculator <<<" + RESET)
    print("-" * 45)

def get_ordinal(n):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def get_numbers():
    numbers = []
    count = 1
    print(GREEN + "\nEnter numbers one by one." + RESET)
    print(YELLOW + "Leave blank and press Enter to finish." + RESET)
    
    while True:
        ordinal = get_ordinal(count)
        
        # Determine prompt message
        if count <= 2:
            prompt_text = f"{ordinal} number : "
        else:
            prompt_text = f"{ordinal} number (optional) : "
            
        user_input = input(BOLD + prompt_text + RESET)

        # Logic to stop input
        if user_input.strip() == "":
            if count <= 2:
                print(RED + "  [!] You need at least 2 numbers!" + RESET)
                continue
            else:
                break
        
        try:
            num = float(user_input)
            numbers.append(num)
            count += 1
        except ValueError:
            print(RED + "  [!] Please enter a valid number." + RESET)
            
    return numbers

def main():
    while True:
        print_banner()
        print("  1. Addition (+)")
        print("  2. Subtraction (-)")
        print("  3. Multiplication (×)")
        print("  4. Division (÷)")
        print("  5. Exit")
        print("-" * 45)
        
        choice = input(CYAN + "What is your operation : " + RESET)

        if choice == '5':
            print("Exiting RitamCulator...")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print(RED + "Invalid Option!" + RESET)
            time.sleep(1)
            continue

        # Get inputs
        nums = get_numbers()
        result = 0

        # Calculate
        if choice == '1': # Addition
            result = sum(nums)
            
        elif choice == '2': # Subtraction
            result = nums[0]
            for n in nums[1:]:
                result -= n
            
        elif choice == '3': # Multiplication
            result = 1
            for n in nums:
                result *= n
            
        elif choice == '4': # Division
            result = nums[0]
            try:
                for n in nums[1:]:
                    if n == 0:
                        print(RED + "  [!] Error: Cannot divide by Zero!" + RESET)
                        result = "Undefined"
                        break
                    result /= n
            except:
                result = "Error"

        # Output Result
        print("-" * 45)
        if isinstance(result, float) and result.is_integer():
            result = int(result) # Make it look clean (5.0 -> 5)
            
        print(GREEN + BOLD + f"  RESULT: {result}" + RESET)
        print("-" * 45)
        
        input("Press Enter to calculate again...")

if __name__ == "__main__":
    main()


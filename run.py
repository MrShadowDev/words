import string
import itertools
import os
from tqdm import tqdm
from colorama import init, Fore, Style

init()
os.system('cls' if os.name == 'nt' else 'clear')

BANNER = [f"""

    ██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗
    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗╚══███╔╝
    ██║ █╗ ██║██║   ██║██████╔╝██║  ██║  ███╔╝ 
    ██║███╗██║██║   ██║██╔══██╗██║  ██║ ███╔╝  
    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗
     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
                                                                                                                          
                           Made by MrSh4dow :)
"""]

def generate_combinations(length, alphabet=string.ascii_lowercase):
    return itertools.product(alphabet, repeat=length)

def display_progress(combinations, length, output_file=None):
    total_combinations = len(string.ascii_lowercase) ** length
    progress_bar = tqdm(total=total_combinations, unit=" combinations", 
                         desc=f"{Fore.CYAN}Generating {length}-.....{Style.RESET_ALL}")
    
    if output_file:
        with open(output_file, 'w') as f:
            for combo in combinations:
                f.write(''.join(combo) + '\n')
                progress_bar.update(1)
        progress_bar.close()
        print(f"{Fore.GREEN}\nCombinations written to {output_file}{Style.RESET_ALL}")
    else:
        for combo in combinations:
            print(''.join(combo))
            progress_bar.update(1)
        progress_bar.close()
        print(f"{Fore.MAGENTA}\Complete!{Style.RESET_ALL}")

def main():
    print(*BANNER, sep='\n')
    length = int(input(f"{Fore.YELLOW}Enter the length for words: {Style.RESET_ALL}"))
    alphabet = string.ascii_lowercase
    save_to_file = input(f"{Fore.YELLOW}Do you want to save to a file? (yes/no): {Style.RESET_ALL}").lower()
    
    if save_to_file == "yes":
        output_filename = input(f"{Fore.YELLOW}Enter the output filename: {Style.RESET_ALL}")
        if not output_filename.endswith('.txt'):
            output_filename += 'output.txt'
    else:
        output_filename = None
    
    print(f"\n{Fore.CYAN}Generating {length}-...{Style.RESET_ALL}")
    combinations = generate_combinations(length, alphabet)
    display_progress(combinations, length, output_file=output_filename)

if __name__ == "__main__":
    main()
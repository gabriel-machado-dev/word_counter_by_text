from rich.console import Console
from rich.table import Table
from time import sleep
import os
import re

# Colors
DEFAULT = '\033[0m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
YELLOW = '\033[3m\033[1;33m'
YELLOW2 = '\033[1;93m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
BOLD = '\033[1m'
BLINK = '\033[5m'

def print_title():
    print('''

       {5} ░█░█░█▀█░█▀▄░█▀▄░░░█▀▀░█▀█░█░█░█▀█░▀█▀░█▀▀░█▀▄{0}
       {6} ░█▄█░█░█░█▀▄░█░█░░░█░░░█░█░█░█░█░█░░█░░█▀▀░█▀▄{0}
       {7} ░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀{0}
       
         {6})    /\__/\ 
         {6}( = (˶ᵔ ᵕ ᵔ˶)
         {1}-------{6}U{1}-{6}U{1}----------------
         {1}|                        |       |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
         {1}|  {3}Code Author: {2}Gabriel Machado  {0}{1}|       {3}GitHub: {2}https://github.com/gabriel-machado-dev{0}
         {1}|      {3}Version: {2}1.0      {0}{1}|             
         {1}|                        |       |_____________________________________________|
         {1}--------------------------                        {6}\ (˶ᵔ ᵕ ᵔ˶) /{0}
                                                            {6}\         /{0}

        '''.format(DEFAULT, GREEN, RED,YELLOW2
                   ,YELLOW, BLINK, MAGENTA, CYAN))

def instructions():
    print(f'{YELLOW2}{BOLD}Instructions: {DEFAULT}')
    print(f'{YELLOW2}{BOLD}1. Enter a text with more than 5 words{DEFAULT}')
    print('\n')

def get_text():
    while True:
        text = input(f'{BLINK}{BOLD}Enter a text: {DEFAULT}')
        print('\n')
        if len(text.split()) > 5:
            return text.strip()
        print(f'{RED}{BOLD}Invalid input: Please enter a non-empty text{DEFAULT}\n')

def count_words(text):
    
    # Remove caracteres especiais e converte para minúsculas
    words = [word.lower().strip(",.!?;:@#$%^&*()[{/}\]}") for word in text.split()]
    word_count = {word: words.count(word) for word in set(words) if len(word) > 2}

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1])

    table = Table(title='Most Frequent Words', show_lines=True, row_styles=['dim', 'none'])
    table.add_column('Word', justify='center', style='cyan', no_wrap=True)
    table.add_column('Frequency', justify='center', style='magenta', no_wrap=True)

    for word, count in sorted_word_count:
        table.add_row(f'{word}', f'{count}')

    console = Console()
    console.print(table)
    print('\n')
    print(f'{CYAN}{BOLD}The most frequent word is "{sorted_word_count[-1][0]}" which appears {sorted_word_count[-1][1]} times{DEFAULT}')

if __name__ == '__main__':
    print_title()
    instructions()
    count_words(get_text())
    while True:
        run_again = input('Do you want to run the program again? (yes/no): ')
        if run_again.lower().strip() in ['yes', 'no']:
            if run_again.lower().strip() == 'no':
                print(f'{YELLOW}{BOLD}Thank you for using the program!{DEFAULT}')
                sleep(2)
                break
            else:
                os.system('clear' if os.name == 'posix' else 'cls')
                print_title()
                instructions()
                count_words(get_text())
        else:
            print(f'{RED}{BOLD}Invalid input: Please enter either "yes" or "no"{DEFAULT}\n')


from rich.console import Console
from rich.table import Table
from time import sleep
import os

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_title():
    print(CYAN + BOLD + r'''

        ░█░█░█▀█░█▀▄░█▀▄░░░█▀▀░█▀█░█░█░█▀█░▀█▀░█▀▀░█▀▄
        ░█▄█░█░█░█▀▄░█░█░░░█░░░█░█░█░█░█░█░░█░░█▀▀░█▀▄
        ░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀

        ''' + RESET)

def instructions():
    print(f'{YELLOW}{BOLD}Instructions: {RESET}')
    print(f'{YELLOW}1. Enter a text with more than 10 words{RESET}')
    print(f'{YELLOW}2. The text cannot contain numbers{RESET}')
    print('\n')

def get_text():
    while True:
        text = input('Enter a text: ')
        print('\n')
        if len(text.split()) >= 10 and not any(char.isdigit() for char in text) and text.strip():
            return text
        print(f'{RED}{BOLD}Invalid input: Please enter a non-empty text without numbers{RESET}\n')

def count_words(text):
    words = [word.lower().strip(",.!?;:") for word in text.split()]
    word_count = {word: words.count(word) for word in set(words)}

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    table = Table(title='Most Frequent Words', show_lines=True, row_styles=['dim', 'none'])
    table.add_column('Word', justify='center', style='cyan', no_wrap=True)
    table.add_column('Frequency', justify='center', style='magenta', no_wrap=True)

    for word, count in sorted_word_count:
        table.add_row(f'{word}', f'{count}')

    console = Console()
    console.print(table)
    print('\n')
    print(f'{CYAN}{BOLD}The most frequent word is "{sorted_word_count[0][0]}" which appears {sorted_word_count[0][1]} times{RESET}')

if __name__ == '__main__':
    print_title()
    instructions()
    count_words(get_text())
    while True:
        run_again = input('Do you want to run the program again? (yes/no): ')
        if run_again.lower().strip() in ['yes', 'no']:
            if run_again.lower().strip() == 'no':
                print(f'{YELLOW}{BOLD}Thank you for using the program!{RESET}')
                sleep(2)
                break
            else:
                os.system('clear' if os.name == 'posix' else 'cls')
                print_title()
                instructions()
                count_words(get_text())
        else:
            print(f'{RED}{BOLD}Invalid input: Please enter either "yes" or "no"{RESET}\n')


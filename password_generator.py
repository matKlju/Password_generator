"""

A random password generator

Using Numbers, Upper and Lowercase letters, and symbols.

"""

from random import choice as rnd
import string
import sys

TIP = """
Using Numbers, Upper and Lowercase letters, and symbols.

Password length      Password strength
    4  - 6               very weak
    7  - 10                weak
    11 - 12               normal
    13 - 15               strong
    16 - 18             very strong"""


def get_choice() -> int:
    """Check and return value"""

    while True:
        try:
            choice = int(input('\n1. New password\n2. Quit\n\t> '))
            if choice > 2 or choice < 1:
                print('\nOut of range!')
                continue

            return choice

        except ValueError:
            print('\nOnly integers!')


def get_length() -> int:
    """Check type and return length"""

    while True:
        try:
            choice = int(input('\nHow long should the password be?\n\t> '))
            return choice

        except ValueError:
            print('Only integers')


def generate_password(length: int) -> str:
    """Generate password, by length, from ASCII printable collection"""

    return ''.join(rnd(string.printable[:-6]) for i in range(length))


def main_menu():
    """Start main loop and prompt user for action"""

    print(f'{TIP}')

    while True:
        choice = get_choice()

        if choice == 2:
            print('\nBye!')
            sys.exit()

        if choice == 1:
            print(f'\nLet’s generate a random password!'
                  f'\n\nYour password is: {generate_password(get_length())}')


if __name__ == '__main__':
    main_menu()

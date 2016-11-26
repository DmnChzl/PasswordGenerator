# -*- coding: utf-8 -*-
'''
Copyright (C) 2016 Damien Chazoule

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import re
import sys

from random import *

OUTPUT = False
LENGTH = 0
PATTERN = "{P8}"

letters = 'abcdefghijklmnopqrstuvwxyz'
consonants = 'bcdfghjklmnpqrstvwxz'
vowels = 'aeiouy'
numbers = '0123456789'
symbols = '!@#$%^&*_=+-/.?<>)'
chars = letters + letters.upper() + numbers + symbols

def output_password(password):
    if OUTPUT:
        try:
            os.remove("password.txt")
        except OSError:
            pass

        with open("password.txt", "a") as text:
            text.write("{}\n".format(password))

def convert_key(key, last):
    if key.lower() == "l":
        return letters
    elif key.lower() == "c":
        return consonants
    elif key.lower() == "v":
        return vowels
    elif key.lower() == "n":
        return numbers
    elif key.lower() == "s":
        return symbols
    elif key.lower() == "w":
        if last.lower() in consonants:
            return vowels
        elif last.lower() in vowels:
            return consonants
        else:
            return letters
    else:
        return chars

def build_password(key, last):
    index = randrange(len(convert_key(key, last)))
    char = convert_key(key, last)[index]
    if key.isupper():
        return char.upper()
    else:
        return char

def custom_generator():
    size = LENGTH
    if LENGTH == 0:
        size = randint(8, 16)

    values = re.findall('\{(.*?)\}', PATTERN)

    template = ""
    for x in range(len(values)):
        try:
            template += values[x][0] * int(values[x][1:])
            size -= int(values[x][1:])
        except ValueError:
            template += values[x][0] * size

    password = ""
    for y in range(0, len(template)):
        try:
            password += build_password(template[y], password[y-1])
        except IndexError:
            password += build_password(template[y], letters[randrange(len(letters))])

    if len(password) < LENGTH:
        for z in range(len(password), LENGTH):
            password += chars[randrange(len(chars))]

    print("Your custom password is : '{}'".format(password))
    output_password(password)

def classic_generator():
    size = LENGTH
    if LENGTH == 0:
        size = randint(8, 16)

    password = "".join(choice(chars) for x in range(size))
    print("Your password is : '{}'".format(password))
    output_password(password)

def identify_arg(arg):
    global OUTPUT
    global LENGTH
    global PATTERN

    values = arg.split("=")
    if len(values) == 1:
        if values[0] in ["-o", "--output"]:
            OUTPUT = True
        else:
            print("Unknown option : '{}'".format(values[0]))
            sys.exit(1)
    elif len(values) == 2:
        if values[0] in ["-l", "--length"]:
            LENGTH = int(values[1])
        elif values[0] in ["-p", "--pattern"]:
            PATTERN = values[1]
        else:
            print("Unknown option : '{}'".format(values[0]))
            sys.exit(1)
    else:
        print("Unknown option : '{}'".format(values[0]))
        sys.exit(1)

def use_assistant():
    global LENGTH
    global PATTERN

    LENGTH = int(input("What length of password do you want : "))
    if LENGTH == 0:
        LENGTH = int(input("Invalid length of password ! Try again : "))

    val = input("Would you specify the pattern (y/N) ? ")
    if val.lower() in ["y", "yes"]:
        PATTERN = input("Specify the pattern : ")
        custom_generator()
    else:
        classic_generator()

def show_help():
    print('''Usage : password_generator.py [option] ...
Options available :
-a : use the assistant (also --ask)
-h : print this help message (also --help)
-l : modify default value of the length, use it like this '-l=[value]' (also --length)
-o : save password generated in .txt file (also --output)
-p : modify default value of the pattern, use it like this : '-p=[value]' (also --pattern)
''')

if __name__ == "__main__":
    args = list(sys.argv)
    args.remove("password_generator.py")
    if len(args) > 0:
        if "-h" in args:
            show_help()
        elif "--help" in args:
            show_help()
        elif "-a" in args:
            use_assistant()
        elif "--ask" in args:
            use_assistant()
        else:
            for x in range(0, len(args)):
                identify_arg(args[x])

            custom_generator()
    else:
        classic_generator()

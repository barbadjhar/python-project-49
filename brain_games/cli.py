#!/usr/bin/env python3

import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    # print("Hello, " + name + "!")             # первый вариант простой 
    print(f"Hello, {name}!")                    # второй вариант через f
    return name

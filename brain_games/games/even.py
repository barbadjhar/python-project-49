#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_parity(number):
    return "yes" if number % 2 == 0 else "no"


def assembling_game():
    number = randint(0, 99)
    question = f'{number}'

    correct_answer = check_parity(number)

    return question, correct_answer

#!/usr/bin/env python3

from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generating_value(min=1, max=100):
    operand_1 = randint(min, max)
    operand_2 = randint(min, max)
    return operand_1, operand_2


def calculate_exact(a, b):
    return gcd(a, b)


def assembling_game():
    operand_1, operand_2 = generating_value()
    question = f'{operand_1} {operand_2}'

    correct_answer = calculate_exact(operand_1, operand_2)

    return question, correct_answer

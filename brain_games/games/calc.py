#!/usr/bin/env python3

from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def generating_value(min=1, max=100):
    operand_1 = randint(min, max)
    operand_2 = randint(min, max)
    return operand_1, operand_2


def generating_symbol():
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    return operation, operator


def calculate_exact(a, b, operator):
    return operator(a, b)


def assembling_game():
    operand_1, operand_2 = generating_value()
    operation, operator = generating_symbol()
    question = f'{operand_1} {operator} {operand_2}'

    correct_answer = calculate_exact(operand_1, operand_2, operation)

    return question, correct_answer


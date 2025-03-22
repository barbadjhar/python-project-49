
from math import sqrt
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

ROUND_START = 1
ROUND_END = 100


def check_simple_number(num):
    if num == 2:
        return "yes"
    if num <= 1 or num % 2 == 0:
        return "no"
    for i in range(3, int(sqrt(num)), 2):
        if num % i == 0:
            return "no"
    return "yes"


def get_question_and_answer():
    number = randint(ROUND_START, ROUND_END)
    question = f'{number}'

    correct_answer = str(check_simple_number(number))

    return question, correct_answer

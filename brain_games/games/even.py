
from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

ROUND_START, ROUND_END = 0, 99


def check_parity(number):
    return True if number % 2 == 0 else False


def get_question_and_answer():
    number = randint(ROUND_START, ROUND_END)
    question = f'{number}'

    if check_parity(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer

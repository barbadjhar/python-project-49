#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'What number is missing in the progression?'
LENGHT_MAX = 10             # длина прогресси большая 
LENGHT_MIN = 5             # длина прогресси малая 


def generation_progression(start, step, length=10):          
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression
    

def assembling_game():
    length = randint(LENGHT_MIN, LENGHT_MAX)      
    start = randint(1, 100)                         
    step = randint(1, 20)                    
    
    correct_progress = generation_progression(start, step, length)  

    shadow = randint(0, len(correct_progress) - 1)                        

    shadow_progress = [*correct_progress]               
    shadow_progress[shadow] = '..'                     
    shadow_progress = ' '.join(map(str, shadow_progress))

    question = f'{shadow_progress}'
    correct_answer = correct_progress[shadow]   
    return question, correct_answer


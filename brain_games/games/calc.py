#!/usr/bin/env python


from brain_games.games import logic
import random

MIN_NUMBER = 1
MAX_NUMBER = 100
BEGIN_STRING = 'What is the result of the expression?'


def calc_start():
    user_name = logic.welcome_user()
    print(BEGIN_STRING)
    for i in range(3):
        number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        sign = random.choice('+-*')
        text_question = f'{number1} {sign} {number2}'
        correct_answer = str(eval(f'{number1}{sign}{number2}'))

        if not logic.game_step(text_question, correct_answer):
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!!!')

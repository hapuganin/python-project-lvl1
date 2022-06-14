#!/usr/bin/env python


from brain_games.games import logic
import random
import math

MIN_NUMBER = 1
MAX_NUMBER = 100
BEGIN_STRING = 'Find the greatest common divisor of given numbers.'


def gcd_start():
    user_name = logic.welcome_user()
    print(BEGIN_STRING)
    for i in range(3):
        number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        text_question = f'{number1} {number2}'
        correct_answer = str(math.gcd(number1, number2))

        if not logic.game_step(text_question, correct_answer):
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!!!')

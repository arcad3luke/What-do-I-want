import random
import time as t
import sys

def choose():
    question = input('What are your options? (Please enter comma separated):\n').split(',')
    choice = random.choice(question)
    print(choice)
    t.sleep(5)
    return question

choices = choose()


while choices is not None:
    rerun = input('Do you want to try again? (y/n) ')
    if rerun.upper() != 'N':
        keep_choices = input('Do you want to use the same choices? (y/n) ')
        if keep_choices.upper() == 'Y':
            choice = random.choice(choices)
            print(choice)
            t.sleep(5)
        elif keep_choices.upper() == 'N':
            choices = choose()
    else:
        print('Have a good one then!')
        sys.exit()


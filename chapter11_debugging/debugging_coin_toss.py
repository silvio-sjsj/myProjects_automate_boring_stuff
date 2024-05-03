#! python3
"""
The following program is meant to be a simple coin toss guessing game. The
player gets two guesses (it's an easy game). However, the program has several
bugs in it. Run through the program a few times to find the bugs that keep
the program from working correctly.
"""

""" Bugs we can find:
- The original code is not able to tell the difference between HEADS and heads
(and any other difference between using lower and upper cases in heads or tails)
- the input from the user and the result of the toss in the line `if toss == guess`
will never evaluate to True because there is nothing that converts the result 1 or 0
from the `random.randint(0,1)` to the string 'heads/tails'
- even if there were something converting the number 0 or 1 to heads or tails, in the
second `guess = input()` there is nothing checking if the input is heads or tails, thus
since it can be anything like 'heads', 'tails' or 'umbreon is the best pokémon' so there
can be any input to the program.   
"""

import random 
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
 
guess = ''

print("Flipping the coin...")

toss = random.randint(0, 1) # 0 is tails, 1 is heads

logging.debug('The toss is: ' + str(toss))

while guess.lower() not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess.lower() not in ('tails', 'heads'):
        raise Exception('You must guess "heads" or "tails".')
    logging.debug('The user\'s guess is: ' + guess)

if toss == 1:
    toss = 'heads'
else:
    toss = 'tails'

if toss == guess:
    print("You got it right!")
else:
    print("Nope! Try again!")
    guess = input()
    if guess.lower() not in ('tails', 'heads'):
        raise Exception('You must guess "heads" or "tails".')
    logging.debug('The user\'s guess is: ' + guess)
    if toss == guess:
        print("Now, you got it!")
    else:
        print("Nope. C'mon! You are really bad at this game.\
              You have two guesses from two options.......")

logging.debug('End of program')
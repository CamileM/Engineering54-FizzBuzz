
import time

from fizz_buzz_functions import *

numb = ''

while numb != 'pineapple':

    numb = int(input('Please enter a number: '))

    for current_numb in range(1, numb):
        print(play_fizz_buzz(current_numb))
        time.sleep(1)

        if numb == 'pineapple':
            break

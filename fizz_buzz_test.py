
from fizz_buzz_functions import *

# ===== TEST FUNCTION ONE ====

# Check to see if number is divisible by mod
# is_divisible_by should return True if number is divisible by mod
#                 should return False if number is not divisible by mod

# function(user input) ---> expected results
# is_divisible_by(9, 3) ---> True

print(is_divisible_by(9, 3) == True) # True
# def is_divisible_by(9, 3):
#         return (9 % 3) == 0
#         return (  0  ) == 0
#         return   true
#
#
print(is_divisible_by(10, 3) == False) # True
# def is_divisible_by(10, 3):
#         return (10 % 3) == 0
#         return (  1  ) == 0
#         return   false


# ===== TEST FUNCTION TWO ====

# if I call play_fizz_buzz with the number 4
# it should return 4
print(play_fizz_buzz(4) == 4) # True

# def play_fizz_buzz(numb):
#
#     if is_divisible_by(numb, 3) and is_divisible_by(numb, 5):
#         return('FizzBuzz')
#
#     elif is_divisible_by(numb, 3):
#         return('Fizz')
#
#     elif is_divisible_by(numb, 5):
#         return('Buzz')
#
#     else:
#         return(numb)


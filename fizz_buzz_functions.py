

# def is_fizz(numb):
#     return numb % 3 == 0

# def is_buzz(numb):
#     return numb % 5 == 0

def is_divisible_by(numb, mode):
    return numb % mode == 0


def play_fizz_buzz(numb):

    if is_divisible_by(numb, 3) and is_divisible_by(numb, 5):
        return('FizzBuzz')

    elif is_divisible_by(numb, 3):
        return('Fizz')

    elif is_divisible_by(numb, 5):
        return('Buzz')

    else:
        return(numb)


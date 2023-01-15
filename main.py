# Python version of the HigherLower game.
import random


# Generate number between 1 and 20 to use in game
def generate_num():
    return random.randint(1, 20)


if __name__ == '__main__':
    guess = ""

    # generate first number to show user
    first_num = generate_num()

    # get guess from the user
    while True:
        guess = input('Number is ' + str(first_num) + '. Will the next be "higher" or "lower"? (between 1-20):')

        # only accept guess if it is a valid guess
        if guess.casefold() == 'higher' or guess.casefold() == 'lower':
            break
        # only accept guess if it is an integer
        print('Invalid response, please enter either "higher" or "lower"')

    second_num = generate_num()
    print('The first number is ' + str(first_num) + ' and the second number is ' + str(second_num))

    # Results logic
    if first_num > second_num and guess.casefold() == 'lower':
        print('You were correct!')
    elif first_num < second_num and guess.casefold() == 'higher':
        print('You were correct!')
    else:
        print("Sorry, but you were incorrect")

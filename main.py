# Python version of the HigherLower game.
import random


# Generate number between 1 and 20 to use in game
def generate_num():
    return random.randint(1, 20)


if __name__ == '__main__':
    # generate first number to show user
    first_num = generate_num()

    # get guess from the user
    while True:
        try:
            guess = input('Number is ' + str(first_num) + '. Will the next be "higher" or "lower"? (between 1-20):')

            # only accept guess if it a valid guess
            if guess.lower() == 'higher' or guess.lower() == 'lower':
                break
        # only accept guess if it is an integer
        except ValueError:
            print('Invalid response, please enter either "higher" or "lower"')

        second_num = generate_num()



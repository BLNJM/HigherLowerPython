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
            guess = int(input('The first number is ' + str(first_num) + '. Please enter a number between 1-20: '))

            # only accept guess if it is within accepted range
            if guess in range(1, 21):
                print("Your choice was: ", guess)
                break
        # only accept guess if it is an integer
        except ValueError:
            print('Invalid response, please enter a number between 1-20')

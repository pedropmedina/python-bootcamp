from random import randint

random_num = randint(1, 10)
guess = input('Guess a number from 1 to 10: ')

while True:
    guess = input('Guess a number from 1 to 10: ')
    guess_int = int(guess)

    if guess_int == random_num:
        print(f'You guessed the corrent number ({guess_int})')
        play_again = input('Want to play again (y/n): ')

        if play_again == 'n':
            break
        elif play_again == 'y':
            random_num = randint(1, 10)
    elif guess_int > random_num:
        print('You gussing too high!')
    elif guess_int < random_num:
        print('You guessing too low!')
    else:
        guess = input('Guess again a number from 1 to 10: ')

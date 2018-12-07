from random import randint

HANGMAN_PICS = [
    r"""
    +---+
        |
        |
        |
       ===
    """,
    r"""
    +---+
    O   |
        |
        |
       ===
    """,
    r"""
    +---+
    O   |
   /|   |
        |
       ===
    """,
    r"""
    +---+
    O   |
   /|\  |
        |
       ===
    """,
    r"""
    +---+
    O   |
   /|\  |
   /    |
       ===
    """,
    r"""
    +---+
    O   |
   /|\  |
   / \  |
       ===
    """,
]

words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()


# Returns random world from word list
def get_random_word(word_list):
    word_index = randint(0, len(word_list) - 1)
    return word_list[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])

    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")

    print()

    blanks = "_" * len(secret_word)

    # update blanks to represent the correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1 :]

    # display updated blanks with space between each letter
    for letter in blanks:
        print(letter, end=" ")

    print()


# Ensure player enters single letter at a time
def get_guess(already_guessed):
    while True:
        print("Guess a letter:")
        guess = input()
        guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijkmnlopqrstuvwyz":
            print("Please enter a LETTER.")
        else:
            return guess


def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


# This is the state of the application
print("H A N G M A N")
missed_letters = ""
correct_letters = ""
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    # let the player enter a letter, and check whether guess letter
    # conforms to the various checks in the function
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess

        # Check if the player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break

        if found_all_letters:
            print(f"Yes! The secrect word is '{secret_word}'! You have won!")
            game_is_done = True
    else:
        missed_letters += guess

        # Check if player has guessed too many times and lost.
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print(
                f"You have run out of guesses!\n After {str(len(missed_letters))} missed guesses and {str(len(correct_letters))} correct guesses, the word was '{secret_word}'"
            )
            game_is_done = True

        # Ask player if they want to play again
        # and reset the state of the application
        if game_is_done:
            if play_again():
                missed_letters = ""
                correct_letters = ""
                game_is_done = False
                secret_word = get_random_word(words)
            else:
                break

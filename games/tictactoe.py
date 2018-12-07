import random


def draw_board(board):
    print(f"{board[7]}|{board[8]}|{board[9]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[1]}|{board[2]}|{board[3]}")


def input_player_letter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be 'X' or 'O'?")
        letter = input().upper()

    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def who_goes_first():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    # winning angles:
    # 1 -> top row
    # 2 -> middle row
    # 3 -> bottom row
    # 4 -> left column
    # 5 -> middle column
    # 6 -> right column
    # 7 -> 45 deg diagnoal
    # 8 -> 135 deg diagnoal
    return (
        (board[7] == letter and board[8] == letter and board[9] == letter)
        or (board[4] == letter and board[5] == letter and board[6] == letter)
        or (board[1] == letter and board[2] == letter and board[3] == letter)
        or (board[7] == letter and board[4] == letter and board[1] == letter)
        or (board[8] == letter and board[5] == letter and board[2] == letter)
        or (board[9] == letter and board[6] == letter and board[3] == letter)
        or (board[7] == letter and board[5] == letter and board[3] == letter)
        or (board[9] == letter and board[5] == letter and board[1] == letter)
    )


def get_board_copy(board):
    # Make a copy of the board list and return it.
    # In the presence of nested arrays, the copy will be shallow,
    # thus changes to nested arrays are also visible in originals as
    # their values are passed by reference
    return [*board]


def is_space_free(board, move):
    return board[move] == " "


def get_player_move(board):
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not is_space_free(
        board, int(move)
    ):
        print("What is your next move? (1 - 9)")
        move = input()
    return int(move)


# Given a list of available positions on board, randomly place computer
# move in one of the spaces
def choose_random_move_from_list(board, move_list):
    possible_moves = []
    for i in move_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to
    # move and return that move.
    if computer_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    # Tic-Tac-Toe AI algorithm
    # Check scenarios in which computer can win
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i

    # Check scenarios in which player wins and block him/her
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    # Try to take one of the corners, if they're free
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free
    if is_space_free(board, 5):
        return 5

    # Get any other available space on board
    return choose_random_move_from_list(board, [2, 4, 6, 8])


# Check of all spaces in board are taken
def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print("Welcome to Tic-Tac-Toe!")

while True:
    # Reset the board
    the_board = [" "] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print(f"The {turn} will go first.")
    game_is_playing = True

    while game_is_playing:
        if turn == "player":
            # Player's turn
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print("Hooray! You have won the game!")
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            # Computer's turn
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print("The computer has beaten you! You lose.")
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

    print("Do you want to player again? (yes or no)")
    if not input().lower().startswith("y"):
        break

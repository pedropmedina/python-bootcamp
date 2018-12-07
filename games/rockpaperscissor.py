from random import randint

print('Rock...')
print('Paper...')
print('Scissor...')

options = ['rock', 'paper', 'scissor']
rand_idx = randint(0, 2)
player_1 = input('Player 1, make your move: ')
player_2 = options[rand_idx]
print(f'Computer players {player_2}')

if player_1 == player_2:
    print('It\'s a tie!')
elif player_1 == 'rock':
    if player_2 == 'paper':
        print('player 2 wins')
    if player_2 == 'scissor':
        print('player 1 wins')
elif player_1 == 'paper':
    if player_2 == 'rock':
        print('player 1 wins')
    if player_2 == 'scissor':
        print('player 2 wins')
elif player_1 == 'scissor':
    if player_2 == 'paper':
        print('player 1 wins')
    if player_2 == 'rock':
        print('player 2 wins')
else:
    print('something went wrong')

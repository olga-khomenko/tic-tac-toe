import random
from IPython.display import clear_output

board = [' '] * 9


# 1. Func to display game
def display_board(board):
    clear_output()
    for x in range(0, 9, 3):
        # Make the board look empty
        print(f'{board[x:x+3]}'.replace(", ", "|").replace("'", "").replace("[", " ").replace("]", " "))


# 2. Func that take players' input "X" or "O"
def player_input():
    """
    Defines which symbol of (X or O) players have
    """
    markers = ['X', 'O']
    while True:
        marker = input('Player 1, how will you play X or O?').upper()
        if marker.upper() not in markers:
            print(f'Sorry, invalid choice. Enter {markers[0]} or {markers[1]}.')
            continue
        else:
            player1 = marker.upper()
            markers.remove(marker)
            player2 = markers[0]
            return player1, player2


# player1_marker, player2_marker = player_input()
# print(f'Player 1 choice: {player1_marker}')
# print(f'Player 2 choice: {player2_marker}')


# 3. Fun that takes in the board list object, a marker (X or O) and position (1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position-1] = marker


# 4. Func takes in board and a mark (x or O) and checks if that mark has won.
def win_check(board, mark):
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[6] == mark and board[3] == mark and board[0] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[8] == mark and board[4] == mark and board[0] == mark) or
            (board[6] == mark and board[4] == mark and board[2] == mark))


# 5.Func that uses random module to decide which player goes first. Use random.randint().
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# 6. Func that returns a boolean indicating that a space on the board is available.
# Check if the position is an empty string
def space_check(board, position):
    return board[position] == ' '


# 7. Func that checks if the board is full and returns a boolean. True - full, False - not full.
def full_board_check(board):
    if ' ' in board:
        return False
    return True


# 8. Func that asks for player's next position (1-9) and uses func 6 to check if it is free.
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))
        return position


# 9. Func to ask a player if they want to play again. Returns boolean True if they want to continue.
def replay():
    choice = input('Do you want to play again? Yes or No.')
    return choice == "Yes"


# 10. Use while loops and funcs above to run the game.
print('Welcome to my first project: TIC TAC TOE')

# While loop to keep running the game.

while True:
    # Play the game
    # set up: board, who first, choose markers(x,0)
    the_board = [' '] * 9
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + 'will go first')

    play_game = input('Ready to play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # game play
    while game_on:
        if turn == 'Player 1':
            # player 1 turn
            # 1. Show the board
            display_board(the_board)
            # 2. Choose a position
            position = player_choice(the_board)
            # 3. Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # 4. Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            # 5. Check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = "Player 2"
            # 6. No tie no win? Next player's turn.
        else:
            # player 2 turn
            # 1. Show the board
            display_board(the_board)
            # 2. Choose a position
            position = player_choice(the_board)
            # 3. Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # 4. Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            # 5. Check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game.")
                    game_on = False
                else:
                    turn = "Player 1"
            # 6. No tie no win? Next player's turn.

    if not replay():
        break
        # Break out of the loop on replay func ()

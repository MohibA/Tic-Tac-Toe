
# 3x3 game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

#Global variables

game_is_on = True
winner = None
player_one = 'x'
player_two = 'o'
current_player = player_one


def drawboard():
    print(board[0] + ' | ' + board[1] + ' | '+ board[2])
    print(board[3] + ' | ' + board[4] + ' | '+ board[5])
    print(board[6] + ' | ' + board[7] + ' | '+ board[8])


#This will be the main function to run our game
def play():
    #draw_board
    print("Welcome to tic tac toe. Player one = x and player two = o")
    print('')
    drawboard()

    while game_is_on:
        current_turn(current_player)

        check_game()

        change_player()

    if winner == player_one:
        print('player one(x) won.')
    if winner == player_two:
        print('player one(o) won.')
    elif winner == None:
        print('Tie')


#handle players turn. Check if turn is valid and place current players letter on board
def current_turn(player):

    # you can also have it says x's turn or o's turn by simply having it print (player + "'s turn").
    #But I like it better this way so it prints player one or player two.
    
    if player == player_one:
        print("player one's turn")
    else:
        print("player two's turn.")
        
    position = int(input('choose a position from 1-9'))

    # set valid turn to false the run a while loop to check if input is betweein 1-9 and the spot is empty
    valid_turn = False

    while not valid_turn:

        while position not in range(1,10):
            position = input('choose a position from 1-9')

        position = int(position) -1

        if board[position] == '-':
            valid_turn = True
        else:
            print("can't go there again")
    board[position] = player
    drawboard()

# function to check for a win or a tie
def check_game():
    check_for_win()
    check_for_tie()

 # check for winner from either row,column or diagonal
def check_for_win():

    # Check rows,columns and diagonals
    global winner

    rows_winner = row_winner()
    column_winner = columns_winner()
    diagonal_winner = check_diagonal_win()
    check_for_tie()

    if rows_winner:
        winner = rows_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return




    return

#check all rows to see if they contain the same letter
def row_winner():

    global game_is_on

    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_is_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


    else:
        return None

#Check columns for same letter to declare winner
def columns_winner():

    global game_is_on


    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        game_is_on = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    else:
        return None

#check diagonals to see winner
def check_diagonal_win():

    global game_is_on


    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'


    if diagonal_1 or diagonal_2:
        game_is_on = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    else:
        return None


#end game if there is no empty spot on board declaring a tie
def check_for_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
        return True

    else:
        return False


#change player after turn
def change_player():

    global current_player
    global player_one
    global player_two

    if current_player == player_one:
        current_player = player_two

    elif current_player == player_two:
        current_player = player_one


#function to run entire game
play()

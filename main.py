#board
#display board
#play game
#handle the turns
#check win
 #check rows
 #check columns
 #check diagonals
#check tie
#flip player


board=["_", "_", "_",
       "_", "_", "_",
       "_", "_", "_"]

game_still_going=True

winner=None

current_player="X"

def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])


def play_game():
    display_board()  # display initial board


    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

#gane has ended
    if winner=="X" or winner=="O":
        print(winner + "'won'")
    elif winner==None:
        print("Tie")

def handle_turn(player):

    print(player + "'s turn.")
    position=input('choose a position b/w 1-9:')

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("invalid input,choose a position b/w 1-9:")

        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("go again")

    board[position]=player

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():

    global winner #set up global variable
    #check rows


    row_winner=check_rows()

    column_winner=check_columns()

    diagonal_winner=check_diagonals()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_rows():
    global game_still_going #set up local variable
    row_1 = board[0] == board[1] == board[2] !="_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False

     #return the winner
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]


def check_columns():
    global game_still_going  # set up local variable
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_going = False

    # return the winner
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]


def check_diagonals():
    global game_still_going  # set up local variable
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]



def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going=False
    return

def flip_player():
    global current_player

    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return

play_game()

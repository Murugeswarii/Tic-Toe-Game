def get_user_choice_symbol():
    user_choice_symbol = ' '
    while user_choice_symbol not in ('X','O'):
        user_choice_symbol = input("Enter choice 'X' or 'O' : ").upper()
    return user_choice_symbol
def place_in_board(game_board, sym_position, user_choice_symbol):
        if not game_board[sym_position-1] in ('X','O'):
            game_board[sym_position-1] = user_choice_symbol
            return True
        else:
            print('This position is already occupied.')
            return False
def get_symbol_position(user_choice_symbol):
        sym_position = 0
        while sym_position not in (1,2,3,4,5,6,7,8,9):
            sym_position = int(input('Enter position for '+ user_choice_symbol+ ' : '))
        return sym_position 
def change_symbol(user_choice_symbol):
        if user_choice_symbol.upper() == 'X':
            return 'O'
        else:
            return 'X'
def display_board(game_board):
        print('\n')
        for (index, item) in enumerate(game_board):
            if (index+1) % 3 == 0:
                print(item)
                if (index+1) <= 6:
                    print('----------')
            else:
                print(item, end=' | ')
        print('\n')
def won_game(game_board, user_choice_symbol):
        def horizontal_match(game_board):
            return ((game_board[0] == game_board[1] == game_board[2] == user_choice_symbol) or
                (game_board[3] == game_board[4] == game_board[5] == user_choice_symbol) or
                (game_board[6] == game_board[7] == game_board[8] == user_choice_symbol))
        def vertical_match(game_board):
            return ((game_board[0] == game_board[3] == game_board[6] == user_choice_symbol) or
                (game_board[1] == game_board[4] == game_board[7] == user_choice_symbol) or
                (game_board[2] == game_board[5] == game_board[8] == user_choice_symbol))
        def diagonal_match(game_board):
            return ((game_board[0] == game_board[4] == game_board[8] == user_choice_symbol) or
                (game_board[2] == game_board[4] == game_board[6] == user_choice_symbol))
        return horizontal_match(game_board) or vertical_match(game_board) or diagonal_match(game_board)
def full_board(game_board):
    for i in game_board:
        if i not in ('X', 'O'):
            return False
    return True

def switch_user(user_choice_symbol):
    return change_symbol(user_choice_symbol)
def replay(user_choice_symbol):
    play_again = input("Do you want to play again? 'Yes' or 'No' : ")
    if play_again.lower() == 'yes':
        return True
    elif play_again.lower() == 'no':
        return False
def init_board():
    return [' ',' ',' ',' ',' ',' ',' ',' ',' ']
def start_game():
    print('Welcome to Tic Tac Toe!')
    
    # Initialize board with empty values
    game_board = init_board()                   
    display_board(game_board)

    #Get the user's choice of symbol
    user_choice_symbol = get_user_choice_symbol()

    def play_game(game_board, user_choice_symbol):

        #Get the position to place the symbol
        sym_position = get_symbol_position(user_choice_symbol)

        #If the symbol is not placed, that means already entry is found at that position so get the position again and proceed
        if not place_in_board(game_board, sym_position, user_choice_symbol):
             play_game(game_board, user_choice_symbol)
        else:
            #Symbol is placed in the board
            display_board(game_board)

            #If the symbols match, it means the user has won. so ask the user if they want to play again
            if won_game(game_board, user_choice_symbol):
                print(user_choice_symbol.upper() + ' has WON !!!')
                if replay(user_choice_symbol):
                     start_game()
            else:
                # check if the game is tie
                if full_board(game_board):
                    print('Game is Tie !!!')
                    if replay(user_choice_symbol):
                         start_game()
                else:
                    #If the game is not ended proceed with next step
                    user_choice_symbol = switch_user(user_choice_symbol)
                    play_game(game_board, user_choice_symbol)

    #Start the game
    play_game(game_board, user_choice_symbol)
           
start_game()

import random
from colorama import init
from colorama import Fore as f
from colorama import Style as s

reset = s.RESET_ALL
cyan = f.CYAN

init(autoreset=True)

def display_board(board=list[str]):
    print()

    def colored_cell(cell:str):
        cell = str(cell)
        if cell == 'X':
            return f.RED+cell+reset

        elif cell == 'O':
            return f.BLUE+cell+reset

        else:
            return f.YELLOW+cell+reset


    print(' '+colored_cell(board[0])+'|'+colored_cell(board[1])+'|'+colored_cell(board[2]))
    print(cyan+'---+---+---'+reset)
    print(' '+colored_cell(board[3])+'|'+colored_cell(board[4])+'|'+colored_cell(board[5]))
    print(cyan+'---+---+---'+reset)
    print(' '+colored_cell(board[6])+'|'+colored_cell(board[7])+'|'+colored_cell(board[8]))

    print()

def player_choice():
    symbol = ''
    while symbol not in ['X','O']:
        symbol = input(f.GREEN+'Do you want to be X or O?: '+reset).upper()

        if symbol=='X':
            return ('X','O')
        else:
            return ('O','X')

def player_move(board:list,symbol):
    move = -1

    while move not in range(1,10) or board[move-1] in ['X', 'O']:
        try:
            move = int(input('Enter your move (1-9): '))
            if move not in range(1,10) or board[move-1] in ['X', 'O']:
                print('Invalid move. Please try again')

        except ValueError:
            print('Please enter a number between 1 and 9')

    board[move-1]=symbol

def ai_move(board,ai_symbol,player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy,ai_symbol):
                board[i] = ai_symbol
                return

    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy,player_symbol):
                board[i] = ai_symbol
                return

    possible_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board,symbol):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),#Horizontal
        (0,3,6),(1,4,7),(2,5,8),#Vertical
        (0,4,8),(2,4,6)#Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True

    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print('Welcome to Tic-Tac-Toe!')
    player_name = input(f.GREEN+'Enter your name: '+reset)
    while True:
        board = [str(i) for i in range(1, 10)]
        player_symbol,ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)

            if turn=='Player':
                player_move(board,player_symbol)
                if check_win(board,player_symbol):
                    display_board(board)
                    print(f'{f.GREEN}Congratulations! {player_name}, you have won the game!')
                    game_on=False

                else:
                    if check_full(board):
                        display_board(board)
                        print(f"{f.YELLOW}It's a tie.")
                        break
                    else:
                        turn='AI'
            else:
                ai_move(board,ai_symbol,player_symbol)
                if check_win(board,ai_symbol):
                    print(f"{f.RED} AI has won the game!")
                    game_on=False
                else:
                    if check_full(board):
                        display_board(board)
                        print(f"{f.YELLOW}It's a tie.")
                        break
                    else:
                        turn='Player'

        play_again = input('Do you want to play again? (yes/no/y/n): ').lower()
        if play_again!='yes' or play_again!='y':
            print(f"{cyan}Thank you for playing!")
            break


if __name__=='__main__':
    tic_tac_toe()
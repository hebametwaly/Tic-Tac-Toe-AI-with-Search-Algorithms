
board = [" " for _ in range(9)]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def get_available_moves(board):
    return [i for i, x in enumerate(board) if x == " "]

 
def player_move(symbol):
    move = int(input("Enter your move (1-9): ")) - 1
    while board[move] != " ":
        print("Invalid move. Try again.")
        move = int(input("Enter your move (1-9): ")) - 1
    board[move] = symbol


def computer_move(symbol):
    def dfs(board, symbol, depth, max_depth):
        if depth > max_depth:
            return None
        for move in get_available_moves(board):
            new_board = board[:]
            new_board[move] = symbol
            
            if check_winner(new_board, symbol):
                return move  
            
            result = dfs(new_board, symbol, depth + 1, max_depth)
            if result is not None:
                return result  
        return None

    
    max_search_depth = 5  
    for depth_limit in range(1, max_search_depth + 1):
        best_move = dfs(board, symbol, 0, depth_limit)
        if best_move is not None:
            board[best_move] = symbol  
            return

    for move in get_available_moves(board):
        board[move] = symbol
        return


def tic_tac_toe():
    player_symbol = input("Choose your symbol (X/O): ").upper()
    computer_symbol = "O" if player_symbol == "X" else "X"
    current_turn = "Player"

    print_board(board)

    for _ in range(9):  
        if current_turn == "Player":
            print("Player's turn")
            player_move(player_symbol)
            if check_winner(board, player_symbol):
                print_board(board)
                print("Congratulations! You win!")
                return
            current_turn = "Computer"
        else:
            print("Computer's turn")
            computer_move(computer_symbol)
            if check_winner(board, computer_symbol):
                print_board(board)
                print("Computer wins!")
                return
            current_turn = "Player"
        print_board(board)

    print("It's a tie!")


tic_tac_toe()

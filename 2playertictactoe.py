def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = players[0]
    while True:
        print_board(board)
        row = int(input("Enter row number (0-2): "))
        col = int(input("Enter column number (0-2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                break
            if all(board[i][j] != " " for i in range(3) for j in range(3)):
                print_board(board)
                print("Result is tie")
                break
            current_player = players[(players.index(current_player) + 1) % 2]
        else:
            print("space filled")

tic_tac_toe()

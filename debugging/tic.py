#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board) and not is_full(board):
        print_board(board)
        try:
            row = int(input("Enter row (0,1,2) for player " + player + ": "))
            col = int(input("Enter column (0,1,2) for player " + player + ": "))
            if row not in range(3) or col not in range(3):
                print("Coordinates must be 0, 1, or 2. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number 0, 1, or 2.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    if check_winner(board):
        winner = "O" if player == "X" else "X"
        print("Player " + winner + " wins!")
    else:
        print("It's a tie!")

tic_tac_toe()

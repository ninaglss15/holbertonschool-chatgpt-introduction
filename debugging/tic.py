#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
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


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    quit_game = False

    while not check_winner(board):
        print_board(board)

        try:
            row_input = input("Enter row (0, 1, or 2) for player " + player + ": ")
            if row_input == "exit":
                print("Players leave the game")
                quit_game = True
                break
            row = int(row_input)
            if not (0 <= row <= 2):
                print("Row must be 0, 1 or 2.")
                continue

            col_input = input("Enter col (0, 1, or 2) for player " + player + ": ")
            if col_input == "exit":
                print("Players leave the game")
                quit_game = True
                break
            col = int(col_input)
            if not (0 <= col <= 2):
                print("Column must be 0, 1 or 2.")
                continue

        except EOFError:
            print("Exit via Ctrl+D")
            quit_game = True
            break
        except KeyboardInterrupt:
            print("\nExit via Ctrl+C")
            quit_game = True
            break
        except ValueError:
            print("Wrong input ! You have to use 0, 1 or 2")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            winner = player

            if not check_winner(board):
                empty_case = False
                for row in board:
                    for cell in row:
                        if cell == " ":
                            empty_case = True
                            break
                if not empty_case:
                    print("It's a draw !")
                    quit_game = True
                    break

            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    if not quit_game:
        print_board(board)
        print("Player " + winner + " wins!")


tic_tac_toe()
import os
import random

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_board(board):
    clear_screen()
    print(f"{players[0]} (X)  -  {players[1]} (O)\n")
    print("     |     |     ")
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ")
    print("     |     |     \n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_tic_tac_toe():
    global players
    players = [input("Enter Player 1's name (X): "), input("Enter Player 2's name (O): ")]
    scores = {players[0]: 0, players[1]: 0}
    
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        print("\nWelcome to Tic-Tac-Toe!")
        print_board(board)

        while True:
            row = int(input(f"{players[current_player == 'X']} ({current_player}), enter row (0, 1, 2): "))
            col = int(input(f"{players[current_player == 'X']} ({current_player}), enter column (0, 1, 2): "))

            if board[row][col] != " ":
                print("That cell is already taken. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"{players[current_player == 'X']} ({current_player}) wins! Congratulations!")
                scores[players[current_player == 'X']] += 1
                break

            if is_board_full(board):
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        print("Scores:")
        print(f"{players[0]} ({players['X']}): {scores[players[0]]}")
        print(f"{players[1]} ({players['O']}): {scores[players[1]]}")

        play_again = input("Play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()

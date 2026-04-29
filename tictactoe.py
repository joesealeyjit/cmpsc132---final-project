"""
CMPSC 132 Final Project: Tic-Tac-Toe Game
Author: Joe Sealey

A two-player terminal-based Tic-Tac-Toe game.
Players alternate turns as X and O until one player wins or the game ends in a draw.
"""


def create_board():
    """
    Create and return a 3x3 Tic-Tac-Toe board.

    Each empty space is represented by a single space character.
    """
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    """
    Print the current Tic-Tac-Toe board in a readable format.
    """
    print("\nCurrent Board:")
    print("   0   1   2")
    for row_index in range(3):
        print(f"{row_index}  {board[row_index][0]} | {board[row_index][1]} | {board[row_index][2]}")
        if row_index < 2:
            print("  ---+---+---")
    print()


def check_winner(board, player):
    """
    Return True if the given player has won the game.

    A player wins by getting three marks in a row, column, or diagonal.
    """
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_draw(board):
    """
    Return True if the board is full and there is no winner.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def get_valid_move(board, player):
    """
    Ask the current player for a valid row and column.

    This function keeps asking until the player enters:
    - two numbers
    - numbers between 0 and 2
    - a position that is not already occupied
    """
    while True:
        move = input(f"Player {player}, enter your move as row column (example: 1 2): ").strip()
        parts = move.split()

        if len(parts) != 2:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        try:
            row = int(parts[0])
            col = int(parts[1])
        except ValueError:
            print("Invalid input. Row and column must be numbers.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Row and column must both be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("Invalid move. That space is already taken.")
            continue

        return row, col


def switch_player(current_player):
    """
    Switch from X to O, or from O to X.
    """
    if current_player == "X":
        return "O"
    return "X"


def play_game():
    """
    Run one full game of Tic-Tac-Toe.
    """
    board = create_board()
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Two players will take turns entering a row and column from 0 to 2.")
    print("Example move: 0 2")

    while True:
        print_board(board)
        row, col = get_valid_move(board, current_player)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        if is_draw(board):
            print_board(board)
            print("The game ended in a draw!")
            break

        current_player = switch_player(current_player)


def ask_play_again():
    """
    Ask users if they want to play another game.
    """
    while True:
        answer = input("Would you like to play again? (yes/no): ").strip().lower()
        if answer == "yes" or answer == "y":
            return True
        if answer == "no" or answer == "n":
            return False
        print("Please enter yes or no.")


def main():
    """
    Main program loop.
    """
    while True:
        play_game()
        if not ask_play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

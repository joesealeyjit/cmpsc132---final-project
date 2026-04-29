# cmpsc132---final-project

## Project Description

This project is a two-player terminal-based Tic-Tac-Toe game written in Python. Two players take turns entering their moves as row and column coordinates. Player X goes first, then Player O. The game continues until one player gets three marks in a row, column, or diagonal, or until the board is full and the game ends in a draw.

## Features

- Displays a 3x3 Tic-Tac-Toe board
- Allows two players to alternate turns as X and O
- Accepts row and column input from 0 to 2
- Prevents invalid moves
- Prevents players from choosing occupied spaces
- Detects row, column, and diagonal wins
- Detects draw games
- Allows players to replay after a game ends

## Data Structures Used

The board is stored as a list of lists:

```python
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
```

Each inner list represents one row of the board.

## How to Run the Program

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python tictactoe.py
```

Depending on your computer, you may need to run:

```bash
python3 tictactoe.py
```

## How to Play

When the game asks for a move, enter the row and column separated by a space.

Example:

```text
Player X, enter your move as row column (example: 1 2): 0 2
```

Rows and columns must be numbers from 0 to 2.



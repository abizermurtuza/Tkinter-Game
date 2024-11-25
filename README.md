# Tkinter Game

This project is a simple two-player game built using the Python `tkinter` library. Players take turns to claim the most space within a 2D grid of squares.

## Overview

The game gives each player three turns to claim as many squares as possible in a grid. The player with the most claimed squares by the end of the game wins.

## Features

- **Main Menu**: Allows customization of grid size, player colors, and number of turns.
- **Game Board**: Dynamically created based on user input.
- **Turn-Based Gameplay**: Players alternate turns to claim squares.
- **Win Condition**: The game declares a winner based on the number of squares claimed or a tie if both players claim an equal number of squares.

## How to Play

1. **Main Menu**: Configure the game settings including the number of rows, columns, and total turns.
2. **Instructions**: Read the game instructions from the main menu.
3. **Start Game**: Click the "START GAME" button to begin.
4. **Gameplay**:
   - Player 1 starts first and claims a square by clicking on it.
   - Players alternate turns until all turns are used.
5. **Win Condition**: The game announces the winner based on the number of squares claimed.

## Usage

To run the game, execute `Tkinter Game.py` in a Python environment. Ensure that the `tkinter` library is available.

```sh
python Tkinter\ Game.py

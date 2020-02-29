# This file will contain the various functions needed for displaying the board in the terminal.
import os
import time


def clear():
    """ Wipes the terminal screen of all text. """
    os.system("clear||cls")
    return


def print_example_board():
    print("When you are selecting a starting square the following board indexing format is used.\nSquare indices are of the form (row, column) where row 1 is the top row and column 1 is the left-most column.\neg.\n")
    for i in range(16):
        if i % 4 == 0:
            print()
        print(f"{i:02d}", end=' ')
    print("\n")
    return


def print_final_board(knight_positions, all_squares, m, n):
    """
    Prints the full knight's tour path to the screen. Squares are numbered 1-num_squares in order of
    the squares taken by the knight for the full knight's tour.
    """
    clear()
    print("Here is your completed knight's tour.")
    for i in range(m*n):
        if i % n == 0:
            print()
        print(f"{knight_positions.index(all_squares[i])+1:02d}", end=' ')
    return


def print_moves(knight_positions, speed, all_squares, m, n):
    """
    For each move the knight takes a makeshift board consisting of zeros will be printed to the screen.
    The knight's current position will be represented by a 7.
    """
    clear()
    if speed == "slow":
        wait = 1
    elif speed == "medium":
        wait = 0.6
    elif speed == "fast":
        wait = 0.25
    move_num = 0
    for move in knight_positions:
        clear()
        print("Move number: ", move_num)
        move_num += 1
        for i in range(m*n):
            if i % n == 0:
                print()
            if i == all_squares.index(move):
                print(7, end=' ')
            else:
                print(0, end=' ')
        print()
        time.sleep(wait)
    return


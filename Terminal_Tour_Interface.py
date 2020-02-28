# This file will contain the majority of the text which will be printed to the screen and also functions
# will be called when asking for user input.
import os


def clear():
    os.system("clear||cls")
    return


def greeting():
    print("Welcome to Terminal Tour, a python programme which will solve (if possible) the classic chess problem known as the knight's tour and print the completed tour to your screen step by step.\nThis problem is a chess themed instance of the more general hamiltonian path problem, in which each vertex of a graph must be visited exactly once.\nCurrently the largest supported board size is 10x10 as the wait times become excessive beyond this size. Everything up to 9x9 should run rather quickly but please allow up to 2 minutes for 10x10\n")
    return


def get_board_size():
    m, n = input("Please input the desired row x column board size (eg. 8 8): ").split()
    m, n = int(m), int(n)
    if m in list(range(1, 11)) and n in list(range(1, 11)):
        return m, n
    else:
        print("The chosen board size is currently not supported.\n")
        return get_board_size()
    
    
def choose_speed():
    speed = input("Please choose the speed at which you would like each move to be displayed in the terminal (slow, medium, fast): ")
    if speed in ["slow", "medium", "fast"]:
        return speed
    else:
        print("Please select the speed from one of the options above.\n")
        return choose_speed()
    
    
def go_again():
    response = input('If you would like to try another board please type "yes", else type "no".')
    if response == "yes": return True
    if response == "no": return False
    return go_again()
    

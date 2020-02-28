# This file will contain the majority of the text which will be printed to the screen and also functions
# that will be called when asking for user input.


def greeting():
    print("Welcome to Terminal Tour, a python programme which will solve (if possible) the classic chess problem known as the knight's tour and print the completed tour to your screen step by step.\n\nThis problem is a chess themed instance of the more general hamiltonian path problem, in which each vertex of a graph must be visited exactly once.\n\nCurrently the largest supported board size is 10x10 as the wait times become excessive beyond this size. Everything up to 8x8 should run almost instantly, 9x9 should run rather quickly but please allow up to 2 minutes for 10x10\n")
    input("Hit the return key to continue.\n")
    return


def get_board_size():
    try:
        m, n = input("Please input the desired row x column board size (eg. 8 8): ").strip().split()
        m, n = int(m), int(n)
        if m in list(range(1, 11)) and n in list(range(1, 11)):
            print()
            return m, n
        else:
            print("The chosen board size is currently not supported.\n")
            return get_board_size()
    except:
        print("Please use the specified input format.")
        return get_board_size()
    
def get_square(m, n):
    try:
        i, j = input("Please enter the starting square's index. Please enter two space separated numbers where the first number corresponds to the starting square's row and the second number to its column (eg 4 5): ").strip().split()
        if 0 < int(i) < m + 1 and 0 < int(j) < n + 1: 
            print()
            return int(m) - 1, int(n) - 1
        else:
            print("That square does not exist on the board size you have specified.\n")
            return get_square(m, n)
    except:
        print("Please enter the starting square's index as specified.\n")
        return get_square(m, n)
    
    
def choose_speed():
    speed = input("Please choose the speed at which you would like each move to be displayed in the terminal (slow, medium, fast): ").strip()
    if speed in ["slow", "medium", "fast"]:
        print()
        return speed
    else:
        print("Please select the speed from one of the options above.\n")
        return choose_speed()
    
    
def go_again():
    print("\n")
    response = input('If you would like to try another board please type "yes", else type "no": ')
    if response == "yes": 
        return True
    elif response == "no": 
        return False
    else:
        print("Please enter either yes or no to continue or exit.")
        return go_again()
    

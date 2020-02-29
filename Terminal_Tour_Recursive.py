"""
This file will function as the main function for this project.
"""
import Print_Board as pb
import Terminal_Tour_Interface as tti
import time

# knight moves represented by addition of row and column indices
move_types = ((-2,1), (2,1), (1,-2), (1,2), (-1,2), (-1, -2), (-2,-1), (2,-1)) 
l = None
stack = None
possible_moves = None
used = None
num_squares = None

def available_moves(current_pos, all_squares):
    """ 
    On an m x n matrix board a knight's movements can be represented by addition and subtraction.
    """
    return [(current_pos[0] + move[0], current_pos[1] + move[1]) for move in move_types if (current_pos[0] + move[0], current_pos[1] + move[1]) in all_squares]


def next_move(square):
    """
    A DFS of all possible knight's tours which terminates as soon as the number of moves (l) is
    equal to the number of squares on the board. 
    Global variables are used for optimization puproses to lower the overhead of the recursive stack.
    
    square: the knight's current square on the board.
    stack: the current list of moves taken by the knight.
    used: a dictionary which states returns true if a square is in the stack.
    possible_moves: a dictionary which returns a lsit of all legal moves from a square.
    """
    global stack
    global l
    global num_squares
    global used
    global possible_moves
    
    l += 1
    stack.append(square)
    used[square] = True
    if l == num_squares:
        return stack, l
    for sqr in possible_moves[square]:
        if not used[sqr]:
            temp = next_move(sqr)
            if temp[1] == num_squares:
                return temp
    else:
        l -= 1
        stack.pop()
        used[square] = False
        return stack, l


def main():
    global l
    global stack
    global possible_moves
    global used
    global num_squares
    
    pb.clear()
    again = True
    tti.greeting()
    while again:
        pb.clear()
        m, n  = tti.get_board_size()
        pb.print_example_board()
        starting_square = tti.get_square(m, n)
        speed = tti.choose_speed()
        
        num_squares = m*n   
        l = 0               # the length of stack
        stack = []          # will keep track of knight moves
        all_squares = [(i,j) for i in range(m) for j in range(n)]
    
        used = {sqr: False for sqr in all_squares}  # returns True if a square is in the stack
        possible_moves = {sqr: available_moves(sqr, all_squares) for sqr in all_squares}
        
        # sorts possible moves from each square by which square has the least number of possible moves from it (Warnsdorff's algorithm).
        for key in possible_moves.keys():
            moves = possible_moves[key]
            degree_moves = [(len(available_moves(move, all_squares)), move) for move in moves]
            degree_moves.sort()
            possible_moves[key] = [degree_moves[i][1] for i in range(len(degree_moves))]
            
        knight_positions = next_move(starting_square)[0]

        if not knight_positions:
            print()
            print("A knight's tour could not be calculated for a board with the chosen dimensions.")
        else:
            pb.print_moves(knight_positions, speed, all_squares, m, n)
            pb.print_final_board(knight_positions, all_squares, m, n)
        print(knight_positions)
        again = tti.go_again()
    exit()


if __name__ == "__main__":
    main()

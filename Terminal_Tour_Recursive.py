import config as cfg

# knight moves represented  addition of row and column indices
move_types = ((-2,1), (2,1), (1,-2), (1,2), (-1,2), (-1, -2), (-2,-1), (2,-1)) 


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
    #global num_squares
    #global l
    #global stack
    #global used
    #global possible_moves
    
    cfg.l += 1
    cfg.stack.append(square)
    cfg.used[square] = True
    if cfg.l == cfg.num_squares:
        return cfg.stack, cfg.l
    for i in range(len(cfg.possible_moves[square])):
        if not cfg.used[cfg.possible_moves[square][i]]:
            temp = next_move(cfg.possible_moves[square][i])
            if temp[1] == cfg.num_squares:
                return temp
            
    else:
        cfg.l -= 1
        cfg.stack.pop()
        cfg.used[square] = False
        return cfg.stack, cfg.l

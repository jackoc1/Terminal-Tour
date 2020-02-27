# Attempt to solve the knight's tour chess puzzle programmatically for chess boards with dimension n x n.
# Current method to check if a square is visited will be to check if the square is already 
# in the stack -> change to hashmap true/false check.
# The knight's tour is considered complete if we can reach a stack length equal to the number of squares on the board
# taking only valid moves at that point (hamiltonian path).
# 
# Using Warnsdorff's algorithm

n = 7       # change to int(input())
l = 0       # length of move stack
stack = []  # keep track of moves currently taken

# move to program declaration
starting_square = int(input("Enter square row: ")), int(input("Enter square column: "))
all_squares = [(i,j) for i in range(n) for j in range(n)] # first index = row, second index = column
move_types = ((-2,1), (2,1), (1,-2), (1,2), (-1,2), (-1, -2), (-2,-1), (2,-1)) # knight moves as addition of row and column index


def print_board(knight_positions): # needs to be readjusted to accomodate matrix notation
    """
    knight_positions is a list of length 64. Index corresponds to move number.
    Value at index corresponds to position on board at that move number.
    """
    for i in range(n**2):
        if i % n == 0:
            print()
        print(f"{knight_positions[i]:02d}", end=' ')
    print()
    return


def available_moves(current_pos): # needs an if check for if a square has already been visited.
    """ 
    On an n x n matrix board a knight's movements can be represented by addition and subtraction.
    """
    return [(current_pos[0] + move[0], current_pos[1] + move[1]) for move in move_types if (current_pos[0] + move[0], current_pos[1] + move[1]) in all_squares]


# dictionaries for constant time lookups
used = {sqr: False for sqr in all_squares}
possible_moves = {sqr: available_moves(sqr) for sqr in all_squares}


# sort by number of possible moves from that square
for key in possible_moves.keys():
    moves = possible_moves[key]
    degree_moves = [(len(available_moves(move)), move) for move in moves]
    degree_moves.sort()
    possible_moves[key] = [degree_moves[i][1] for i in range(len(degree_moves))]


def next_move(square, stack, n, l, used, possible_moves):
    l += 1
    stack.append(square)
    used[square] = True
    if l == n**2:
        return stack, l
    #print(stack, l)
    #print()
    for i in range(len(possible_moves[square])):
        if not used[possible_moves[square][i]]:
            temp = next_move(possible_moves[square][i], stack, n, l, used, possible_moves)
            if temp[1] == n**2:
                return temp
            
    else:
        l -= 1
        stack.pop()
        used[square] = False
        return stack, l
        
            
        
# the big sad has defeated me for tonight
    






print(next_move(starting_square, stack, n, l, used, possible_moves))














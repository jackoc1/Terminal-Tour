# Attempt to solve the knight's tour chess puzzle programmatically for chess boards with dimension n x n.
# Current method to check if a square is visited will be to check if the square is already 
# in the stack -> change to hashmap true/false check.
# The knight's tour is considered complete if we can reach a stack length equal to the number of squares on the board
# taking only valid moves at that point (hamiltonian path).
# 
# Using Warnsdorff's algorithm

n = 5       # change to int(input())
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


def available_moves_from_square(current_pos): # needs an if check for if a square has already been visited.
    """ 
    On an n x n matrix board a knight's movements can be represented by addition and subtraction.
    """
    return [(current_pos[0] + move[0], current_pos[1] + move[1]) for move in move_types if (current_pos[0] + move[0], current_pos[1] + move[1]) in all_squares]



# dictionaries for constant time lookups
used = {sqr: False for sqr in all_squares}
available_moves = {sqr: available_moves_from_square(sqr) for sqr in all_squares}


for key in available_moves.keys():
    degree = [(len(available_moves_from_square(available_moves[key][i])), available_moves[key]) for i in range(len(available_moves[key]))]
    degree.sort()
    available_moves[key] = [degree[i][1] for i in range(len(degree))]
# each list in available moves should now be sorted by number of possible moves from that square
    
    

def next_move(square, stack, n, l, used, available_moves):
    l += 1
    stack.append(square)
    if l == n**2:
        return stack, l
    for i in range(len(available_moves[square])):
        if not used[sqr]:
            used[sqr] = True
            if next_move(available[square][i], stack, n, l, used, available_moves)[1] == n**2:
                return stack, l
            used[sqr] = False
    l -= 1
    stack.pop()
            
        
# the big sad has defeated me for tonight
    




print_board([i for i in range(n**2)])
print()
for key, value in available_moves.items():
    print(key, value)
print()
print(next_move((2, 1), n, l, stack, available_moves, used))














# Run this file to use Terminal Tour.
import config as cfg
import Terminal_Tour_Interface as tti
import Terminal_Tour_Recursive as ttr
import Print_Board as pb


def main():
    pb.clear()
    again = True
    tti.greeting()
    while again:
        pb.clear()
        m, n  = tti.get_board_size()
        pb.print_example_board()
        starting_square = tti.get_square(m, n)
        speed = tti.choose_speed()
        
        cfg.num_squares = m*n   
        cfg.l = 0               # the length of stack
        cfg.stack = []          # will keep track of knight moves
        all_squares = [(i,j) for i in range(m) for j in range(n)]
    
        cfg.used = {sqr: False for sqr in all_squares}  # returns True if a square is in the stack
        cfg.possible_moves = {sqr: ttr.available_moves(sqr, all_squares) for sqr in all_squares} 
        
        # sorts possible moves from each square by which square has the least number of possible moves from it (Warnsdorff's algorithm).
        for key in cfg.possible_moves.keys():
            moves = cfg.possible_moves[key]
            degree_moves = [(len(ttr.available_moves(move, all_squares)), move) for move in moves]
            degree_moves.sort()
            cfg.possible_moves[key] = [degree_moves[i][1] for i in range(len(degree_moves))]
        
        # DFS portion
        knight_positions = ttr.next_move(starting_square)[0]
        if not knight_positions:
            print()
            print("A knight's tour could not be calculated for a board with the chosen dimensions.")
        else:
            pb.print_moves(knight_positions, speed, all_squares, n)
            pb.print_final_board(knight_positions, all_squares, cfg.num_squares, n)
        
        again = tti.go_again()

if __name__ == "__main__":
    main()

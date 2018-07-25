"""
Solve edgeless puzzle

A puzzle is specified using 9 squares and for each square each of the 4 sides an identifier used for matching

"""
import board as bd
import piece as pc
import edge as ed

def solve_puzzle(board,piece_queue,idx):
    used_pieces = []
    if len(piece_queue) == 0:
        return True
    piece_match_map = board.board_map[idx]

    while len(piece_queue) > 0:
        #pop single piece 
        piece = piece_queue.pop()
        for ii in range(4):
        #try to place piece in board idx
            if board.add_piece(idx,piece):
                #call next solve puzzle
                #need to include used_pieces as well
                new_piece_queue = piece_queue[:]
                new_piece_queue.extend(used_pieces)
                if solve_puzzle(board,new_piece_queue,idx+1):
                    return True
                else:
                    board.remove_piece(idx)

            piece.rot_clockwise()
        #this shouldn't be nessisary but being doublly sure we always store pieces
        # in rotation = 0 (i.e. original side up)
        piece.rotation = 0
        used_pieces.append(piece)
                    
            
        #    if solve_puzzle returns True, then return True here
        #    else: 
        #if not match or increment fails then rotate and try again
        #if have tried all rotations then push piece to used_pieces
        
    #if we get here we have tried all pieces and we return False
    return False




if __name__ == "__main__":
    import sys
    fname = sys.argv[1]#"cards_definition_easy_solve.txt"
    piece_spec = []
    with open(fname, "r") as fh:
        for line in fh.readlines():
            piece_spec.append([[cc for cc in ed] for ed in line.strip().split(",")])

    for ps in piece_spec:
        print(len(ps),ps)
    
    piece_list = [pc.Piece(ps) for ps in piece_spec]
    piece_list_store = [pc.Piece(ps) for ps in piece_spec]
    board = bd.Board()

    if solve_puzzle(board,piece_list,0):
        
        for ii,piece in enumerate(board.board_list):
            piece_idx = [ii for ii in range(9) if piece_list_store[ii] == piece]
            print(ii,piece.rotation,piece_idx,[[ed.edge_type,ed.edge_dirc] for ed in piece.edge_list])
    

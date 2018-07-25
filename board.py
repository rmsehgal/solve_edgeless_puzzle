

from collections import namedtuple

BOARD_NODE = namedtuple("board_node","square_id, connection_list")
BOARD_EDGE = namedtuple("board_edge","connection_id, connection_side, piece_side")

class Board(object):
    
    
    def __init__(self):
        """
        defining board list and connection map
        
        board_list - list of puzzle pieces
        
        """
        self.board_list = [None]*9
        self.board_map = [BOARD_NODE(0, connection_list = []), \
                          BOARD_NODE(1, connection_list = [BOARD_EDGE(0, 1, 3)]), \
                          BOARD_NODE(2, connection_list = [BOARD_EDGE(1, 1, 3)]), \
                          BOARD_NODE(3, connection_list = [BOARD_EDGE(0, 2, 0)]), \
                          BOARD_NODE(4, connection_list = [BOARD_EDGE(1, 2, 0), BOARD_EDGE(3, 1, 3)]), \
                          BOARD_NODE(5, connection_list = [BOARD_EDGE(2, 2, 0), BOARD_EDGE(4, 1, 3)]), \
                          BOARD_NODE(6, connection_list = [BOARD_EDGE(3, 2, 0)]), \
                          BOARD_NODE(7, connection_list = [BOARD_EDGE(4, 2, 0), BOARD_EDGE(6, 1, 3)]), \
                          BOARD_NODE(8, connection_list = [BOARD_EDGE(5, 2, 0), BOARD_EDGE(7, 1, 3)])]

    def add_piece(self,location,piece):

        if self.board_list[location] is not None:
            raise ValueError("Specified location ({}) is already filled".format(location))


        for edge_spec in self.board_map[location].connection_list:
            piece_edge = piece.get_side(edge_spec.piece_side)
            cur_board_edge = self.board_list[edge_spec.connection_id].get_side(edge_spec.connection_side)
            if not piece_edge.matches(cur_board_edge):
                return False

        self.board_list[location] = piece
        return True
            
    def remove_piece(self,location):
        if self.board_list[location] is None:
            raise ValueError("Specified location ({}) is not filled".format(location))
        tmp_p = self.board_list[location]
        self.board_list[location] = None
        return tmp_p
        

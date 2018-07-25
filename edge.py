"""Edge class definition"""

EDGE_TYPES = ["O", "P", "G", "R"]
EDGE_DIRECTIONS = ["B", "T"]

class Edge():
    """
    Types of edges
    """

    def __init__(self, edge_type_str, edge_dirc_str):
        if edge_type_str in EDGE_TYPES:
            self.edge_type = edge_type_str
        else:
            raise ValueError("Unable to parse edge direction string {}".format(edge_type_str))

        if edge_dirc_str == EDGE_DIRECTIONS[0]:
            self.edge_dirc = 0
        elif edge_dirc_str == EDGE_DIRECTIONS[1]:
            self.edge_dirc = 1
        else:
            raise ValueError("Unable to parse edge direction string {}".format(edge_dirc_str))
        
    def __eq__(self,other):
        return other.edge_type == self.edge_type and other.edge_dirc == self.edge_dirc
    
    def matches(self, other):
        if isinstance(other, Edge):
            if self.edge_type == other.edge_type and self.edge_dirc^other.edge_dirc:
                return True
            else:
                return False
        

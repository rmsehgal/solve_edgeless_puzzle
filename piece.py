"""
Class for edgeless puzzle piece
"""
import edge

class Piece(object):
    """Class defining a single piece in the edgeless puzzle"""
    def __init__(self,edge_spec_list):
        """
        Holds ordered edges
        """
        if len(edge_spec_list) != 4:
            raise(ValueError("Did not specify 4 edges, insted specified {}".format(len(edge_spec_list))))
        self.edge_list = []
        self.rotation = 0

        for ed_spec in edge_spec_list:
            if len(ed_spec) != 2:
                raise(ValueError("Did not specify 2 edge params, instead specified{}".format(len(ed_spec))))
            self.edge_list.append(edge.Edge(ed_spec[0],ed_spec[1]))
        
    def __eq__(self,other):
        return all([se==oe for se,oe in zip(self.edge_list,other.edge_list)])
        
    def get_side(self,side_number):
        """
        Get an edge under current rotation:
        side_number:
           0 - top
           1 - right
           2 - bottom
           3 - left
        """
        return self.edge_list[(side_number-self.rotation)%len(self.edge_list)]

    def rot_clockwise(self):
        self.rotation = (self.rotation+1)%(len(self.edge_list))

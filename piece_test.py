"""All unit tests for piece class"""
import unittest
import piece as pc
import edge as ed


class PieceTest(unittest.TestCase):
    """All unittests for piece class"""
    def test_not_enough_edges_specd(self):
        """
        Unit test to check that correct number
        of edges are specified
        """
        piece_spec = [["P", "T"], \
                      ["R", "B"], \
                      ["O", "B"]]#, \
                      #["G", "T"]]
        with self.assertRaises(ValueError):
            pc.Piece(piece_spec)
            
    def test_not_edges_specd_wrong(self):
        """
        Unit test to check that edges are 
        properly specified
        """
        piece_spec = [["P", "T"], \
                      ["R", "B"], \
                      ["O"], \
                      ["G", "T"]]
        with self.assertRaises(ValueError):
            pc.Piece(piece_spec)

    def test_get_edge_eq(self):
        """
        Unit test to check that edges are 
        properly specified
        """
        piece_spec = [["P", "T"], \
                      ["R", "B"], \
                      ["O", "B"], \
                      ["G", "T"]]
        
        piece1 = pc.Piece(piece_spec)
        piece2 = pc.Piece(piece_spec)
        self.assertTrue(piece1==piece2)

    def test_get_edges(self):
        """
        Unit test to check that edges are 
        properly specified
        """
        piece_spec = [["P", "T"], \
                      ["R", "B"], \
                      ["O", "B"], \
                      ["G", "T"]]
        
        piece = pc.Piece(piece_spec)
        edge = ed.Edge(piece_spec[3][0],piece_spec[3][1])
        self.assertEqual(piece.get_side(3).edge_type,edge.edge_type)
        self.assertEqual(piece.get_side(3).edge_dirc,edge.edge_dirc)



    def test_do_rotation(self):
        """
        Unit test to check that rotation works
        properly
        """
        piece_spec = [["P", "T"], \
                      ["R", "B"], \
                      ["O", "B"], \
                      ["G", "T"]]
        
        piece = pc.Piece(piece_spec)
        piece.rot_clockwise()
        edge = ed.Edge(piece_spec[3][0],piece_spec[3][1])
        self.assertEqual(piece.get_side(0).edge_type,edge.edge_type)
        self.assertEqual(piece.get_side(0).edge_dirc,edge.edge_dirc)

            
        
if __name__ == "__main__":
    unittest.main()

"""All unit tests for board class"""
import unittest
import piece as pc
import board as bd


class BoardTest(unittest.TestCase):
    """All unit tests for board class"""

    def test_add_first_board_piece(self):
        """
        Unit test to ensure a piece can be added 
        to the first empty spot in the board
        """

        piece_spec = [["P", "T"], \
                      ["R", "B"], \
                      ["O", "B"], \
                      ["G", "T"]]

        piece = pc.Piece(piece_spec)
        board = bd.Board()

        board.add_piece(0,piece)
        self.assertEqual(board.board_list[0],piece)


    def test_add_second_board_piece_no_match(self):
        """
        Unit test to ensure an incorrect piece 
        cannot be added to the second spot
        """

        piece1 = pc.Piece([["P", "T"], \
                           ["R", "B"], \
                           ["O", "B"], \
                           ["G", "T"]])

        piece2 = pc.Piece([["P", "T"], \
                           ["R", "B"], \
                           ["O", "B"], \
                           ["G", "T"]])

        board = bd.Board()

        board.add_piece(0,piece1)
        self.assertFalse(board.add_piece(1,piece2))

    def test_add_second_board_piece_match(self):
        """
        Unit test to ensure a correct second 
        piece can be added to the board
        """

        piece1 = pc.Piece([["P", "T"], \
                           ["R", "B"], \
                           ["O", "B"], \
                           ["G", "T"]])

        piece2 = pc.Piece([["P", "T"], \
                           ["R", "B"], \
                           ["O", "B"], \
                           ["R", "T"]])

        board = bd.Board()

        board.add_piece(0,piece1)
        self.assertTrue(board.add_piece(1,piece2))


if __name__ == "__main__":
    unittest.main()

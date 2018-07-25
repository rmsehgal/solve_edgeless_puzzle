"""All unit tests for edge class"""
import unittest
import edge as ed


class EdgeTest(unittest.TestCase):
    """All unittests for edge """
    def test_edge_type_spec(self):
        """
        Unit test to check that edge
        specification is parseable
        """
        with self.assertRaises(ValueError):
            ed.Edge("Q","T")
        

    def test_edge_dirc_spec(self):
        """
        Unit test to check that edge
        specification is parseable
        """
        with self.assertRaises(ValueError):
            ed.Edge("O","1")

    def test_edge_eq(self):
        """
        Unit test to check that edge match
        is correct
        """
        e1 = ed.Edge("O","B")
        e2 = ed.Edge("O","B")
        self.assertTrue(e1==e2)

    def test_edge_neq(self):
        """
        Unit test to check that edge match
        is correct
        """
        e1 = ed.Edge("O","B")
        e2 = ed.Edge("O","T")
        self.assertFalse(e1==e2)

    def test_edge_match(self):
        """
        Unit test to check that edge match
        is correct
        """
        e1 = ed.Edge("O","B")
        e2 = ed.Edge("O","T")
        self.assertTrue(e1.matches(e2))


    def test_edge_not_match_direction(self):
        """
        Unit test to check that edge match
        catches edge direction not matching
        """
        e1 = ed.Edge("O","B")
        e2 = ed.Edge("O","B")
        self.assertFalse(e1.matches(e2))


    def test_edge_not_match_type(self):
        """
        Unit test to check that edge match
        catches edge type not matching
        """
        e1 = ed.Edge("O","B")
        e2 = ed.Edge("P","T")
        self.assertFalse(e1.matches(e2))

        
if __name__ == "__main__":
    unittest.main()

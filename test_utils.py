#!/usr/bin/env python3

import sys
import unittest
import io

from utils import Point, Line, Vertices, Edges, Graph, is_intersect, intersect, point_on_edge

class test_point(unittest.TestCase):

    def test_eq(self):
        """Test the eq function of class Point"""
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertNotEqual(Point(1, 2), Point(2, 1))
        self.assertNotEqual(Point(1, 2), Point(1, 1))
        self.assertEqual(Point(1, 2), Point(1.0, 2.0))
        self.assertNotEqual(Point(1, 2), Point(1.0, 1.0))

    def test_repr(self):
        
        """Test repr function of class Point"""
        capturedOutput = io.StringIO()                         # Create StringIO object
        sys.stdout = capturedOutput                            # and redirect stdout.
        print(Point(1, 2))                                     # Call unchanged function.
        sys.stdout = sys.__stdout__                            # Reset redirect.
        assert capturedOutput.getvalue() == "(1, 2)\n"         # Now works as before.
        
        """Test repr function of class Point"""
        capturedOutput = io.StringIO()                         # Create StringIO object
        sys.stdout = capturedOutput                            # and redirect stdout.
        print(Point(1.0, 2.0))                                 # Call unchanged function.
        sys.stdout = sys.__stdout__                            # Reset redirect.
        assert capturedOutput.getvalue() == "(1, 2)\n"         # Now works as before.
        
        """Test repr function of class Point"""
        capturedOutput = io.StringIO()                         # Create StringIO object
        sys.stdout = capturedOutput                            #  and redirect stdout.
        print(Point(1.1234, 2.234))                            # Call unchanged function.
        sys.stdout = sys.__stdout__                            # Reset redirect.
        assert capturedOutput.getvalue() == "(1.12, 2.23)\n"   # Now works as before.


class test_line(unittest.TestCase):

    def test_eq(self):

        """Test the eq function of class Line"""
        assert Line(Point(1, 2), Point(3, 4)) == Line(Point(1, 2), Point(3, 4))
        assert Line(Point(1, 2), Point(3, 4)) == Line(Point(3, 4), Point(1, 2))
        assert Line(Point(1, 2), Point(3, 4)) != Line(Point(1, 2), Point(4, 3))
        assert Line(Point(1, 2), Point(3, 4)) != Line(Point(2, 1), Point(3, 4))
        assert Line(1, 2) == Line(1, 2)
        assert Line(1, 2) == Line(2, 1)
        assert Line(1, 2) != Line(1, 3)
        assert Line(1, 2) != Line(3, 2)

    def test_repr(self):

        """Test repr function of class Line"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Line(1, 2))                               # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "<1, 2>\n"  # Now works as before.

        """Test repr function of class Line"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Line(1.0, 2.0))                           # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "<1, 2>\n"  # Now works as before.

        """Test repr function of class Line"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Line(1.000001, 1.99999))                  # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "<1, 2>\n"  # Now works as before.


class test_vertices(unittest.TestCase):

    def test_repr(self):

        """Test repr function of class Vertices"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Vertices([Point(1, 2), Point(3, 4)]))     # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "V = {\n0: (1, 2)\n1: (3, 4)\n}\n"  # Now works as before.

        """Test repr function of class Vertices"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Vertices([Point(2.0, 1.0), Point(3, 4)]))     # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "V = {\n0: (2, 1)\n1: (3, 4)\n}\n"  # Now works as before.
        
        """Test repr function of class Vertices"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Vertices([Point(1.99999999, 2.000001), Point(3, 4)]))     # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "V = {\n0: (2, 2)\n1: (3, 4)\n}\n"  # Now works as before.


class test_edges(unittest.TestCase):

    def test_repr(self):

        """Test repr function of class Edges"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Edges([Line(1, 2), Line(3, 4)]))                  # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "E = {\n0: <1, 2>\n1: <3, 4>\n}\n"  # Now works as before.

        """Test repr function of class Edges"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Edges([Line(1.0, 2.0), Line(3, 4)]))                  # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "E = {\n0: <1, 2>\n1: <3, 4>\n}\n"  # Now works as before.

        """Test repr function of class Edges"""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     # and redirect stdout.
        print(Edges([Line(1.99999999, 2.000001), Line(3, 4)]))                  # Call unchanged function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        assert capturedOutput.getvalue() == "E = {\n0: <2, 2>\n1: <3, 4>\n}\n"  # Now works as before.


class test_graph(unittest.TestCase):

    def test_op(self):

        """test the operation of class Graph"""
        """add(), get(), modify(), remove()"""
        """gg() is left for afterwards testing"""
        
        # add operations
        g = Graph()
        g.add("st 1", [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(1, 2)])
        g.add("st 2", [Point(2, 1), Point(4, 3), Point(6, 5), Point(8, 7), Point(2, 1)])
        g.add("st 3", [Point(3, 2), Point(5, 4), Point(7, 6), Point(9, 8), Point(2, 2)])
        g.add("st 4", [Point(4.2, 3.3), Point(6.5, 5.5), Point(8.6, 7.8), Point(10.2, 9.5), Point(2.2, 3.0)])
        self.assertRaisesRegexp(Exception, "Error: Street name already exists", g.add, "st 1", [Point(1, 2), Point(3, 4)])

        # get operations
        self.assertEqual(g.get("st 1"), [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(1, 2)])
        self.assertRaisesRegexp(Exception, "Error: Street name does not exist", g.get, "st 5")

        # modify operations
        g.modify("st 1", [Point(2,3), Point(4,5), Point(6,7), Point(8,9), Point(2,3)])
        assert g.get("st 1") == [Point(2,3), Point(4,5), Point(6,7), Point(8,9), Point(2,3)]
        self.assertRaisesRegexp(Exception, "Error: Street name does not exist", g.modify, "st 5", [Point(1, 2), Point(3, 4)])

        # remove operations
        g.remove("st 1")
        self.assertRaisesRegexp(Exception, "Error: Street name does not exist", g.remove, "st 5")
        self.assertRaisesRegexp(Exception, "Error: Street name does not exist", g.get, "st 1")


class test_method(unittest.TestCase):

    def test_intersect(self):

        assert is_intersect(Line(Point(1, 1), Point(2, 2)), Line(Point(1, 2), Point(2, 1))) == True
        assert is_intersect(Line(Point(1, 1), Point(2, 2)), Line(Point(1, 2), Point(2, 3))) == False
        assert is_intersect(Line(Point(1, 1), Point(2, 2)), Line(Point(1, 2), Point(3, 4))) == False
        assert is_intersect(Line(Point(1, 1), Point(2, 2)), Line(Point(3, 3), Point(2, 2))) == True
        assert is_intersect(Line(Point(0, 0), Point(0, 1)), Line(Point(-1, 1), Point(1, 1))) == True

        assert intersect(Line(Point(1, 1), Point(2, 2)), Line(Point(1, 2), Point(2, 1))) == Point(1.5, 1.5)
        assert intersect(Line(Point(1, 1), Point(2, 2)), Line(Point(2, 2), Point(3, 3))) == Point(2, 2)
        assert intersect(Line(Point(0, 0), Point(0, 1)), Line(Point(-1, 1), Point(1, 1))) == Point(0, 1)
        assert intersect(Line(Point(-1, 1), Point(1, 1)), Line(Point(0, 0), Point(0, 1))) == Point(0, 1)


    def test_point_on_edge(self):

        assert point_on_edge(Point(1, 1), Line(Point(1, 1), Point(2, 2))) == False
        assert point_on_edge(Point(2, 2), Line(Point(1, 1), Point(2, 2))) == False
        assert point_on_edge(Point(1.5, 1.5), Line(Point(1, 1), Point(2, 2))) == True
    


if __name__ == '__main__':
    unittest.main()

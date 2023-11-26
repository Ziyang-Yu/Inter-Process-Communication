#!/usr/bin/env python3

import sys
import unittest
import io

from utils import Point, Line, Vertices, Edges, Graph, is_intersect
from input import legal, _seq_legal, _int_legal, _st_legal, _add_legal, _mod_legal, _rm_legal

class test_legal(unittest.TestCase):

    def test_seq_legal(self):
        
        bol, msg = _seq_legal("(2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == [Point(2, 3), Point(4, 5), Point(6, 7)]

        bol, msg = _seq_legal("2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _seq_legal("(2, 3 (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _seq_legal("(2, 3), (4, 5), (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _seq_legal("(2%%!%!FFASF, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _seq_legal("(2, 3)@%!#@F##@ (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _seq_legal("(2, 3) (4, 5) (6, 7)$@!$!$@!")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _seq_legal("(2, 3) (-4, 5) (-6, 7)")
        assert bol == True
        assert msg == [Point(2, 3), Point(-4, 5), Point(-6, 7)]

    
    def test_int_legal(self):

        bol, msg = _int_legal("21512")
        assert bol == True
        assert msg == 21512

        bol, msg = _int_legal("-21512")
        assert bol == True
        assert msg == -21512

        bol, msg = _int_legal("21512.0")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _int_legal("-21512.0")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _int_legal("21512#%!5")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _int_legal("-21512.1")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _int_legal("21512.1")
        assert bol == False
        assert msg.startswith("Error")


    def test_st_legal(self):

        bol, msg = _st_legal("\"st 1\" (2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == "st 1"

        bol, msg = _st_legal("\"st 1\"(2, 3) (4^#$&#, 5) (6, 7)")
        assert bol == True
        assert msg == "st 1"

        bol, msg = _st_legal("\"st\"#%@\" 1\"(2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == "st\"#%@\" 1"

        bol, msg = _st_legal("\"st 1 (2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _st_legal("st 1\"(2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

    
    def test_add_legal(self):

        bol, msg = _add_legal("\"st 1\" (2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == ["add", "st 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = _add_legal("\"st 1\"(2, 3) (4^#$&#, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _add_legal("\"st\"#%@\" 1\"(2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == ["add", "st\"#%@\" 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = _add_legal("\"st 1 (2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _add_legal("st 1\"(2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _add_legal("\"st 1\" (2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")


    def test_mod_legal(self):

        bol, msg = _mod_legal("\"st 1\" (2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == ["mod", "st 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = _mod_legal("\"st 1\"(2, 3) (4^#$&#, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _mod_legal("\"st\"#%@\" 1\"(2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == ["mod", "st\"#%@\" 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = _mod_legal("\"st 1 (2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _mod_legal("st 1\"(2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _mod_legal("\"st 1\" (2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")


    def test_rm_legal(self):

        bol, msg = _rm_legal("\"st 1\"")
        assert bol == True
        assert msg == ["rm", "st 1"]

        bol, msg = _rm_legal("\"st 1\" %$FV  ")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _rm_legal("\"st 1\"   ")
        assert bol == True
        assert msg == ["rm", "st 1"]

        bol, msg = _rm_legal("\"st 1\"(2, 3) (4^#$&#, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _rm_legal("\"st\"#%@\" 1\"(2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _rm_legal("\"st 1 (2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _rm_legal("st 1\"(2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = _rm_legal("\"st 1\" (2, 3) (4, 5) (6, 7)\"")
        assert bol == True
        assert msg == ["rm", "st 1\" (2, 3) (4, 5) (6, 7)"]


    def test_legal(self):

        bol, msg = legal("add \"st 1\" (2, 3) (4, 5) (6, 7)")
        print(msg)
        assert bol == True
        assert msg == ["add", "st 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = legal("add \"st 1\"(2, 3) (4^#$&#, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("add \"st\"#%@\" 1\"(2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == ["add", "st\"#%@\" 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = legal("add \"st 1 (2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("add st 1\"(2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("add \"st 1\" (2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("mod \"st 1\" (2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == ["mod", "st 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = legal("mod \"st 1\"(2, 3) (4^#$&#, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("mod \"st\"#%@\" 1\"(2, 3) (4, 5) (6, 7)")
        assert bol == True
        assert msg == ["mod", "st\"#%@\" 1", [Point(2, 3), Point(4, 5), Point(6, 7)]]

        bol, msg = legal("mod \"st 1 (2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("mod st 1\"(2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("mod \"st 1\" (2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("rm \"st 1\"")
        assert bol == True
        assert msg == ["rm", "st 1"]

        bol, msg = legal("rm \"st 1\" %$FV  ")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("rm \"st 1\"   ")
        assert bol == True
        assert msg == ["rm", "st 1"]

        bol, msg = legal("rm \"st 1\"(2, 3) (4^#$&#, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("rm \"st\"#%@\" 1\"(2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("rm \"st 1 (2, 3) (4, 5) (6, 7)")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("rm st 1\"(2, 3) (4, 5) (6, 7)\"")
        assert bol == False
        assert msg.startswith("Error")

        bol, msg = legal("rm \"st 1\" (2, 3) (4, 5) (6, 7)\"")
        assert bol == True
        assert msg == ["rm", "st 1\" (2, 3) (4, 5) (6, 7)"]

        bol, msg = legal("gg")
        assert bol == True
        assert msg == ["gg"]

        bol, msg = legal("gg ")
        assert bol == True
        assert msg == ["gg"]

        bol, msg = legal("gG  ")
        assert bol == False
        assert msg.startswith("Error")


    def test_gg_legal(self):
        bol, msg = legal("  gg  ")
        assert bol == True
        assert msg == ["gg"]

        bol, msg = legal("gg ")
        assert bol == True
        assert msg == ["gg"]

        bol, msg = legal("gG  ")
        assert bol == False
        assert msg.startswith("Error")

if __name__ == '__main__':
    unittest.main()



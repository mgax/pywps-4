import os
import sys

pywpsPath = os.path.abspath(os.path.join(os.path.split(os.path.abspath(__file__))[0],"..",".."))
sys.path.insert(0,pywpsPath)
sys.path.append(pywpsPath)

import unittest

from pywps.process.inout import *

class RequestInputTestCase(unittest.TestCase):
    """Test case for input parsing - tests, if the parser finds the propper
    input, based on it's identifier"""
    
    inpt = None

    def setUp(self):
        self.inpt = Input("idn")

    def test_set_from_url_literal(self):
        pass
    def test_set_from_url_compex(self):
        pass
    def test_set_from_url_bbox(self):
        pass

    def test_set_from_node_literal(self):
        pass
    def test_set_from_node_compex(self):
        pass
    def test_set_from_node_bbox(self):
        pass

def main():
   suite = unittest.TestLoader().loadTestsFromTestCase(RequestInputTestCase)
   unittest.TextTestRunner(verbosity=4).run(suite)

if __name__ == "__main__":
    main()


import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.mgtDryads import mgtDryads

value = list(mgtDryads.nameGen())

class mgtDryads(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()


import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.mgtCephalids import mgtCephalids

value = list(mgtCephalids.nameGen())

class mgtCephalids(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

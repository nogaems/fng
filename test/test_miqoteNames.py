
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.miqoteNames import miqoteNames

value = list(miqoteNames.nameGen())

class miqoteNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

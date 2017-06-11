
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.dndGenasi import dndGenasi

value = list(dndGenasi.nameGen())

class dndGenasi(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

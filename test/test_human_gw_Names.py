
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.human_gw_Names import human_gw_Names

value = list(human_gw_Names.nameGen())

class human_gw_Names(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

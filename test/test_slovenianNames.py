
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.slovenianNames import slovenianNames

value = list(slovenianNames.nameGen())

class slovenianNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

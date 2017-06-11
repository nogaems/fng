
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.apocalypseNames import apocalypseNames

value = list(apocalypseNames.nameGen())

class apocalypseNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

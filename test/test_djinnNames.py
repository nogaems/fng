
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.djinnNames import djinnNames

value = list(djinnNames.nameGen())

class djinnNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

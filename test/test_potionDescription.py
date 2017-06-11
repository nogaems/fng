
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.potionDescription import potionDescription

value = list(potionDescription.nameGen())

class potionDescription(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

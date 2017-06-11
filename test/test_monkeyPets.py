
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.monkeyPets import monkeyPets

value = list(monkeyPets.nameGen())

class monkeyPets(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

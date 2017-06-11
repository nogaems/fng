
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.professions import professions

value = list(professions.nameGen())

class professions(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

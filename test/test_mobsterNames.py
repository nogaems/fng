
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.mobsterNames import mobsterNames

value = list(mobsterNames.nameGen())

class mobsterNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()


import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.jamaicanNames import jamaicanNames

value = list(jamaicanNames.nameGen())

class jamaicanNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

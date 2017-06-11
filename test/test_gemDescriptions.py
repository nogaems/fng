
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.gemDescriptions import gemDescriptions

value = list(gemDescriptions.nameGen())

class gemDescriptions(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

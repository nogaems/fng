
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.toolNicknames import toolNicknames

value = list(toolNicknames.nameGen())

class toolNicknames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

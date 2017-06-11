
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.mermaidNames import mermaidNames

value = list(mermaidNames.nameGen())

class mermaidNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

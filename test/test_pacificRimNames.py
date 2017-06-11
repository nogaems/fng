
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.pacificRimNames import pacificRimNames

value = list(pacificRimNames.nameGen())

class pacificRimNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

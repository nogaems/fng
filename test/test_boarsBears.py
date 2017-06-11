
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.boarsBears import boarsBears

value = list(boarsBears.nameGen())

class boarsBears(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()


import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.mgtAvatars import mgtAvatars

value = list(mgtAvatars.nameGen())

class mgtAvatars(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

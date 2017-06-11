
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.warhammerSkaven import warhammerSkaven

value = list(warhammerSkaven.nameGen())

class warhammerSkaven(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

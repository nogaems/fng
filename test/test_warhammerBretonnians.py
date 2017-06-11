
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.warhammerBretonnians import warhammerBretonnians

value = list(warhammerBretonnians.nameGen())

class warhammerBretonnians(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

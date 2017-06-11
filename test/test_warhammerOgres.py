
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.warhammerOgres import warhammerOgres

value = list(warhammerOgres.nameGen())

class warhammerOgres(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

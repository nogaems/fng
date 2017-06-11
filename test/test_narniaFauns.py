
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.narniaFauns import narniaFauns

value = list(narniaFauns.nameGen())

class narniaFauns(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()

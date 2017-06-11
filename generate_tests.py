import os
generators = [name.split('.')[0] for name in os.listdir(
    'generators') if os.path.isfile('generators/' + name) and
    not name.startswith('_')]

code = '''
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.{name} import {name}

value = list({name}.nameGen())

class {name}(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
'''

if not os.path.isdir('test'):
    os.mkdir('test')
for g in generators:
    f = open('test/test_{}.py'.format(g), 'w')
    f.write(code.format(name=g))
    f.close()

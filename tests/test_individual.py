import unittest
import inspect

from drhtaxes import individual
from drhtaxes.individual import Tax

class ApplicationTests(unittest.TestCase):
    def test_individual(self):
        self.assertTrue(inspect.ismodule(individual))

    def test_tax_calc(self):
        t = Tax()
        self.assertEqual(t.calc_tax(9000),0)


if __name__ == '__main__':
    unittest.main()


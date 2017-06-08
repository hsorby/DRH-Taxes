import unittest
import inspect

from drhtaxes.admission import tax_input_checker
from drhtaxes import admission

class inputCheckerTests(unittest.TestCase):

    def test_float(self):
        self.assertTrue(tax_input_checker('9.000'))

    def test_bad_float(self):
        self.assertFalse(tax_input_checker('9..00'))
    
if __name__ == '__main__':
    unittest.main()


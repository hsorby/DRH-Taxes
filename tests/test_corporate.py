import unittest
import inspect

from drhtaxes import corporate
from drhtaxes.corporate import COR


class ApplicationTests(unittest.TestCase):
    """
    Testing class_COR
    """
    
    def test_class_COR(self):
        """
        Testing function_corp
        """
        tax = COR()
        print(tax.corp(79000, 0))
        self.assertEqual(15800, tax.corp(79000, 0))
        #self.assertTrue(tax.corp(79000,0) == 15800)
        self.assertEqual(16980, tax.corp(85000,100))


if __name__ == '__main__':
    unittest.main()


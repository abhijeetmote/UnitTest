import unittest
from MyString import MyString
import pdb
import sys
class TestStringMethods(unittest.TestCase):
        
    def setUp(self):
        self.obj = MyString("abhijeet")
        self.obj1 = MyString("abhijeet")

    # @unittest.skip("demonstrating skipping")
    def test_upper(self):   
        self.assertEqual(self.obj.upper(),"ABHIJEET")
        self.assertTrue(self.obj1.upper())
        self.assertTrue(isinstance(self.obj1.var, str))

    @unittest.skipUnless(sys.platform.startswith("lin"), "requires Linux")
    def test_windows_support(self):
        # os specific testing code
        pass
        
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
                
    def tearDown(self):
        self.obj = None
        
if __name__ =="__main__":
    unittest.main()

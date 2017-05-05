############################################################
## API : Test_dir_Validation
## It validates all the dir and file related validation
## such as dir is empty,dir does not exist, 
## file not exist, get the count of files, get the size of dir
## Author : Abhijeet Mote
############################################################

import unittest
from Test_Dir_Validation import TestDir
from Test_Date_Validation import TestDate
class DirTestSuite(unittest.TestSuite):
    """A test suite for Dir objects."""
    def __init__(self):
        super(DirTestSuite, self).__init__()

        # ---- add test cases for dir, path, file
        self.addTest(TestDir('test_set_path'))
        self.addTest(TestDir('test_dir_exists'))
        self.addTest(TestDir('test_not_existing_dir'))
        self.addTest(TestDir('test_get_size'))
        self.addTest(TestDir('test_get_size_not_existing_dir'))
        self.addTest(TestDir('test_empty_dir_raises'))
        self.addTest(TestDir('test_dir_not_found_raises'))
        self.addTest(TestDir('test_get_size_in_unit'))
        self.addTest(TestDir('test_get_file_list'))
        self.addTest(TestDir('test_get_file_count'))
        self.addTest(TestDir('test_get_path'))

        # --- add test cases fro date
        #self.addTest(TestDir('test_get_path'))


if __name__ == "__main__": 
    #unittest.main()
    unittest.TextTestRunner(verbosity=2).run(DirTestSuite())

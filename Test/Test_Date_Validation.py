############################################################
## API : Test_dir_Validation
## It validates all the dir and file related validation
## such as dir is empty,dir does not exist, 
## file not exist, get the count of files, get the size of dir
## Author : Abhijeet Mote
############################################################


import unittest
import sys,os
sys.path.insert(1, '../Date')
from Date import *
class TestDate(unittest.TestCase):

    # Initilizing 
    def setUp(self): 
        self.date_obj = Date()

    

    def tearDown(self):
        self.date_obj = None

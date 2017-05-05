############################################################
## API : Test_dir_Validation
## It validates all the dir and file related validation
## such as dir is empty,dir does not exist, 
## file not exist, get the count of files, get the size of dir
## Author : Abhijeet Mote
############################################################


import unittest
import sys,os
sys.path.insert(1, '../Directory')
from Cls import Dir_validation
from custom_error import DirectoryEmpty, DirNotFound, NotDir
class TestDir(unittest.TestCase):

    # Initilizing 
    def setUp(self):
        self.dir_obj = Dir_validation(unit='mb')
        self.dir_obj.exist_dir = (
                            ("/home/abhijeet/449/"),
                            ("/home/abhijeet/AST/"),
                            ("/home/abhijeet/bin/")
                     )
        self.dir_obj.non_exist_dir = (
                            ("/home/abhijeet/123/"),
                            ("/home/abhijeet/d d/"),
                            ("/home/abhijeet/asdf/")
                     )
    
    def test_set_path(self):

        for index in self.dir_obj.exist_dir:
            self.dir_obj.set_path(index)
            #self.assertEqual(self.dir_obj.path,"/home/abhijeet/449/")
        # self.dir_obj.set_path("/home/abhijeet/UnitTest/asdf")
        # self.assertEqual(,"/home/abhijeet/UnitTest/asdf")

            
    def test_dir_exists(self):
        # test for existing directory 
        for index in self.dir_obj.exist_dir:
            self.dir_obj.set_path(index)
            self.assertTrue(self.dir_obj.dir_exists())

    def test_not_existing_dir(self):
        # test for non existing directory 
        for index in self.dir_obj.non_exist_dir:
            self.dir_obj.set_path(index)
            self.assertFalse(self.dir_obj.dir_exists())  

            
    def test_get_size(self):
        # Test for existing directory, get the the size of it
        for index in self.dir_obj.exist_dir:
            self.dir_obj.set_path(index)
            self.assertTrue(isinstance(self.dir_obj.get_size(), int))
            self.assertGreaterEqual(self.dir_obj.get_size(),0)
            self.assertTrue(isinstance(self.dir_obj.get_size, object))

    def test_get_size_not_existing_dir(self):
        # Test for non existing directory
        for index in self.dir_obj.non_exist_dir:
            self.dir_obj.set_path(index)
            self.assertFalse(self.dir_obj.dir_exists())
            self.assertTrue(isinstance(self.dir_obj.dir_exists, object))

    def test_empty_dir_raises(self):
        self.dir_obj.set_path("/home/abhijeet/UnitTest/asdf")
        self.assertRaises(DirectoryEmpty, self.dir_obj.get_size)

    def test_dir_not_found_raises(self):
        self.dir_obj.set_path("/home/asdf")
        self.assertRaises(DirNotFound, self.dir_obj.get_size)        

    def test_get_size_in_unit(self):
        # for non existing dir
        self.dir_obj.set_path("/home/abhijeet/UnitTest/abhijeet")
        self.assertTrue(isinstance(self.dir_obj.get_size_in_unit(), str))
        self.assertGreaterEqual(self.dir_obj.get_size_in_unit(),0)        
        self.assertTrue(isinstance(self.dir_obj.get_size_in_unit, object))

    def test_get_file_list(self):
        self.dir_obj.set_path("/home/abhijeet/UnitTest/aasdf")
        self.assertRaises(DirNotFound, self.dir_obj.get_file_list)
        self.dir_obj.set_path("/home/abhijeet/UnitTest/Read.txt")
        self.assertRaises(NotDir, self.dir_obj.get_file_list)
        self.dir_obj.set_path("/home/abhijeet/UnitTest/asdf")
        self.assertRaises(DirectoryEmpty, self.dir_obj.get_file_list)
        # self.assertTrue(isinstance(self.dir_obj.get_file_list(), list))
        # self.assertGreaterEqual(len(self.dir_obj.get_file_list()),0)
        self.assertTrue(isinstance(self.dir_obj.get_file_list, object))

    def test_get_file_count(self):
        self.dir_obj.set_path("/home/abhijeet/UnitTest/aasdf")
        self.assertRaises(DirNotFound, self.dir_obj.get_file_list)
        self.dir_obj.set_path("/home/abhijeet/UnitTest/Read.txt")
        self.assertRaises(NotDir, self.dir_obj.get_file_list)
        self.dir_obj.set_path("/home/abhijeet/UnitTest/abhijeet")
        self.assertTrue(isinstance(self.dir_obj.get_file_count(), int))
        self.assertGreaterEqual(self.dir_obj.get_file_count(),0)
        self.assertTrue(isinstance(self.dir_obj.get_file_count, object))

    def test_get_path(self):
        self.dir_obj.set_path("/home/abhijeet/UnitTest/abhijeet")        
        self.assertTrue(isinstance(self.dir_obj.get_path, object))


    def tearDown(self):
        self.dir_obj = None

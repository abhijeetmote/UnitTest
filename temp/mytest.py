#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import RemovalService
import unittest
from unittest import mock


class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        
        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("/home/abhijeet/UnitTest/abhijeet/")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        print(mock_os.remove.called)
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        reference.rm("/home/abhijeet/UnitTest/abhijeet/")
        print(mock_os.remove.called)
        mock_os.remove.assert_called_with("/home/abhijeet/UnitTest/abhijeet/")        


if __name__ == '__main__':
    unittest.main()
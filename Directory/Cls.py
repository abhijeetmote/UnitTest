import os
from os import listdir
from os.path import isfile, join
from custom_error import Error, DirNotFound, DirectoryEmpty, NotDir


class Dir_validation(object):
    def __init__(self, path=None, unit = None):
        self.path = path
        #self.schema = schema
        #self.folder_date = folder_date
        self.unit = unit 


    def set_path(self, path):
        # Before setting any value please validate then there wont be possible errors in post of this code 
        # suggestion by abhijeet
        self.path = path        

    def set_unit(self, unit):
        self.unit = unit

    def dir_exists(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

    def get_size(self):
        if self.dir_exists(): # this if statement accepting only True value but not False value
            if len(listdir(self.path)) > 0:
                total_size = 0
                for dirpath, dirnames, filenames in os.walk(self.path):
                    for f in filenames:
                        fp = os.path.join(dirpath, f)
                        total_size += os.path.getsize(fp)
                return total_size
            else:
                raise DirectoryEmpty('The Given directory is empty and does not contain any subdirectory or files. ')
        
        #this else statement never have been called in case first if statement is not true
        else:
            raise DirNotFound('The provided directory path does not exist!! Please check the path provided ')

    def get_size_in_unit(self):
        ## Function does no work when we did not pass prarameter of unit while creating the object. 
        ## Validate whether the unit is given ???? suggestion by abhijeet
        ## This function takes too much of time it iterates through all files present in dir,
        ## If list of files is more then it consumes more time 
        size = self.get_size()        
        unit = (self.unit).upper()
        accepted_units = ['KB', 'MB', 'GB', 'TB', 'PB'] # the units may be in lower case letters.
        if unit == 'B': return size, 'B'
        for x in accepted_units:
            size = size/1024.0
            if x == unit:
                break
        return str(size) + unit

    def get_file_list(self):
        if self.dir_exists(): # this if statement accepting only True value but not False value
            if os.path.isdir(self.path):
                if len(listdir(self.path)) > 0:
                    only_files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
                    return only_files
                else:
                    raise DirectoryEmpty('The Given directory is empty and does not contain any subdirectory or files. ')
            else:
                raise NotDir('Given path does not belong to a directory, but to a file!! ')
        
        #this else statement never have been called in case first if statement is not true
        else:
            raise DirNotFound('The provided directory path does not exist!! Please check the path provided')


    def get_file_count(self):
        if self.dir_exists(): # this if statement accepting only True value but not False value
            if os.path.isdir(self.path):
                count_files = len(self.get_file_list())
                return count_files
            else:
                raise NotDir('Given path does not belong to a directory, but to a file!! ')
 
         #this else statement never have been called in case first if statement is not true
        else:
            raise DirNotFound('The provided directory path does not exist!! Please check the path provided')

    
    def get_path(self):
        return self.path
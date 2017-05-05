

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class DirNotFound(Error):
   pass


class DirectoryEmpty(Error):
   pass


class NotDir(Error):
   pass


class MyString(object):

    def __init__(self,var):
        self.var = var

    def upper(self):
        return self.var.upper()
        
    def split(self):
        return self.var.split(" ")
    
    
if __name__ == "__main__":
    strobj = MyString("abhijeet mote")
    print strobj.upper()
    print strobj.split()

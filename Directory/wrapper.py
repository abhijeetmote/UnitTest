
from Cls import Dir_validation
import argparse
import pdb


obj = Dir_validation()
parser = argparse.ArgumentParser(description='This is sample code')

parser.add_argument('-a', action="store", dest='path')
parser.add_argument('-b', action="store", dest='unit')
#parser.add_argument('-c', action="store", dest='folder_date', type=int)

args = parser.parse_args()

obj.set_path(args.path)
obj.set_unit(args.unit)
#obj.set_folder_date(args.folder_date)

pdb.set_trace()
print obj.get_path()
print obj.get_size_in_unit()
#print obj.get_folder_date()

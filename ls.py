import sys
import os

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print(arg1)
files = os.listdir(os.curdir)
print(files)



from os import listdir
from os.path import isfile, join
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# print("%1")
# print("%2")
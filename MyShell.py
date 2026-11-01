
import subprocess
from subprocess import Popen
# p = Popen("ls.bat")
# stdout, stderr = p.communicate()

#
# import os
# os.system("ls.bat param1 param2")


folder_name = input("Enter folder name")


subprocess.call("ls.bat folder_name")
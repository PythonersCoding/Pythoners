import shutil
import os
#task 3
__author = "Pythoners"

f = str(input("enter the file u want to move it : "))
path = str(input("enter the path u want to move your file to : "))
list = []
for root, dirs, files in os.walk("/root/"):
    for name in files:
        if name == f :
           name = str(name)
           name = os.path.realpath(os.path.join(root,name))
           list.append(name)


shutil.copy(list[0],path)

import urllib.request
import os
import platform
import ctypes
urllib.request.urlretrieve("https://heimdalsecurity.com/blog/wp-content/uploads/Wana_Decrypt0r_screenshot-1.png", "ransom.png")

pic = "ransom.png"
list = []
for root, dirs, files in os.walk("C:\\"):
    for name in files:
        if name == pic :
            name = str(name)
            name = os.path.join(root, name)
            list.append(name)
print(list[0])
print(platform.architecture()[0])
if platform.architecture()[0] == "32bit" :
    ctypes.windll.user32.SystemParametersInfoW(20,0,list[0],3)
elif platform.architecture()[0] == "64bit" :

    ctypes.windll.user32.SystemParametersInfoA(20, 0, list[0], 3)

print("Done")

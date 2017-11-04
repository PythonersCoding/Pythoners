import random
import string
error = "\033[31m[!]\033[0m "
info = "\033[33m[i]\033[0m "
while True :
    genType = input("""\n1.) alphanum\n2.) alpha\n3.) alphacap\n4.) all\n[~] Which type?: """)
    if (genType.isdigit() == False):
        print(error + "Bad input\n")
    break

while True :
    genLength = input("""[~] Length of password: """)
    if (genLength.isdigit() == False):
        print (error+"Bad input\n")
    break

passwd = ""
alphanum = string.ascii_letters + string.digits
alpha = string.ascii_letters
alphacap = string.ascii_uppercase
all = string.ascii_letters + string.digits + string.punctuation

if str(genType).lower() == "1":

    genType = alphanum
elif str(genType).lower() == "2":
    genType = alpha
elif str(genType).lower() == "3":
    genType = alphacap
elif str(genType).lower() == "4":
    genType = all
print (info+"Password: "+passwd.join(random.sample(genType, int(genLength))))
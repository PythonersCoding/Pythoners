__author = "Pythoners"

from datetime import datetime
now = datetime.now()
t = int(now.strftime ("%Y")) # to get the currently year example :2017
M = int(now.strftime("%m"))  # to get the currently month example : 10
D = int(now.strftime("%d"))  # to get the currently day example : 24
y = int(input("Enter the year you were Born :"))
m = int(input("Enter the month you were Born :"))
d = int(input("Enter the day you were Born :"))

your_year = (t-y)
print("u have been lived for : {} years".format(your_year))
your_month = (t-y)*12+(M-m)
print("u have been lived for : {} months".format(your_month))
if m == 2 :
    day = 28
elif m == 4:
    day=30
elif m == 11:
    day=30
elif m == 9:
    day=30
elif m == 6:
    day=30
else:
    day=31

if m == 1:

    your_day = (your_year)*365 + ((M-m)*31-5) + (day - d) - (day - D)

if m == 2:

    your_day = (your_year)*365 + ((M-m)*31-3) + (day - d) - (day - D)

elif m == 3 :

    your_day = (your_year)*365 + ((M-m)*31-3) + (day - d) - (day - D)

elif m == 4 :

    your_day = (your_year)*365 + ((M-m)*31-2) + (day - d) - (day - D)

elif m == 5 :

    your_day = (your_year)*365 + ((M-m)*31-2) + (day - d) - (day - D)

elif m == 6 :

    your_day = (your_year)*365 + ((M-m)*31-1) + (day - d) - (day - D)

elif m == 7 :

    your_day = (your_year)*365 + ((M-m)*31-1) + (day - d) - (day - D)

elif m == 8 :

    your_day = (your_year)*365 + ((M-m)*31-1) + (day - d) - (day - D)

elif m == 9 :

    your_day = (your_year)*365 + ((M-m)*31-0) + (day - d) - (day - D)

elif m == 10 :

    your_day = (your_year)*365 + ((M-m)*31-0) + (day - d) - (day - D)

elif m == 11 :

    your_day = (your_year)*365 + ((M-m)*31-0) + (day - d) - (day - D)

elif m == 12 :
    your_day = (your_year)*365 + ((M-m)*31-0) + (day - d) - (day - D)

print("u have been lived for : {} day".format(your_day))








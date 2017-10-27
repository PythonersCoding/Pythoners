# task 2
__author = "Pythoners"
from random import randint
import sys
from threading import Timer
import os

def tooslow():
    print ("\ntoo slow :( " )
    os._exit(1)


timer = Timer(50, tooslow)
timer.start()


x = randint(1, 100)
z = randint(1, 100)
l = randint(1, 100)
d = randint(1, 100)

r = int(x + z)
r2 = int(l - x)
r3 = int(z * l)


print("what is {} + {} ?".format(x, z))

a = int(input("Your answer is : "))


if not a :
    timer.cancel()

elif a == r:
    print("good now answer Question 2 what is {} - {} ".format(l, x))

elif a != r:
    print("\nIncorrect answer ")
    os._exit(1)
a2 = int(input("Your answer is : "))



if not a2 :
    timer.cancel()
elif a2 == r2:
    print("good now answer Question 3 what is {} * {} ".format(z, l))

elif a2 != r2:
    print("\nIncorrect answer ")
    os._exit(1)



a3 = int(input("Your answer is : "))

if not a3 :
    timer.cancel()
elif a3 == r3:

    while d % x != 0:
        d = randint(1, 100)
        x = randint(1, 100)
    if d % x == 0:
        print("good now answer Question 4 what is {} / {} ".format(d, x))
        r4 = float(d / x)
elif a3 != r3:
    print("\nIncorrect answer ")
    os._exit(1)

a4 = int(input("Your answer is : "))



if not a4 :
    timer.cancel()
elif a4 == r4:

    while z <= d :
        z = randint(0, 100)
        d = randint(0, 100)
    if z > d:
        print("good now answer Question 3 what is {} % {} ".format(z, d))
        r5 = float(z % d)

elif a4 != r4:
    print("\nIncorrect answer ")
    os._exit(1)
a5 = int(input("Your answer is : "))


if not a5 :
    timer.cancel()
elif a5 == r5:
    print("congratulations you win !")

else:
    print("You're out of the game !")

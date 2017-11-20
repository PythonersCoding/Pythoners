# Task 9
__Author = "Pythoners"
import pyttsx3

Y = pyttsx3.init()
Y.setProperty('rate', 135)
x = str(input("what word do you want to say ?"))
Y.say(x)
Y.runAndWait()
وده الgui بتاعه

from tkinter import *
import pyttsx3

# task 9
__Author = "Pythoners"


class Talk:
    def __init__(self):
        root = Tk()

        labl = Label(root, text="What do you want to say ?", fg="blue", bg="white", font="none 12 bold")
        labl.grid(row=0, column=0)

        self.x = Entry(root, width=22)
        self.x.grid(row=1, column=0, sticky=N)

        bt1 = Button(root, text="Speak", font="none 12 bold", command=self.speak, bg="white", fg="red")
        bt1.grid(columnspan=2)

        root.resizable(width=False, height=False)
        root.mainloop()

    def speak(self):
        Y = pyttsx3.init()
        Y.setProperty('rate', 135)
        Y.say(self.x.get())
        Y.runAndWait()

x = Talk()

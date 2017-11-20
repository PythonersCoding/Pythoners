from tkinter import *
# task 8
__Author = "Pythoners"


class LearnPython:
    def __init__(self):
        root = Tk()
        root.geometry("425x600")
        self.srvr = Entry(root, width=22)
        self.srvr.grid(row=1, column=0, sticky=N)
        self.srvr.setvar(name="server", value="")

        labl = Label(root, text="What do you want to learn today ?", fg="black", bg="white", font="none 12 bold")
        labl.grid(row=0, column=0)

        bt1 = Button(root, text="Enter", font="none 12 bold", command=self.IfElse, bg="white", fg="black")
        bt1.grid(columnspan=2)

        self.txt = Text(root, width=60, height=50, wrap=WORD, fg="black", bg="white")
        self.txt.grid(row=5, column=0, sticky=W)
        self.IfElse()
        root.title("Learn Python with us")
        root.resizable(width=False, height=False)
        root.mainloop()

    def IfElse(self):
        if self.srvr.get() == "def":
            self.msg = 'def stands for define and it`s the function in python \n example:- \n def print(): \n    print("this is a print function")'
            self.txt.insert(0.0, self.msg)
        elif self.srvr.get() == "loop":
            self.msg = 'this is a loop\n'
            self.txt.insert(0.0, self.msg)
        elif self.srvr.get() == "if/else":
            self.msg = 'this is if and else\n'
            self.txt.insert(0.0, self.msg)


python = LearnPython()

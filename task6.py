import socket
from tkinter import *
from tkinter import messagebox
from datetime import datetime
class PortScanner:
    def __init__(self):
        root = Tk()
        self.srvr = Entry(root,textvariable="server",width=22)
        self.srvr.grid(row=0,column=1,sticky=W)
        self.srvr.setvar(name="server",value="")
        lablstart = Label(root,text="Starting Port",fg="black",bg="white",width=13)
        lablstart.grid(row=2,column=0,sticky=W)
        labl = Label(root,text="Server address",fg="black",bg="white",width=13)
        labl.grid(row=0,column=0,sticky=W )
        self.start = Spinbox(root,from_=1,to=10000,value=1)
        self.start.grid(row=2,column=1,sticky=E)
        labl2 = Label(root,text="Ending ports",fg="black",bg="white",width=13)
        labl2.grid(row=3,column=0,sticky=W)
        self.end = Spinbox(root,from_=1,to=10000,value=10000)
        self.end.grid(row=3,column=1,sticky=E)
        bt = Button(root,text="Scan",font="none 12 bold",command=self.scan,bg="black",fg="white")
        bt.grid(columnspan=2)
        self.txt = Text(root,width=50,height=30,wrap=WORD)
        self.txt.grid(row=5,column=0,sticky=W)
        self.txt.insert(0.0 ,'Open Ports will apper here after scan is complete\n\nPortScanner By Pythoners')
        menu = Menu(root)
        root.config(menu=menu)
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Close", command=sys.exit)
        subMenu.add_command(label="New File",command=PortScanner)
        root.resizable(width=False,height=False)
        root.title("Port Scanner by Pythoners".center(140))
        root.mainloop()
    def pscan(self,port):
        try:
            target = self.srvr.get()
            s=socket.socket()
            s.settimeout(1)
            s.connect((target,port))
            return True
        except :
            return False
    def scan(self):
        self.txt.delete(0.0,END)
        print("scanning",self.srvr.get())
        t1 = datetime.now()
        for port in range(int(self.start.get()),int(self.end.get())+1) :
            if self.pscan(port):
                print("port"+str(port)+ "is open")
                msg = 'Port ' + str(port) + ' Is Open : '+socket.getservbyport(port)+"\n"
                self.txt.insert(0.0,msg)
            else :
                print("Port"+str(port)+ "is closed")
        t2 = datetime.now()
        self.txt.insert(0.0,'Scan has finished at %s\r\n' %t2)
        self.txt.insert(0.0,'Scan has started at %s\r\n' %t1)
        total = t2-t1
        messagebox.showinfo(title="Port scanner ",message="Scan Complete in "+str(total))

portscanner = PortScanner()
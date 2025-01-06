import csv
import tkinter as tk

class IpSites:

    def __init__(self,win:tk.Tk,ipfile:str,root:str):

        self.win=win
        self.ipfile=ipfile
        self.root=root
        self.checkvars=[]
        self.checkbuts=[]
        self.ips=[]
        self.otherip=None

        self.readfile()

        t=0
        for i in self.ips:
            for j in i:
                if j:
                    self.checkvars.append(tk.IntVar())
                    self.checkbuts.append(tk.Checkbutton(self.win,variable=self.checkvars[t]))
                    t+=1

        self.othercheckvar=tk.IntVar()
        self.othercheckbut=tk.Checkbutton(self.win,variable=self.othercheckvar)
        self.otheripvar=tk.StringVar()
        self.otheripvar.set(self.otherip)
        self.otheripent=tk.Entry(self.win,textvariable=self.otheripvar)

    def readfile(self):

        with open(self.ipfile) as file:
            reader=list(csv.reader(file))

        self.otherip=f"{self.root}.{reader[0][0]}"
        reader[0][0]=''
            
        for i in reader:
            tmp=[]
            for j in i:
                tmp.append(f"{self.root}.{j}" if j else j)
            self.ips.append(tmp)

    def place(self,x:int,y:int,dw:int=50,dh:int=50):
        
        t=0
        for i in range(len(self.ips)):
            for j in range(len(self.ips[i])):
                if self.ips[i][j]:
                    self.checkbuts[t].place(x=x+(j-1)*dw,y=y+(i-1)*dh)
                    t+=1

        self.othercheckbut.place(x=x,y=len(self.ips)*dh)
        self.otheripent.place(x=x+30,y=len(self.ips)*dh,width=150,height=30)

    def get(self)->list:

        ips=[]
        t=0

        for i in self.ips:
            for j in i:
                if j:
                    if t<len(self.checkvars) and self.checkvars[t].get():
                        ips.append(j)
                    t+=1

        if self.othercheckvar.get():
            ips.append(self.otheripvar.get())

        return ips

    def forget(self):

        for i in self.checkbuts:
                i.place_forget()
        
        self.othercheckbut.place_forget()

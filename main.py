import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from ip_sites import IpSites
import hack

win=tk.Tk()
win.title("JiyuController")
win.iconbitmap(default="file\\jiyu.ico")
win_w,win_h=800,450
win_x,win_y=(win.winfo_screenwidth()-win_w)//2,(win.winfo_screenheight()-win_h)//2
win.geometry(f"{win_w}x{win_h}+{win_x}+{win_y}")
win.resizable(False,False)

def obey_command(*event):
    ips=ipsites.get()
    command=obey_cbox.get()
    
    if ips==[]:
        showerror(title="JiyuController",message="没有指定ip")
        return

    print(*ips,sep=',',end=' [command]: ')
    print(command)

    hack.obey_command(ips,command)

def send_message(*event):
    ips=ipsites.get()
    message=send_ent.get()
    
    if ips==[]:
        showerror(title="JiyuController",message="没有指定ip")
        return

    print(*ips,sep=',',end=' [message]: ')
    print(message)

    hack.send_message(ips,message)

def ipsites_update(*event):
    global ipsites

    ipsites.forget()
    ipsites=IpSites(win,ipfile_ent.get(),root_ent.get())
    ipsites.place(x=400,y=40)

#执行命令
obey_lab=tk.Label(win,text="命令：",font=("宋体",12))
obey_values=('shutdown -s -t 0',
             'shutdown -i',
             'echo  >C:\\Users\\Administrator\\Desktop',
             'for /l %a in (0,0,1) do',
             'taskkill -F -IM StudentMain.exe',
             'start chrome.exe "网址"')
obey_cbox=ttk.Combobox(win,values=obey_values)
obey_cbox.bind("<Return>",obey_command)
obey_but=tk.Button(win,text="执行命令",command=obey_command,font=("宋体",12))

obey_lab.place(x=40,y=30,width=60,height=30)
obey_cbox.place(x=40,y=60,width=260,height=30)
obey_but.place(x=300,y=60,width=80,height=30)

#发送消息
send_lab=tk.Label(win,text="消息：",font=("宋体",12))
send_ent=tk.Entry(win)
send_ent.bind("<Return>",send_message)
send_but=tk.Button(win,text="发送消息",command=send_message,font=("宋体",12))

send_lab.place(x=40,y=130,width=60,height=30)
send_ent.place(x=40,y=160,width=260,height=30)
send_but.place(x=300,y=160,width=80,height=30)

#ip根
root_lab=tk.Label(win,text="ip根：",font=("宋体",12))
root_var=tk.StringVar()
root_var.set("192.168.112")
root_ent=tk.Entry(win,textvariable=root_var)
root_ent.bind("<Return>",ipsites_update)
root_but=tk.Button(win,text="确定",command=ipsites_update,font=("宋体",12))

root_lab.place(x=40,y=230,width=60,height=30)
root_ent.place(x=40,y=260,width=150,height=30)
root_but.place(x=190,y=260,width=60,height=30)

#ip文件
ipfile_lab=tk.Label(win,text="ip文件：",font=("宋体",12))
ipfile_var=tk.StringVar()
ipfile_var.set("file\\ip.csv")
ipfile_ent=tk.Entry(win,textvariable=ipfile_var)
ipfile_ent.bind("<Return>",ipsites_update)
ipfile_but=tk.Button(win,text="确定",command=ipsites_update,font=("宋体",12))

ipfile_lab.place(x=50,y=330,width=60,height=30)
ipfile_ent.place(x=40,y=360,width=150,height=30)
ipfile_but.place(x=190,y=360,width=60,height=30)

#ip坐标
ipsites=IpSites(win,ipfile_ent.get(),root_ent.get())

ipsites.place(x=400,y=40)

#循环刷新
win.mainloop()

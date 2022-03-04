from tkinter import *
from pymodbus.client.sync import ModbusTcpClient

root = Tk()

def PLC_Connection_Status():
    client = ModbusTcpClient("192.168.1.200",port=502)
    connection = client.connect()
    print(f"PLC CONNECTION STATUS--------->{connection}")
    if connection == False:
        Label(root,text="False").place(x=80,y=110)
    else:
        Label(root,text="True").place(x=80,y=110)

root.geometry("200x200")
Button(root, text="connect PLC",command=PLC_Connection_Status).place(x=60,y=80)
root.mainloop()
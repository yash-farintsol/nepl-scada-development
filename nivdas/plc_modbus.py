import json
import datetime
import pymodbus
import numpy as np
from pymodbus.client.sync import ModbusTcpClient
client = ModbusTcpClient("192.168.1.200")
connection = client.connect()
print("Modbus connection ",connection,'\n')

#READ/VIEW RTC(TIME) FROM PLC
def view_rtc():
    vrtc_set_1 = client.read_holding_registers(146,5,unit = 0x01)
    vrtc_set_2 = client.read_holding_registers(152,2,unit = 0x01)
    vrtc_set_3 = client.read_holding_registers(155,1,unit = 0x01)
    vrtc_keys = ["view_sec","view_hour_min","view_month_date","view_year","view_hour","view_min","view_month","view_date"]
    vrtc_values = [vrtc_set_1.registers[i] for i in range(0,5)] + [vrtc_set_2.registers[0],vrtc_set_2.registers[1]] + [vrtc_set_3.registers[0]]
    view_rtc_values = json.dumps({vrtc_keys[i]:vrtc_values[i] for i in range(0,8)})
    print("View_RTC_Values  -->  ",view_rtc_values,'\n')

#WRITE/SET RTC(TIME) TO PLC
def set_rtc():
    set_sec = 30
    set_min = 25
    set_hour = 5
    set_date = 5
    set_month = 10
    set_year = 2021
    client.write_registers(130,set_sec,unit = 0x01)
    client.write_registers(131,set_min,unit = 0x01)
    client.write_registers(132,set_hour,unit = 0x01)
    client.write_registers(133,set_date,unit = 0x01)
    client.write_registers(134,set_month,unit = 0x01)
    client.write_registers(135,set_year,unit = 0x01)
    

#READ TEMPERATURE VALUES
def temp_set():
    tset = client.read_holding_registers(4,3,unit = 0x01)
    tset_keys = ["chamber1_set_temp","chamber1_set_low_temp","chamber1_set_high_temp"]
    tset_values = [tset.registers[i] for i in range(0,3)]
    temp_set_values = json.dumps({tset_keys[i]:tset_values[i]/10 for i in range(0,3)})
    print("Temp_Set_Values  -->  ",temp_set_values,'\n')
    
view_rtc()
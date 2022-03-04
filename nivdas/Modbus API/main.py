import os
import time
import schedule
import ast
import datetime
import pymodbus
import numpy as np
import json
from pymodbus.client.sync import ModbusTcpClient
import paho.mqtt.client as mqtt




mclient = mqtt.Client()
mclient.connect("broker.hivemq.com",1883,60)

def on_connect(mclient,userdata,flag,rc):
    #print("connected")
    mclient.subscribe("nepl/trans_info")
def on_message(mclient,userdata,msg):
    data = json.loads(msg.payload.decode())
    global flag
    flag = data["Send"]
    #print(flag)
    

def DecimalToBinary(num):
    bin = np.binary_repr(num,width=12)
    #binary = int(bin(num).replace("0b",""))
    return bin
    
plc_rtc_time = time.time()
initial_file_time = time.time()


def input_status():
    inputs = client.read_holding_registers(85,10,unit = 0x01)
    bin = np.binary_repr(inputs.registers[0],width=12)
    input_keys = ["alarm_ack","chamber2_door_sensor","chamber1_door_sensor","chamber2_compressor_fb","chamber1_compressor_fb","chamber2_main_fail",
                  "chamber1_main_fail","chamber2_dry_heater_fb","chamber1_dry_heater_fb","null","null"]
    input_values = list(bin)
    input_status_values = json.dumps({input_keys[i]:input_values[i] for i in range(0,10)})
    #print("Input_Status_Values  -->  ",input_status_values)
    return json.loads(input_status_values)
    
def output_status():
    outputs = client.read_holding_registers(85,16,unit = 0x01)
    bin = np.binary_repr(outputs.registers[0],width=16)
    output_keys = ["chamber2_compressor","chamber1_compressor","null","null1","null2","null3","remote_alrarm",
                  "alarm_hooter_2","null4","null5","null6","alarm_hooter_1",
                   "chamber2_dry_heater_safety_relay","chamber1_dry_heater_safety_relay",
                   "chamber2_dry_heater","chamber1_dry_heater"]
    output_values = list(bin)
    #print(output_values)
    output_status_values = json.dumps({output_keys[i]:output_values[i] for i in range(0,16)})
    #print("Output_Status_Values  -->  ",output_status_values)
    return json.loads(output_status_values)

def temp_act_values():
    act_val = client.read_holding_registers(14,1,unit = 0x01)
    present_val = client.read_holding_registers(4,1,unit = 0x01)
    set_val = client.read_holding_registers(5,1,unit = 0x01)
    temp_act_value = json.dumps({"actual_temp":act_val.registers[0]/10, "present_temp":present_val.registers[0]/10, "set_val":set_val.registers[0]/10})
    #print("temp_act_values  -->  ",temp_act_value)
    return json.loads(temp_act_value)


    
   
def rtc_job(ip_add, sink_time):
    #print("***********************************************")
    #print(ip_add, sink_time, datetime.datetime.now())
    #print("rtc write for once")
    #print("***********************************************")
    
    c = datetime.datetime.fromisoformat(sink_time)
    client.write_register(130,int(c.second),unit = 0x01)
    client.write_register(131,int(c.minute),unit = 0x01)
    client.write_register(132,int(c.hour),unit = 0x01)
    client.write_register(133,int(c.day),unit = 0x01)
    client.write_register(134,int(c.month),unit = 0x01)
    client.write_register(135,int(c.year),unit = 0x01)
    
    return schedule.CancelJob

def read_set_rtc(ip_addr):
    srtc = client.read_holding_registers(130,6,unit=0x01)
    srtc_keys = ["set_sec","set_min","set_hour","set_date","set_month","set_year"]
    srtc_values = [srtc.registers[i] for i in range(0,6)]
    set_rtc_values = json.dumps({srtc_keys[i]:srtc_values[i] for i in range(0,6)})
    #print("SET_RTC_Values  -->  ",set_rtc_values)
    #print("SET_RTC_Values  -->  ",srtc_values)
    if (srtc_values[5]== 0 or srtc_values[4]== 0 or srtc_values[3]== 0):
        plc_rtc_time = datetime.datetime(2000,1,1,0,0,0)
    else:
        plc_rtc_time=datetime.datetime(srtc_values[5],srtc_values[4],srtc_values[3],srtc_values[2],srtc_values[1],srtc_values[0])
        plc_rtc_time = plc_rtc_time.isoformat()
    #print("plc_time  ",plc_rtc_time)
    client.close()
        
    return plc_rtc_time


def check_rtc(ip_add):
    global client
    client = ModbusTcpClient(ip_add)
    connection = client.connect()
    #print(ip_add," on check ",connection)
    if connection == True:
        ## reading ip address sink value from the file
        with open("active_eqp.txt", "r") as file:
            str_file_data = file.read()
            list_file_data = ast.literal_eval(str_file_data)
        for i in range(len(list_file_data)):
            #plc_rtc = plc_rtc_time
            plc_rtc = read_set_rtc(list_file_data[i]['ip_addr'])
            if plc_rtc != list_file_data[i]['sink']:
                rtc_job(list_file_data[i]['ip_addr'], list_file_data[i]['sink'])
    else:
        pass



def data_job(ip_add, sink_time, eqp_name):
    global client
    client = ModbusTcpClient(ip_add)
    connection = client.connect()
    #print(ip_add,"  ",connection)
    if connection == True:
        #print(ip_add, sink_time, datetime.datetime.now())
        #mclient.publish("nepl/dd", json.dumps({"ip_addr": "192.168.1.125"}))
        mclient.publish("nepl/dd", json.dumps({"ip_addr": ip_add,"conn_status":connection,"eqp_name":eqp_name, "data":{"input_status": input_status(),"output_status":output_status() ,"temperature": temp_act_values()}}))
        client.close()
    else:
        mclient.publish("nepl/dd", json.dumps({"ip_addr": ip_add,"conn_status":connection,"eqp_name":eqp_name, "data":{}}))
        client.close()
        


def on_filechange():
    global on_start
    if on_start:
        with open("active_eqp.txt", "r") as file:
            str_file_data = file.read()
            list_file_data = ast.literal_eval(str_file_data)

        for i in range(len(list_file_data)):
            schedule.every(list_file_data[i]['log_interval']).seconds.do(data_job,
                                                                             ip_add=list_file_data[i]['ip_addr'],
                                                                             sink_time=list_file_data[i]['sink'],
                                                                         eqp_name=list_file_data[i]['eqp_name'])
        #print("schedule on start  ---->")
        
        on_start = False
        
    _time = os.path.getmtime("active_eqp.txt")
    global initial_file_time
    if _time != initial_file_time:

        initial_file_time = _time
        #print("changed")
        
        schedule.clear()
        #print("below clear schedules")
        with open("active_eqp.txt", "r") as file:
            str_file_data = file.read()
            list_file_data = ast.literal_eval(str_file_data)
        #print("list_file   ",list_file_data)
        
        
        for i in range(len(list_file_data)):
            
            check_rtc(list_file_data[i]['ip_addr'])
           
            schedule.every(list_file_data[i]['log_interval']).seconds.do(data_job,
                                                                             ip_add=list_file_data[i]['ip_addr'],
                                                                             sink_time=list_file_data[i]['sink'],
                                                                         eqp_name=list_file_data[i]['eqp_name'])
        #print("schedule on change  ---->")


mclient.on_connect = on_connect
mclient.on_message = on_message
mclient.loop_start()
flag = "Stop"
on_start = True

while True:
    if(flag == "Now"):
        try:
            on_filechange()
        except:
            pass
            #print("error")
    if(flag == "Stop"):
        schedule.clear()
        on_start = True
    
    schedule.run_pending()
    time.sleep(1)

# 1642062217.7845552

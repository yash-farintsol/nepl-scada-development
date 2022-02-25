import json
import datetime
import pymodbus
import ast
import os
from pymodbus.client.sync import ModbusTcpClient
import paho.mqtt.client as mqtt


# Connection to the MQTT
def on_connect(client, userdata, flags, rc):
    print("connected to broker" + str(rc))
    client.subscribe("nepl/eqp_create_request")
    client.subscribe("nepl/eqp_update_request")


json_var = {}

def on_message(client, userdata, msg):
    json_var = json.loads(msg.payload.decode())
    print("json_var")
    print(json_var)
    print(len(json_var))
    if(msg.topic=="nepl/eqp_create_request"):
        eqp_write(json_var)
    if(msg.topic=="nepl/eqp_update_request"):
        ip_chfn_list = ip_check_fn(json_var)
        update_list(ip_chfn_list, json_var) 

def eqp_write(json_var):
    print(len(json_var))
    json_list = []
    if(len(json_var) != 0):
        if(json_var['eqp_status'] == "Active"):
            if(os.path.isfile('active_eqp.txt')==False):
                json_list.append(json_var)
                with open("active_eqp.txt", "w") as file:
                    file.write(str(json_list))
                print("Active eqp file created")
                print("Equipment Added in Active list")
            else:
                ip_chfn_list = ip_check_fn(json_var)
                if(ip_chfn_list[0] == "No Data"):
                    with open("active_eqp.txt", "r") as file:
                        str_file_data = file.read()
                    json_list = ast.literal_eval(str_file_data)
                    json_list.append(json_var)
                    with open("active_eqp.txt", "w") as file:
                        file.write(str(json_list))
                    print("Equipment Added in Active list")
                else:
                    print("IP ADDRESS already exists")

        if(json_var['eqp_status'] == "InActive"):
            if(os.path.isfile('inactive_eqp.txt')==False):
                json_list.append(json_var)
                with open("inactive_eqp.txt", "w") as file:
                    file.write(str(json_list))
                print("InActive eqp file created")
                print("Equipment Added in InActive list")
            else:
                ip_chfn_list = ip_check_fn(json_var)
                if(ip_chfn_list[0] == "No Data"):
                    with open("inactive_eqp.txt", "r") as file:
                        str_file_data = file.read()
                    json_list = ast.literal_eval(str_file_data)
                    json_list.append(json_var)
                    with open("inactive_eqp.txt", "w") as file:
                        file.write(str(json_list))
                    print("Equipment Added in InActive list")
                else:
                    print("IP ADDRESS already exists")



client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

client.loop_start()
client.on_connect = on_connect
client.on_message = on_message

def ip_check_fn(json_var):
    print("inside ip_check_fn")
    found_in_active = 0
    found_in_inactive = 0
    fn_list = [1, 2, 3]

    if(os.path.isfile('active_eqp.txt')==True):
        print("Active file exists")
        with open("active_eqp.txt", "r") as file:
            str_file_data = file.read()
            
        list_file_data = ast.literal_eval(str_file_data)
        i = 0
        for i in range(0, len(list_file_data)):
            if(json_var["ip_addr"] == list_file_data[i]["ip_addr"]):
                found_in_active = 1
                fn_list[0] = "Data"
                fn_list[1] = "Active"
                fn_list[2] = i
                print("Available in active list at "+ str(i) + " json element")
        if(i==len(list_file_data) and found_in_active == 0):
            print("Not availalble in active list")

    if(os.path.isfile('inactive_eqp.txt')==True):
        print("Inactive file exists")
        with open("inactive_eqp.txt", "r") as file:
            str_file_data = file.read()
        list_file_data = ast.literal_eval(str_file_data)
        i = 0
        for i in range(0, len(list_file_data)):
            if(json_var["ip_addr"] == list_file_data[i]["ip_addr"]):
                found_in_inactive = 1
                fn_list[0] = "Data"
                fn_list[1] = "InActive"
                fn_list[2] = i
                print("Available in inactive list at "+ str(i) + " json element")

        if(i==len(list_file_data) and found_in_inactive == 0):
            print("Not availalble in inactive list")

    #print("found_in_active", found_in_active)
    #print("found_in_inactive",found_in_inactive)
    if(found_in_active==0 and found_in_inactive==0):
        fn_list[0] = "No Data"
        fn_list[1] = 0
        fn_list[2] = 0
        print("No Data in both lists")

    print("Function Output",fn_list)
    return(fn_list)

def update_list(ip_chfn_list, json_var):
    if(ip_chfn_list[0]=="Data"):
        if(ip_chfn_list[1]=="Active"):
            with open("active_eqp.txt", "r") as file:
                str_file_data = file.read()
            list_file_data = ast.literal_eval(str_file_data)
        if(ip_chfn_list[1]=="InActive"):
            with open("inactive_eqp.txt", "r") as file:
                str_file_data = file.read()
            list_file_data = ast.literal_eval(str_file_data)
        update_obj = list_file_data[ip_chfn_list[2]]
        #update eqp_status
        if(update_obj['eqp_status'] != json_var['eqp_status']):
            list_file_data[ip_chfn_list[2]]['eqp_status'] = json_var['eqp_status']
            up_obj = list_file_data.pop(ip_chfn_list[2])
            if(json_var['eqp_status']=="Active"):
                with open("active_eqp.txt", "r") as file:
                    str_data = file.read()
                list_data = ast.literal_eval(str_data)
                list_data.append(up_obj)
                with open("active_eqp.txt", "w") as file:                    
                    file.write(str(list_data))
                print("eqp_status Updated")

            if(json_var['eqp_status']=="InActive"):
                with open("inactive_eqp.txt", "r") as file:
                    str_data = file.read()
                list_data = ast.literal_eval(str_data)
                list_data.append(up_obj)
                with open("inactive_eqp.txt", "w") as file:                    
                    file.write(str(list_data))
                print("eqp_status Updated")
        #update log_interval
        if(update_obj['log_interval'] != json_var['log_interval']):
            list_file_data[ip_chfn_list[2]]['log_interval'] = json_var['log_interval']
            print("Log Interval Change Detected")
            print("Log Interval from file: ", list_file_data[ip_chfn_list[2]]['log_interval'])
            print("Log Interval from list", json_var['log_interval'])
            if(ip_chfn_list[1]=="Active"):
                with open("active_eqp.txt", "w") as file:
                    file.write(str(list_file_data))
                print("Log Interval Updated in"+ip_chfn_list[1]+"List")
            if(ip_chfn_list[1]=="InActive"):
                with open("inactive_eqp.txt", "w") as file:
                    file.write(str(list_file_data))
                print("Log Interval Updated in"+ip_chfn_list[1]+"List")
        #update sink
        if(update_obj['sink'] != json_var['sink']):
            list_file_data[ip_chfn_list[2]]['sink'] = json_var['sink']
            print("Sink Change Detected")
            print("sink from file: ",str(list_file_data[ip_chfn_list[2]]['sink']))
            print("sink from mqtt: ", json_var['sink'])
            if(ip_chfn_list[1]=="Active"):
                with open("active_eqp.txt", "w") as file:
                    file.write(str(list_file_data))
                print("Sink Updated in"+ip_chfn_list[1]+"List")
            if(ip_chfn_list[1]=="InActive"):
                with open("inactive_eqp.txt", "w") as file:
                    file.write(str(list_file_data))
                print("Sink Updated in"+ip_chfn_list[1]+"List")


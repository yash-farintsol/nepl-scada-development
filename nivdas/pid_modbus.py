import json
import datetime
import pymodbus
import numpy as np
from pymodbus.client.sync import ModbusTcpClient
client = ModbusTcpClient("192.168.1.200")
connection = client.connect()
print(connection)

def DecimalToBinary(num):
    bin = np.binary_repr(num,width=12)
    #binary = int(bin(num).replace("0b",""))
    return bin
    
def alarms():
    chamber1_temp1_high_alarm = client.read_coils(41,8,unit = 0x01)
    chamber1_temp1_low_alarm = client.read_coils(42,8,unit = 0x01)
    chamber1_door_open_alarm = client.read_coils(35,8,unit = 0x01)
    chamber1_main_fail_alarm = client.read_coils(36,8,unit = 0x01)
    chamber1_co_ckt_fail_alarm = client.read_coils(84,8,unit = 0x01)
    chamber2_co_ckt_fail_alarm = client.read_coils(96,8,unit = 0x01)
    chamber1_dh_ckt_fail_alarm = client.read_coils(94,8,unit = 0x01)
    chamber2_dh_ckt_fail_alarm = client.read_coils(95,8,unit = 0x01)
    chamber1_temp1_within_range = client.read_coils(165,4,unit = 0x01)
    alarm_values = json.dumps({"chamber1_temp1_high_alarm":chamber1_temp1_high_alarm.bits[0],
                "chamber1_temp1_low_alarm":chamber1_temp1_low_alarm.bits[0],
                  "chamber1_door_open_alarm":chamber1_door_open_alarm.bits[0],
                "chamber1_main_fail_alarm":chamber1_main_fail_alarm.bits[0],
                  "chamber1_co_ckt_fail_alarm":chamber1_co_ckt_fail_alarm.bits[0],
                "chamber2_co_ckt_fail_alarm":chamber2_co_ckt_fail_alarm.bits[0],
                  "chamber1_dh_ckt_fail_alarm":chamber1_dh_ckt_fail_alarm.bits[0],
                "chamber2_dh_ckt_fail_alarm":chamber2_dh_ckt_fail_alarm.bits[0],
                  "chamber1_temp1_within_range":chamber1_temp1_within_range.bits[0]})
    print("Alarm_Values  -->  ",alarm_values)
    

def view_rtc():
    vrtc = client.read_holding_registers(146,10,unit = 0x01)
    vrtc_keys = ["view_sec","view_hour_min","view_month_date","view_year","view_hour","null","view_min","view_month","null","view_date"]
    vrtc_values = [vrtc.registers[i] for i in range(0,10)]
    view_rtc_values = json.dumps({vrtc_keys[i]:vrtc_values[i] for i in range(0,10)})
    print("View_RTC_Values  -->  ",view_rtc_values)

def set_rtc():
    srtc = client.read_holding_registers(130,6,unit = 0x01)
    srtc_keys = ["set_sec","set_min","set_hour","set_date","set_month","set_year"]
    srtc_values = [srtc.registers[i] for i in range(0,6)]
    set_rtc_values = json.dumps({srtc_keys[i]:srtc_values[i] for i in range(0,6)})
    print("SET_RTC_Values  -->  ",set_rtc_values)

def input_status():
    inputs = client.read_holding_registers(85,10,unit = 0x01)
    bin = np.binary_repr(inputs.registers[0],width=12)
    input_keys = ["alarm_ack","chamber2_door_sensor","chamber1_door_sensor","chamber2_compressor_fb","chamber1_compressor_fb","chamber2_main_fail",
                  "chamber1_main_fail","chamber2_dry_heater_fb","chamber1_dry_heater_fb","null","null"]
    input_values = list(bin)
    input_status_values = json.dumps({input_keys[i]:input_values[i] for i in range(0,10)})
    print("Input_Status_Values  -->  ",input_status_values)
    
def output_status():
    outputs = client.read_holding_registers(85,16,unit = 0x01)
    bin = np.binary_repr(outputs.registers[0],width=16)
    output_keys = ["chamber2_compressor","chamber1_compressor","null","null1","null2","null3","remote_alrarm",
                  "alarm_hooter_2","null4","null5","null6","alarm_hooter_1",
                   "chamber2_dry_heater_safety_relay","chamber1_dry_heater_safety_relay",
                   "chamber2_dry_heater","chamber1_dry_heater"]
    output_values = list(bin)
    print(output_values)
    output_status_values = json.dumps({output_keys[i]:output_values[i] for i in range(0,16)})
    print("Output_Status_Values  -->  ",output_status_values)
    

def set_values():
    r = client.read_holding_registers(390,6,unit = 0x01)
    r_keys = ["no.of_sensors","chamber1_compressor_cut_off","null","chamber2_compressor_cut_off","null","compressor_dalay"]
    r_values = [r.registers[i] for i in range(0,6)]
    print(r_values)
    

def temp_pid_set():
    pid = client.read_holding_registers(7,4,unit = 0x01)
    temp_pid_keys = ["chamber1_temp_KP","chamber1_temp_TI","chamber1_temp_TD","chamber1_temp_cycle_time"]
    temp_pid_values = [pid.registers[i] for i in range(0,4)]
    temp_pid_set_values = json.dumps({temp_pid_keys[i]:temp_pid_values[i] for i in range(0,4)})
    print("Temp_PID_Set_Values  -->  ",temp_pid_set_values)
    
def temp_set():
    tset = client.read_holding_registers(4,3,unit = 0x01)
    tset_keys = ["chamber1_set_temp","chamber1_set_low_temp","chamber1_set_high_temp"]
    tset_values = [tset.registers[i] for i in range(0,3)]
    temp_set_values = json.dumps({tset_keys[i]:tset_values[i]/10 for i in range(0,3)})
    print("Temp_Set_Values  -->  ",temp_set_values)

def temp_act():
    cv_pid = client.read_holding_registers(4,3,unit = 0x01)
    actual_temp = client.read_holding_registers(4,3,unit = 0x01)
    temp_act_values = json.dumps({"chamber1_temp_cv_pid":cv_pid.registers[0]/10,"chamber1_actual_temp_1":actual_temp.registers[0]/10})
    print("temp_act_values  -->  ",temp_act_values)
    

def temp_act_values():
    act_val = client.read_holding_registers(14,1,unit = 0x01)
    temp_act_value = json.dumps({"chamber1_temp":act_val.registers[0]})
    print("temp_act_values  -->  ",temp_act_value)



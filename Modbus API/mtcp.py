import time
from pymodbus.client.sync import ModbusTcpClient

#modbus connection
client = ModbusTcpClient('192.168.1.125')
connection = client.connect()
while True:
    #client = ModbusTcpClient('192.168.1.125')
    #client.write_registers(130,6)
    #read register
    request = client.read_holding_registers(130,6,unit=0x01) #covert to float
    result = request.registers
    print(result)
    #client.close()
    #write to register
    time.sleep(0.5) 

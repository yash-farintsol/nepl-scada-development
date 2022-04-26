import numpy as np
from pymodbus.client.sync import ModbusTcpClient


def read_registers(ip_address, values):
    result = {}
    client = ModbusTcpClient("192.168.1.211")  # "192.168.1.200"
    connection = client.connect()
    # print("Modbus connection ", connection, '\n')
    if connection:
        try:
            for i in values:
                if i > 400000:
                    if i in [400086, 400087]:
                        ios = client.read_holding_registers(i - 400001, 1, unit=0x01)
                        ios_bin = np.binary_repr(ios.registers[0], width=16)
                        values = list(ios_bin)
                        result[i] = values
                    elif i in [400004, 400025, 400014, 400015, 400016, 400017, 400018, 400019, 400020, 400021, 400022,
                               400023, 400035, 400036, 400037, 400038, 400039, 400040, 400041, 400042, 400043, 400044]:
                        reg = client.read_holding_registers(i - 400001, 1, unit=0x01).registers[0]
                        result[i] = reg / 10
                    else:
                        reg = client.read_holding_registers(i - 400001, 1, unit=0x01).registers[0]
                        result[i] = reg
                if 0 < i < 99999:
                    alarms = client.read_coils(i - 1, 8, unit=0x01)
                    result[i] = alarms.bits[0]

            return result
        except:
            return "Register address error"
    else:
        return "Modbus Connection Error"


# # read_registers(ip_address, [address11, address2])
# # returns
# # - Modbus Connection Error on modbus disconnected
# # - Register address error on reading wrong registers

list = read_registers("192.168.1.211", [400151,400153,400147,400156,400154,400150])
print(list)



# from pymodbus.client.sync import ModbusTcpClient


# {400005:50,400006:50}
# def modbus_write(ip_address, values):
#     client = ModbusTcpClient(ip_address)  # "192.168.1.200"
#     print(values)
#     connection = client.connect()
#     print("Modbus connection ", connection, '\n')
#     if connection:
#         try:
#             for i in values:
#                 if i in [400005, 400006, 400007, 400012, 400026, 400027, 400028, 400033]:
#                     client.write_registers(i - 400001, values[i] * 10, unit=0x01)
#                 else:
#                     client.write_registers(i - 400001, values[i], unit=0x01)
#             return True
#         except:
#             return "Register address error"

#     else:
#         return "Modbus Connection Error"

'''

Function - modbus_write(ip_address,{key1:value1, key2:value2})
ip_address = "192.168.1.200"
Chamber1 Set Temp       400005     5
Chamber1 Set Low Temp   400006     3
Chamber1 Set High Temp  400007     7
Sample Function Call - modbus_write("192.168.1.200", {400005: 5, 400006: 3, 400007: 7})

returns the following outputs based on the operations performed.
   - Modbus Connection Error on modbus disconnected
   - Register address error on writing wrong registers
   - True on successful write.

For writing RTC values to the PLC.
Apart from writing date and time in respective registers we should also write "1" in SETRTC CONFIRM Register(400137) so that the PLC will understand
to use the data in the SET RTC registers.

'''
# modbus_write("192.168.1.200",
#              {400131: 40, 400132: 40, 400133: 20, 400028: 75, 400029: 40, 400030: 40, 400031: 40, 400033: 5, 400364: 2})

import numpy as np
from pymodbus.client.sync import ModbusTcpClient


def read_registers(ip_address, values):
    result = {}
    client = ModbusTcpClient("192.168.1.200")  # "192.168.1.200"
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


# read_registers(ip_address, [address11, address2])
# returns
# - Modbus Connection Error on modbus disconnected
# - Register address error on reading wrong registers

list = read_registers("192.168.1.200", [400151,400153,400147,400087])
print(list)
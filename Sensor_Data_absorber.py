import serial
def Get_Sensor_values_degital(comport):
    s = []
    try:
        ser = serial.Serial(port= comport,baudrate=115200,parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
        i = 0
        ser.write(serial.to_bytes([0x01, 0x00, 0x01]))
        st = (int.from_bytes(ser.read(), "little"))
        ch = (int.from_bytes(ser.read(), "little"))
        while i < 8:
            s.append((int.from_bytes(ser.read(), "little")))
            i = i + 1
        ser.close()
        return (s)
    except :
        exit()

def Get_Sensor_values_Real(comport):
    s = []
    try:
        ser = serial.Serial(port= comport,baudrate=115200,parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
        i = 0
        ser.write(serial.to_bytes([0x01, 0x00, 0x01]))
        st = (int.from_bytes(ser.read(), "little"))
        ch = (int.from_bytes(ser.read(), "little"))
        while i < 8:
            s.append((int.from_bytes(ser.read(), "little"))*11.6/255)
            i = i + 1
        ser.close()
        return (s)
    except :
        exit()

import glob
import time
import serial
from sys import platform



def Port_finder_sensor():
    port1 = []
    if platform == 'win32':
        conne = [port.device for port in serial.tools.list_ports.comports()]
        for i in range(0, len(conne)):
            ser = serial.Serial(port=conne[i], baudrate=115200, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS, timeout=1)
            ser.write(serial.to_bytes([0x01, 0x00, 0x01]))
            data_raw = ser.readline()
            if data_raw != b'':PORT = conne[i]
            else:print('not the needed port')
            time.sleep(0.1)
    else:
        port = glob.glob('/dev/tty[A-Za-z]*')
        for i in range(0, len(port)):
            if 'ttyUSB' in port[i]:
                port1.append(port[i])
        for i in range(0, len(port1)):
            ser = serial.Serial(port=port1[i], baudrate=115200, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS, timeout=1)
            ser.write(serial.to_bytes([0x01, 0x00, 0x01]))
            data_raw = ser.readline()
            if data_raw != b'':PORT = port1[i]
            else:print('not the needed port')
            time.sleep(0.1)
    return(PORT)
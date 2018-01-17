#!/usr/bin/python
import serial
import time
import sys

def send():
    
    ser = serial.Serial(
                port="/dev/ttyUSB0",
                baudrate=115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
    
    ser.flushInput()
    ser.flushOutput()

    trame1 = bytes([0x02,0x00,0x08,0x00,0x00,0x00,0x00,0x00,0x08,0xAA,0x55,0x00,0x00,0x13,0xB9]) ## Get Infos command
    trame2 = bytes([0x02,0x00,0x08,0x00,0x00,0x00,0x08,0x00,0x01,0xAA,0x55,0x00,0x00,0x28,0x68]) ## Inventory command

    print (trame2)
    
    ser.write(trame2)

    result = ser.readline()
    result_ = []
    for byte in result:
##        print (hex(byte)[2:])
        result_.append(hex(byte)[2:])
    print (result_)
    print (result_[9])
    case = int(result_[9],16)
    print (case)

    EPC_length = int(result_[10],16)
    EPC_start = 11
    EPC_end = EPC_start + EPC_length
    EPC = []
    i = 0
    EPC_counter = EPC_start
    print ("counter = ",EPC_counter)
    print ("EPC_length = ",EPC_length)
    
    for EPC_counter in result:
##        if (EPC_counter < (EPC_start + EPC_length)):
            EPC[i] = result_[EPC_counter]
            i += 1

    print (EPC)
    
if __name__ == '__main__':     # Program start from here

    send()
                                                                                                                                                                                                                                                                   

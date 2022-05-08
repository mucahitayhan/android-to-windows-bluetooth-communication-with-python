import os
import serial

def enable():
    return os.system("netsh interface set interface 'Wi-Fi' enabled")

def disable():
    return os.system("netsh interface set interface 'Wi-Fi' disabled")   
kapatma=""
ser = serial.Serial(port="COM3",baudrate=9600,timeout=2)
while not kapatma==[b'criptoff']:
    for c in ser.read():
        line = ser.readlines()
        print(line)
        if line == [b'yku']: 
            print("1")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") #sleep mode
        elif line == [b'eboot']:
            print("2")
            os.system("shutdown -t 1 -r -f") #restart the computer
        elif line == [b'apat']:
            print("3")
            os.system("shutdown /s /t 1") #turn off the computer
        elif line == [b'criptoff']:
            print("4")
            kapatma=line
            print(kapatma)
        """if line == [b'ifion']:
            enable()#turn on wifi
            print("5")
        elif line == [b'ifioff']:
            disable()#turn off wifi
            print("6")"""
        #you can add what you want to your computer to do like the lines above

#uyku,reboot,kapat,scriptoff

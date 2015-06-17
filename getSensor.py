#!/usr/bin/python
import time
import wiringpi2
import os
import sys
import struct
import subprocess
from time import sleep
from notsmb import notSMB
from tsl2561_lux import Luxmeter

tmpVal = -999
humVal = -999
co2Val = -999
luxVal = -999

""" LUX Setting """
tsl=Luxmeter()
i = 0
while True:
    try:
        luxVal = int(tsl.getLux())
        if luxVal <= 200000 and luxVal > 100:
            break
        i = i + 1
        if i > 5:
            break
        sleep(0.5)
    except:
        blank =0;
sleep(0.5)

""" CO2 Setting """
I2CBUS = 1
CO2_ADDR = 0x68
READ = 0x22
readBytes = [0x00, 0x08, 0x2A]
bus = notSMB(I2CBUS)
i = 0
while True:
    try:
        resp = bus.i2c(CO2_ADDR,[0x22,0x00,0x08,0x2A],4)
        time.sleep(0.1)
        co2Val = (resp[1]*256) + resp[2]
        if co2Val < 8000:
            break
        i = i + 1
        if i > 5:
            break
    except:
        blank =0;
sleep(0.5)

""" Temperature Humidity Setting """
wiringpi2.wiringPiSetup()
i2c = wiringpi2.I2C()
dev = i2c.setup(0x40)

i2c.writeReg16(dev,0x02,0x10)
i2c.writeReg8(dev,0x00,0x00)
sleep((6350.0 + 6500.0 +  500.0)/1000000.0)
tmpVal = ((struct.unpack('4B', os.read(dev,4)))[0] << 8 | (struct.unpack('4B', os.read(dev,4)))[1])
humVal = ((struct.unpack('4B', os.read(dev,4)))[2] << 8 | (struct.unpack('4B', os.read(dev,4)))[3])
os.close(dev)
tmpVal = round(((tmpVal / 65535.0) * 165 - 40), 1)
humVal = round(((humVal / 65535.0) * 100), 1)
sleep(0.5)

 """ CSV Data Out """ 
line = time.strftime('%Y/%m/%d,') + time.strftime('%H:%M:%S,')
line = line + str(tmpVal) + "," + str(humVal) + "," + str(co2Val) + "," + str(luxVal)
print line

 """ LCD Dsplay Out """ 
parm1 = time.strftime('%m/%d_%H:%M')
parm2 = "T:" + str(tmpVal) + "*c_H:" + str(humVal) + "%"
parm3 = "CO2:" + str(co2Val) + "ppm"
parm4 = "Lig:" + str(luxVal) + "LUX"
cmd = "/home/pi/OLED %s %s %s %s" % (parm1, parm2, parm3, parm4)
subprocess.Popen( cmd.strip().split(" ")  )

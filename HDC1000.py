#!/usr/bin/python
import wiringpi2
import os
import struct
from time import sleep

wiringpi2.wiringPiSetup()
i2c = wiringpi2.I2C()
dev = i2c.setup(0x40)

i2c.writeReg16(dev,0x02,0x10)
i2c.writeReg8(dev,0x00,0x00)
sleep((6350.0 + 6500.0 +  500.0)/1000000.0)

temp = ((struct.unpack('4B', os.read(dev,4)))[0] << 8 | (struct.unpack('4B', os.read(dev,4)))[1]) 
hudi = ((struct.unpack('4B', os.read(dev,4)))[2] << 8 | (struct.unpack('4B', os.read(dev,4)))[3]) 
os.close(dev) 

print "Temperature %.1f" % round( (( temp / 65535.0) * 165 - 40 ), 1)
print "Humidity %.1f" % round( (( hudi / 65535.0 ) * 100), 1)

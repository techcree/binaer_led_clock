# Raspberry Pi Pico Pin Overview by StSkanta (TechCree) 838375
# Start Script
import machine
from machine import Pin
import utime
from machine import I2C
import time
import LEDtest
import os

#exec(open('LEDtest.py').read())

address = 0x68
register = 0x00
#sec min hour week day mout year !!set time here#
NowTime = b'\x00\x27\x14\x24\x02\x20\x22'  ###After set time kill this line
w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"];
#/dev/i2c-1
bus = I2C(1)
#def ds3231SetTime(): ###After set time kill this line
#    bus.writeto_mem(int(address),int(register),NowTime)  ###After set time kill this line

def ds3231ReadTime():
    return bus.readfrom_mem(int(address),int(register),7);

#ds3231SetTime()  ###After set time kill this line

#mainboard LED
led25 =  Pin(25, Pin.OUT)
#
#sekunden Einer
led00 = Pin(0, Pin.OUT) # sek1 gruen (1)
led01 = Pin(1, Pin.OUT) # sek1 gruen (2)
led02 = Pin(2, Pin.OUT) # sek1 gruen (4)
led03 = Pin(3, Pin.OUT) # sek1 gruen (8)
#sekunden Zehner
led04 = Pin(4, Pin.OUT) # sek10 gruen (1) 
led05 = Pin(5, Pin.OUT) # sek10 gruen (2)
#Pin6 wird vom RTC Modul benötigt###
led06 = Pin(28, Pin.OUT) # sek10 gruen (4)
# Pin7 wird vom RTC Modul benötigt###
led07 = Pin(15, Pin.OUT) # sek10 gruen (8)
# Minuten Einer
led08 = Pin(8, Pin.OUT) # min rot (1)
led09 = Pin(9, Pin.OUT) # min rot (2)
led10 = Pin(10, Pin.OUT) # min rot (4)
led11 = Pin(11, Pin.OUT) # min rot (8)
#Minuten Zehner
led12 = Pin(12, Pin.OUT) # min rot (1)
led13 = Pin(13, Pin.OUT) # min rot (2)
led14 = Pin(14, Pin.OUT) # min rot (4)
# min10 (8) rot wird nicht benötigt
#Stunden Einer
led16 = Pin(16, Pin.OUT) # std1 gelb (1)
led17 = Pin(17, Pin.OUT) # std1 gelb (2)
led18 = Pin(18, Pin.OUT) # std1 gelb (4)
led19 = Pin(27, Pin.OUT) # std1 gelb (8)
#Stunden Zehner
led20 = Pin(20, Pin.OUT) # std10 gelb (1)
led21 = Pin(26, Pin.OUT) # std10 gelb (2)
led22 = Pin(22, Pin.OUT) # std10 gelb (4)
# std10 (8) gelb wird nicht benötigt
#
while True:
    t = ds3231ReadTime()
    a = t[0]&0x7F  #sec
    b = t[1]&0x7F  #min
    c = t[2]&0x3F  #hour
    d = t[3]&0x07  #week
    e = t[4]&0x3F  #day
    f = t[5]&0x1F  #mouth
    print("20%x/%02x/%02x %02x:%02x:%02x %s" %(t[6],t[5],t[4],t[2],t[1],t[0],w[t[3]-1]))

    sek = int("%2x" %a)
    min = int("%2x" %b)
    stu = int("%2x" %c)
    print(stu, min, sek)
#
#alternate with input    
#    stu = int(input("Stunden 1er?"))
#    min =  int(input("Minuten 1er?"))
#    sek = int(input("Sekunden 1er?"))
  
    if sek == 1:
        led00.value(1) 
    if sek == 2:
        led01.value(1)
    if sek == 3:    
        led00.value(1)
        led01.value(1)
    if sek == 4:    
        led02.value(1)
    if sek == 5:    
        led00.value(1)
        led02.value(1)
    if sek == 6:
        led01.value(1)
        led02.value(1)
    if sek == 7:
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 8:    
        led03.value(1)
    if sek == 9:
        led00.value(1)
        led03.value(1)
    if sek == 10:    
        led04.value(1)
    if sek == 11:
        led04.value(1)
        led00.value(1)
    if sek == 12:
        led04.value(1)
        led01.value(1)
    if sek == 13:
        led04.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 14:
        led04.value(1)
        led02.value(1)
    if sek == 15:
        led04.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 16:
        led04.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 17:
        led04.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 18:
        led04.value(1)
        led03.value(1)
    if sek == 19:
        led04.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 20:    
        led05.value(1)
    if sek == 21:
        led05.value(1)
        led00.value(1)
    if sek == 22:
        led05.value(1)
        led01.value(1)
    if sek == 23:
        led05.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 24:
        led05.value(1)
        led02.value(1)
    if sek == 25:
        led05.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 26:
        led05.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 27:
        led05.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 28:
        led05.value(1)
        led03.value(1)
    if sek == 29:
        led05.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 30:    
        led04.value(1)
        led05.value(1)
    if sek == 31:
        led04.value(1)
        led05.value(1)
        led00.value(1)
    if sek == 32:
        led04.value(1)
        led05.value(1)
        led01.value(1)
    if sek == 33:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 34:
        led04.value(1)
        led05.value(1)
        led02.value(1)
    if sek == 35:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 36:
        led04.value(1)
        led05.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 37:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 38:
        led04.value(1)
        led05.value(1)
        led03.value(1)
    if sek == 39:
        led04.value(1)
        led05.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 40:    
        led06.value(1)
    if sek == 41:
        led06.value(1)
        led00.value(1)
    if sek == 42:
        led06.value(1)
        led01.value(1)
    if sek == 43:
        led06.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 44:
        led06.value(1)
        led02.value(1)
    if sek == 45:
        led06.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 46:
        led06.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 47:
        led06.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 48:
        led06.value(1)
        led03.value(1)
    if sek == 49:
        led06.value(1)
        led00.value(1)
        led03.value(1)
    if sek == 50:
        led04.value(1)
        led06.value(1)
    if sek == 51:
        led04.value(1)
        led06.value(1)
        led00.value(1)
    if sek == 52:
        led04.value(1)
        led06.value(1)
        led01.value(1)
    if sek == 53:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led01.value(1)
    if sek == 54:
        led04.value(1)
        led06.value(1)
        led02.value(1)
    if sek == 55:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led02.value(1)
    if sek == 56:
        led04.value(1)
        led06.value(1)
        led01.value(1)
        led01.value(1)
    if sek == 57:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led01.value(1)
        led02.value(1)
    if sek == 58:
        led04.value(1)
        led06.value(1)
        led03.value(1)
    if sek == 59:
        led04.value(1)
        led06.value(1)
        led00.value(1)
        led03.value(1)
###
    if min == 1:    
        led08.value(1)
    if min == 2:        
        led09.value(1)
    if min == 3:
        led08.value(1)
        led09.value(1)
    if min == 4:    
        led10.value(1)
    if min == 5:
        led08.value(1)
        led10.value(1)      
    if min == 6:
        led09.value(1)
        led10.value(1)
    if min == 7:
        led08.value(1)
        led09.value(1)
        led10.value(1)  
    if min == 8:
        led11.value(1)
    if min == 9:
        led08.value(1)
        led11.value(1)
###        
    if min == 10:
        led12.value(1)
    if min == 11:
        led12.value(1)
        led08.value(1)
    if min == 12:
        led12.value(1)
        led09.value(1)
    if min == 13:
        led12.value(1)
        led08.value(1)
        led09.value(1)
    if min == 14:
        led12.value(1)
        led10.value(1)
    if min == 15:
        led12.value(1)
        led08.value(1)
        led10.value(1)
    if min == 16:
        led12.value(1)
        led09.value(1)
        led10.value(1)
    if min == 17:
        led12.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)
    if min == 18:
        led12.value(1)
        led11.value(1)
    if min == 19:
        led12.value(1)
        led08.value(1)
        led11.value(1)
    if min == 20:
        led13.value(1)
    if min == 21:
        led13.value(1)
        led08.value(1)
    if min == 22:
        led13.value(1)        
        led09.value(1)
    if min == 23:
        led13.value(1)
        led08.value(1)
        led09.value(1)
    if min == 24:
        led13.value(1)    
        led10.value(1)
    if min == 25:
        led13.value(1)
        led08.value(1)
        led10.value(1)      
    if min == 26:
        led13.value(1)
        led09.value(1)
        led10.value(1)
    if min == 27:
        led13.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)  
    if min == 28:
        led13.value(1)
        led11.value(1)
    if min == 29:
        led13.value(1)
        led08.value(1)
        led11.value(1)
    if min == 30:
        led12.value(1)
        led13.value(1)
    if min == 31:
        led12.value(1)
        led13.value(1)
        led08.value(1)
    if min == 32:
        led12.value(1)
        led13.value(1)        
        led09.value(1)
    if min == 33:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led09.value(1)
    if min == 34:
        led12.value(1)
        led13.value(1)    
        led10.value(1)
    if min == 35:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led10.value(1)      
    if min == 36:
        led12.value(1)
        led13.value(1)
        led09.value(1)
        led10.value(1)
    if min == 37:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)  
    if min == 38:
        led12.value(1)
        led13.value(1)
        led11.value(1)
    if min == 39:
        led12.value(1)
        led13.value(1)
        led08.value(1)
        led11.value(1)
    if min == 40:
        led14.value(1)
    if min == 41:
        led14.value(1)
        led08.value(1)
    if min == 42:
        led14.value(1)
        led09.value(1)
    if min == 43:
        led14.value(1)
        led08.value(1)
        led09.value(1)
    if min == 44:
        led14.value(1)
        led10.value(1)
    if min == 45:
        led14.value(1)
        led08.value(1)
        led10.value(1)
    if min == 46:
        led14.value(1)
        led09.value(1)
        led10.value(1)
    if min == 47:
        led14.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)
    if min == 48:
        led14.value(1)
        led11.value(1)
    if min == 49:
        led14.value(1)
        led08.value(1)
        led11.value(1)
    if min == 50:
        led12.value(1)
        led14.value(1)
    if min == 51:
        led12.value(1)
        led14.value(1)
        led08.value(1)
    if min == 52:
        led12.value(1)
        led14.value(1)
        led09.value(1)
    if min == 53:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led09.value(1)
    if min == 54:
        led12.value(1)
        led14.value(1)
        led10.value(1)
    if min == 55:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led10.value(1)
    if min == 56:
        led12.value(1)
        led14.value(1)
        led09.value(1)
        led10.value(1)
    if min == 57:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led09.value(1)
        led10.value(1)
    if min == 58:
        led12.value(1)
        led14.value(1)
        led11.value(1)
    if min == 59:
        led12.value(1)
        led14.value(1)
        led08.value(1)
        led11.value(1)
###
    if stu == 1:        
        led16.value(1)
    if stu == 2:
        led17.value(1)
    if stu == 3:
        led16.value(1)
        led17.value(1)
    if stu == 4:
        led18.value(1)
    if stu == 5:
        led16.value(1)
        led18.value(1)
    if stu == 6:
        led17.value(1)
        led18.value(1)
    if stu == 7:
        led16.value(1)
        led17.value(1)
        led18.value(1)
    if stu == 8:
        led19.value(1)
    if stu == 9:
        led16.value(1)
        led19.value(1)
##
    if stu == 10:        
        led20.value(1)
    if stu == 11:
        led20.value(1)
        led16.value(1)
    if stu == 12:
        led20.value(1)
        led17.value(1)
    if stu == 13:
        led20.value(1)
        led16.value(1)
        led17.value(1)
    if stu == 14:
        led20.value(1)
        led18.value(1)
    if stu == 15:
        led20.value(1)
        led16.value(1)
        led18.value(1)
    if stu == 16:
        led20.value(1)
        led17.value(1)
        led18.value(1)
    if stu == 17:
        led20.value(1)
        led16.value(1)
        led17.value(1)
        led18.value(1)
    if stu == 18:
        led20.value(1)
        led19.value(1)
    if stu == 19:
        led20.value(1)
        led16.value(1)
        led19.value(1)
    if stu == 20:        
        led21.value(1)
    if stu == 21:
        led21.value(1)
        led16.value(1)
    if stu == 22:
        led21.value(1)
        led17.value(1)
    if stu == 23:
        led21.value(1)
        led16.value(1)
        led17.value(1)
    if stu == 24: #??
        led21.value(1)
        led18.value(1)
 
    time.sleep(1)
#Reset LEDS
    led00.value(0) 
    led01.value(0) 
    led02.value(0) 
    led03.value(0) 
    led04.value(0) 
    led05.value(0) 
    led06.value(0) 
    led07.value(0)
    led08.value(0) 
    led09.value(0)
    led10.value(0)
    led11.value(0)
    led12.value(0)
    led13.value(0)
    led14.value(0)
#    led15.value(0)
    led16.value(0)
    led17.value(0)
    led18.value(0)
    led19.value(0)
    led20.value(0)
    led21.value(0)
    led22.value(0)
#    led24.value(0)

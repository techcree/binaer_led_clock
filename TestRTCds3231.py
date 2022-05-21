#!/usr/bin/python
# -*- coding: utf-8 -*-
from machine import I2C
import time

address = 0x68
register = 0x00
#sec min hour week day mout year
NowTime = b'\x00\x00\x15\x04\x21\x01\x21'
w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"];
#/dev/i2c-1
bus = I2C(1)
def ds3231SetTime():
	bus.writeto_mem(int(address),int(register),NowTime)

def ds3231ReadTime():
	return bus.readfrom_mem(int(address),int(register),7);

ds3231SetTime()
while 1:
	t = ds3231ReadTime()
	a = t[0]&0x7F  #sec
	b = t[1]&0x7F  #min
	c = t[2]&0x3F  #hour
	d = t[3]&0x07  #week
	e = t[4]&0x3F  #day
	f = t[5]&0x1F  #mouth
#	print("20%x/%02x/%02x %02x:%02x:%02x %s" %(t[6],t[5],t[4],t[2],t[1],t[0],w[t[3]-1]))
	print(c, b, a)
	
time.sleep(1)

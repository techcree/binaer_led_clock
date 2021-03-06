# Raspberry Pi Pico Pin Overview by StSkanta (TechCree) 838375
# Enter an "X" for your occupied pins
#
#                        [X] LED onBoard
#
# led00 GP0  [X]  (1)  sek1                 (40)  [ ] VBUS
# led01 GP1  [X]  (2)  sek2                 (39)  [ ] VSYS
#       GND  [ ]  (3)              BuzzerGND(38)  [X] GDN        lED Panel GDN
# led02 GP2  [X]  (4)  sek4                 (37)  [ ] 3V3_EN
# led03 GP3  [X]  (5)  sek8                 (36)  [X] 3V3(OUT)   RTC Power
# led04 GP4  [X]  (6)  sek10                (35)  [ ] -
# led05 GP5  [X]  (7)  sek20          sek40 (34)  [X] GP28 led06
#       GND  [ ]  (8)                       (33)  [ ] GND
#       GP6  [X]  (9)  (RTCMod)        stu8 (32)  [X] GP27 led19
#       GP7  [X]  (10) (RTCMod)             (31)  [X] GP26 
# led08 GP8  [X]  (11) min                  (30)  [ ] RUN
# led09 GP9  [X]  (12) min2           stu40 (29)  [X] GP22 led22 
#       GND  [ ]  (13)                      (28)  [ ] GND
# led10 GP10 [X]  (14) min4           stu20 (27)  [X] GP21 led21 
# led11 GP11 [X]  (15) min8             stu (26)  [X] GP20 led20 
# led12 GP12 [X]  (16) min            Buzzer(25)  [x] GP19
# led13 GP13 [X]  (17) min20           stu4 (24)  [X] GP18 led18 
#       GND  [ ]  (18)                      (23)  [ ] GDN
# led14 GP14 [X]  (19) min40           stu2 (22)  [X] GP17 led17 
# led07 GP15 [X]  (20) min80            stu (21)  [X] GP16 led16  
#
#                    [ ]SWCLK [ ]GND [ ]SWDIO
#
# The LED on the Pico board is the LED PIN 25
#
#                Stu                                Min                               Sek
#  80 ()            8 (GP27/led19)    80 ()            8 (GP11/led11)    80 (GP15/led07)  8 (GP3/led03)
#  40 (GP22/led22)  4 (GP18/led18)    40 (GP14/led14)  4 (GP10/led10)    40 (GP28/led06)  4 (GP2/led02)
#  20 (GP21/led21)  2 (GP17/led17)    20 (GP13/led13)  2 (GP9/led09)     20 (GP5/led05)   2 (GP1/led01)
#  10 (GP20/led20)  1 (GP16/led16)    10 (GP12/led12)  1 (GP8/led08)     10 (GP4/led04)   1 (GP0/led00)
#
#
#

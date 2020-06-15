import serial
import time
import pyautogui

ser=serial.Serial('COM5', baudrate = 9600 , timeout=1)
#ser.open()
time.sleep(10)

while 1:
    time.sleep(0.1)
    g1=ser.readline()
    #print g1
    g1=g1.split()
    g1[0]=float(g1[0])
    g1[1]=float(g1[1])
##    g3=ser.readline()
##    gx=float(g1)
##    gy=float(g2)
##    #gz=float(g3)
##    vx = (gx+15)/15 
##    #vy = -(gz-100)/150
    #print (g1[0],g1[1])
    millis = time.time()*1000
    pyautogui.moveRel(g1[0],g1[1])
    print(-millis+time.time()*1000)
    
    

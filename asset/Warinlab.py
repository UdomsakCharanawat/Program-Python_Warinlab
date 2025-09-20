import RPi.GPIO as GPIO
from time import sleep
import time
from omxplayer.player import OMXPlayer
import sys
import os

GPIO.setmode(GPIO.BOARD)
pt1 = 11
pe1 = 12
GPIO.setup(pt1,GPIO.OUT)
GPIO.setup(pe1,GPIO.IN)
pt2 = 13
pe2 = 15
GPIO.setup(pt2,GPIO.OUT)
GPIO.setup(pe2,GPIO.IN)
pt3 = 16
pe3 = 18
GPIO.setup(pt3,GPIO.OUT)
GPIO.setup(pe3,GPIO.IN)
pt4 = 29
pe4 = 31
GPIO.setup(pt4,GPIO.OUT)
GPIO.setup(pe4,GPIO.IN)
pt5 = 33
pe5 = 35
GPIO.setup(pt5,GPIO.OUT)
GPIO.setup(pe5,GPIO.IN)

path = ('/home/pi/Music/')
#path = ('/media/pi/IDS/music/')
au = '--loop'
media = os.listdir(path)
media.sort()
print(media[0])
mediaPlay = OMXPlayer(path + media[0], au)
mediaPlay.set_volume(0)

maxCM = 150
minCM = 50
maxVol = 1
minVol = 0
volume = 0
changeVol = False
lastVol = 0

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = 0
tempSetvol1 = 0
tempSetvol2 = 0
tempSetvol3 = 0
tempSetvol4 = 0
tempSetvol5 = 0
lis = 0

def distance1():
    global temp1
    global tempSetvol1
    GPIO.output(pt1, GPIO.HIGH)
    sleep(0.001)
    GPIO.output(pt1, GPIO.LOW)
    startTime = time.time()
    stopTime = time.time()
    #print("looping")
    try:
        p=0
        isError = False
        while GPIO.input(pe1) == 0:
            startTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 0 -------------------- 1")
                isError = True
                break
        p=0
        while GPIO.input(pe1) == 1:
            stopTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 1 -------------------- 1")
                isError = True
                break
    except:
        print("check sensor")
    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300) / 2
    if isError:
        distance = maxCM
    #print("distance1 : ",distance)
    
    lis = distance - temp1
    if lis < 0:
        lis *= -1
        #print("lis : ",lis)
    if lis > 100:
        #print("error")
        setvol = tempSetvol1
    elif lis < 100:
        period = maxCM - minCM
        soundPeriod = maxVol - minVol
        soundPertick = soundPeriod / period
        if distance < minCM:
            distance = minCM
        elif distance > maxCM:
            distance = maxCM
        setvol = minVol + (soundPertick * (distance- minCM))
        setvol = -(setvol - maxVol)
    temp1 = distance
    tempSetvol1 = setvol
    #print(setvol)
    return setvol



def distance2():
    global temp2
    global tempSetvol2
    GPIO.output(pt2, GPIO.HIGH)
    sleep(0.001)
    GPIO.output(pt2, GPIO.LOW)
    startTime = time.time()
    stopTime = time.time()
    #print("looping")
    try:
        p=0
        isError = False
        while GPIO.input(pe2) == 0:
            startTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 0 -------------------- 2")
                isError = True
                break
        p=0
        while GPIO.input(pe2) == 1:
            stopTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 1 -------------------- 2")
                isError = True
                break
    except:
        print("check sensor")
    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300) / 2
    if isError:
        distance = maxCM
    #print("distance  : ",distance)
    
    lis = distance - temp2
    if lis < 0:
        lis *= -1
        #print("lis : ",lis)
    if lis > 100:
        #print("error")
        setvol = tempSetvol2
    elif lis < 100:
        period = maxCM - minCM
        soundPeriod = maxVol - minVol
        soundPertick = soundPeriod / period
        if distance < minCM:
            distance = minCM
        elif distance > maxCM:
            distance = maxCM
        setvol = minVol + (soundPertick * (distance- minCM))
        setvol = -(setvol - maxVol)
    temp2 = distance
    tempSetvol2 = setvol
    return setvol

def distance3():
    global temp3
    global tempSetvol3
    GPIO.output(pt3, GPIO.HIGH)
    sleep(0.001)
    GPIO.output(pt3, GPIO.LOW)
    startTime = time.time()
    stopTime = time.time()
    #print("looping")
    try:
        p=0
        isError = False
        while GPIO.input(pe3) == 0:
            startTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 0 -------------------- 3")
                isError = True
                break
        p=0
        while GPIO.input(pe3) == 1:
            stopTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 1 -------------------- 3")
                isError = True
                break
    except:
        print("check sensor")
    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300) / 2
    if isError:
        distance = maxCM
    #print("distance  : ",distance)
    
    lis = distance - temp3
    if lis < 0:
        lis *= -1
        #print("lis : ",lis)
    if lis > 100:
        #print("error")
        setvol = tempSetvol3
    elif lis < 100:
        period = maxCM - minCM
        soundPeriod = maxVol - minVol
        soundPertick = soundPeriod / period
        if distance < minCM:
            distance = minCM
        elif distance > maxCM:
            distance = maxCM
        setvol = minVol + (soundPertick * (distance- minCM))
        setvol = -(setvol - maxVol)
    temp3 = distance
    tempSetvol3 = setvol
    return setvol

def distance4():
    global temp4
    global tempSetvol4
    GPIO.output(pt4, GPIO.HIGH)
    sleep(0.001)
    GPIO.output(pt4, GPIO.LOW)
    startTime = time.time()
    stopTime = time.time()
    #print("looping")
    try:
        p=0
        isError = False
        while GPIO.input(pe4) == 0:
            startTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 0 -------------------- 4")
                isError = True
                break
        p=0
        while GPIO.input(pe4) == 1:
            stopTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 1 -------------------- 4")
                isError = True
                break
    except:
        print("check sensor")
    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300) / 2
    if isError:
        distance = maxCM
    #print("distance  : ",distance)
    
    lis = distance - temp4
    if lis < 0:
        lis *= -1
        #print("lis : ",lis)
    if lis > 100:
        #print("error")
        setvol = tempSetvol4
    elif lis < 100:
        period = maxCM - minCM
        soundPeriod = maxVol - minVol
        soundPertick = soundPeriod / period
        if distance < minCM:
            distance = minCM
        elif distance > maxCM:
            distance = maxCM
        setvol = minVol + (soundPertick * (distance- minCM))
        setvol = -(setvol - maxVol)
    temp4 = distance
    tempSetvol4 = setvol
    return setvol

def distance5():
    global temp5
    global tempSetvol5
    GPIO.output(pt5, GPIO.HIGH)
    sleep(0.001)
    GPIO.output(pt5, GPIO.LOW)
    startTime = time.time()
    stopTime = time.time()
    #print("looping")
    try:
        p=0
        isError = False
        while GPIO.input(pe5) == 0:
            startTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 0 -------------------- 5")
                isError = True
                break
        p=0
        while GPIO.input(pe5) == 1:
            stopTime = time.time()
            p+=1
            if p > 100000:
                print("Error! Freeze 1 -------------------- 5")
                isError = True
                break
    except:
        print("check sensor")
    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300) / 2
    if isError:
        distance = maxCM
    #print("distance  : ",distance)
    
    lis = distance - temp5
    if lis < 0:
        lis *= -1
        #print("lis : ",lis)
    if lis > 100:
        #print("error")
        setvol = tempSetvol5
    elif lis < 100:
        period = maxCM - minCM
        soundPeriod = maxVol - minVol
        soundPertick = soundPeriod / period
        if distance < minCM:
            distance = minCM
        elif distance > maxCM:
            distance = maxCM
        setvol = minVol + (soundPertick * (distance- minCM))
        setvol = -(setvol - maxVol)
    temp5 = distance
    tempSetvol5 = setvol
    return setvol
    
 
if __name__ == '__main__':
    try:
        while True:
            setvol1 = distance1()
            print("rang 1 : ", setvol1)
            setvol2 = distance2()
            print("rang 2 : ", setvol2)
            setvol3 = distance3()
            print("rang 3 : ", setvol3)
            setvol4 = distance4()
            print("rang 4 : ", setvol4)
            setvol5 = distance5()
            print("rang 5 : ", setvol5)
            sumvol = (setvol1 + setvol2 + setvol3 + setvol4 + setvol5) / 5
            
            print("sumvol : ",sumvol)
            
            print("    ")
            #sumvol = setvol1
            #if sumvol < 0:
            #    sumvol = 0
            #if sumvol > 1:
            #    sumvol = 1
            volSet = float(sumvol)
            
            if volume != volSet and changeVol == False:
                    #print("")
                    changeVol = True
            if changeVol == True:
                count = 0
                if volume < volSet:
                    while volume < volSet and count < 20:
                        count+=1
                        if volume <= 1:
                            volume += 0.03
                        else:
                            volume = volSet
                        #print("change volume up : ", volume)
                        mediaPlay.set_volume(volume)
                        sleep(0.001)
                        if volume >= volSet:
                            changeVol == False
                            #print("out up volume : ", changeVol)
                if volume > volSet:
                    while volume > volSet and count < 20:
                        count+=1
                        if volume >= 0:
                            volume -= 0.03
                        else:
                            volume = volSet
                        #print("change volume down : ",volume)
                        mediaPlay.set_volume(volume)
                        sleep(0.001)
                        if volume <= sumvol:
                            changeVol == False
                            #print("out down volume : ", changeVol)
            sleep(0.2)
    except KeyboardInterrupt:
        print("STOP")
        GPIO.cleanup()

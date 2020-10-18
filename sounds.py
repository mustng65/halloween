#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from subprocess import call
from multiprocessing import Process


PIN_ECHO = 11
PIN_TRIGGER = 7
background_audio_path ="sounds/background-sounds.wav"
welcome_audio_path ="sounds/evil-laugh.wav"
isWelcoming=0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_TRIGGER,GPIO.OUT)
GPIO.setup(PIN_ECHO,GPIO.IN)

def checkdist():
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while not GPIO.input(PIN_ECHO):
        pass
    t1 = time.time()
    while GPIO.input(PIN_ECHO):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

def spookySounds():
    while True:
        call(["aplay", background_audio_path])

def welcomeMessage():
    call(["aplay", welcome_audio_path])

P = Process(name="playsound",target=spookySounds)
P.start() # Inititialize Process

time.sleep(2)

try:
    while True:
        distance = checkdist();
        msg="Distance: {:.2f}m"
        print (msg.format(distance))

        if distance < .5 and isWelcoming==0:
            P2 = Process(name="welcome",target=welcomeMessage)
            P2.start() # Inititialize Process
            isWelcoming=1

        if distance > 1.5:
            isWelcoming=0

        time.sleep(0.5)
except KeyboardInterrupt:
    print("bye")
    GPIO.cleanup()    
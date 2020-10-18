import os
from picamera import PiCamera
from time import sleep
from datetime import datetime

dateTimeObj = datetime.now()

ts = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%S.%f")

fileName = ts +'.mp4'
camera = PiCamera()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
os.system('sudo MP4Box -fps 30 -add ../video.h264 ../ShareFiles/' + fileName)

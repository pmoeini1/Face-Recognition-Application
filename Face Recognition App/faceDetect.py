import os
import cv2 as cv
import numpy as np
import time
from mail import *

# turn on camera
vid = cv.VideoCapture(0)
# get face detection .xml
haar_cascade = cv.CascadeClassifier('Face Recognition App\haar_face.xml')
# classify people
people = ["me", "not me"]
# create face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# input pre-made .yml into recognizer
face_recognizer.read('Face Recognition App\face_trained.yml')

if not vid.isOpened():
    # send error message if camera is not opened
    sendErrorEmail()
    exit()

while vid.isOpened():
    # read image from camera
    isTrue, img = vid.read()
    if (isTrue):
        # grayscale image
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # find faces in image
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x,y,w,h) in faces_rect:
            # isolate faces in image
            faces_roi = gray[y:y+h,x:x+w]
            # predict the face
            label, confidence = face_recognizer.predict(faces_roi)
            # label the image
            cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
            # put rectangle around face of user
            cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
            if label != "me":
                # send alert email to user if intruder is detected
                sendAlertEmail(confidence)
            else:
                continue
        
    else:
        # send error message if image can't be read
        sendErrorEmail()
        exit()
    
    # pause 60 seconds
    time.sleep(60)

exit()
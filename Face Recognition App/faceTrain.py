import os
import cv2 as cv
import numpy as np

# folder titles of training images
people = ["me", "not me"]
# get path to haar cascade and images
DIR =r'Face Recognition App\images, training'
haar_cascade = cv.CascadeClassifier('Face Recognition App\haar_face.xml')
# arrays to hold features and classifications
features = []
labels = []

# go through folders
for filename in people:
    path = os.path.join(DIR, filename)
    label = people.index(filename)
    # go through images within folder
    for img in os.listdir(path):
        # turn images into numeric arrays
        img_path = os.path.join(path, img)
        img_array = cv.imread(img_path)
        # handle errors in imread
        if img_array is None:
            continue
        # turn images to grayscale
        gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
        # detect faces
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
        # go through and crop just the face in the images
        for (x,y,w,h) in faces_rect:
                faces_crop = gray[y:y+h, x:x+w]
                # append face data into features
                features.append(faces_crop)
                # append classification
                labels.append(label)

# turn features and labels into numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)
# create model for face classification
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# train model
face_recognizer.train(features,labels)
# save model data
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
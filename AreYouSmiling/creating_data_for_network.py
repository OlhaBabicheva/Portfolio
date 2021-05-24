import numpy as np
import os
import cv2
import face_recognition
import pickle
import random

DATADIR = "images"
CATEGORIES = ["neutral", "sad", "smiling"]

IMG_SIZE = 64

training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))
                face_locations = face_recognition.face_locations(img_array)
                for (top, right, bottom, left) in face_locations:
                    face = img_array[top:bottom, left:right, :]
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    new_array = cv2.resize(face, (IMG_SIZE, IMG_SIZE))
                    training_data.append([new_array, class_num])

            except Exception as e:
                pass


create_training_data()

print(len(training_data))

random.shuffle(training_data)

for sample in training_data[:10]:
    print(sample[1])

X = []
Y = []

for features, label in training_data:
    X.append(features)
    Y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("Y.pickle", "wb")
pickle.dump(Y, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("Y.pickle", "rb")
X = pickle.load(pickle_in)
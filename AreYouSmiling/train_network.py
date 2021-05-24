import os
import pickle
import tensorflow as tf
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split

BATCH_SIZE = 8
EPOCHS = 50

NAME = "RUsmiling"
tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))

os.makedirs('weights', exist_ok=True)
checkpoints = ModelCheckpoint(
    'weights/weights.{epoch:04d}-{val_acc:.3f}.hdf5',
    monitor='val_acc', verbose=0, save_best_only=False)

X = pickle.load(open("X.pickle", "rb"))
Y = pickle.load(open("Y.pickle", "rb"))

X = X / 255.0

Y = to_categorical(Y, num_classes=3)
X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.25, random_state=1)

train_datagen = ImageDataGenerator(
    rotation_range=30, width_shift_range=0.15, height_shift_range=0.05, horizontal_flip=True)
val_datagen = ImageDataGenerator(rotation_range=30, width_shift_range=0, height_shift_range=0, horizontal_flip=False)

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(3))
model.add(Activation('softmax'))

optimizer = Adam(lr=0.0001)
model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])
model.summary()

model.fit_generator(train_datagen.flow(X_train, Y_train, batch_size=BATCH_SIZE, shuffle=True),
                    validation_data=val_datagen.flow(X_val, Y_val, batch_size=BATCH_SIZE, shuffle=True),
                    steps_per_epoch=len(Y_train) / BATCH_SIZE,
                    nb_val_samples = X_val.shape[0],
                    epochs=EPOCHS,
                    callbacks=[tensorboard, checkpoints])

#to jest na wszelki wypadek
model.save('64x3-CNN.model')


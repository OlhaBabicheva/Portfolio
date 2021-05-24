import face_recognition
import numpy as np
import cv2
import tensorflow as tf

# Get a reference to webcam #0 (the default one)
webcam = cv2.VideoCapture(0)
model = tf.keras.models.load_model("64x3-CNN.model")
#choose the best model in folder weights or just use final model "64x3-CNN.model"
# Load a sample picture and learn how to recognize it.
your_image = face_recognition.load_image_file("saved_img.png")
your_face_encoding = face_recognition.face_encodings(your_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    your_face_encoding
]
known_face_names = [
    "You"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = webcam.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        def prepare_face(face):
            IMG_SIZE = 64
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            face = cv2.resize(face, (IMG_SIZE, IMG_SIZE))
            return face.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

        CATEGORIES = ["neutral", "sad", "smiling"]
        face = frame[top:bottom, left:right, :]
        resized_face = prepare_face(face) / 255
        prediction = model.predict([resized_face])
        output_class = np.argmax(prediction[0])
        cv2.putText(frame, (CATEGORIES[output_class]), (left + 6, bottom - 300), font, 1.0, (255,255,255), 1)
        if (CATEGORIES[int(prediction[0][0])]) == 'smiling':
            cv2.putText(frame, "Lista filmow: Joker, Zielona mila, Forrest Gump", (left + 6, bottom - 350), font, 0.4, (255, 255, 255), 1)
        elif (CATEGORIES[int(prediction[0][0])]) == 'neutral':
            cv2.putText(frame, "Lista filmow: Wladca Pierscieni, Gra o Tron", (left + 6, bottom - 350), font, 0.4, (255, 255, 255), 1)
        else:
            cv2.putText(frame, "Lista filmow: Avengers, Guardians of the galaxy, Inglourious Basterds", (left + 6, bottom - 350), font, 0.4, (255, 255, 255), 1)
    # Display the resulting image
    cv2.imshow('Webcam', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
webcam.release()
cv2.destroyAllWindows()
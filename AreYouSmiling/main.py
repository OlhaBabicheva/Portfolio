import os
import cv2

photo = os.path.exists('./saved_img.png')

if photo == True:
    exec(open('webcam.py').read())

else:
    print("Please, take your photo before starting the main script. Just press s on your keyboard to save picture.")
    exec(open('photo.py').read())

if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Program ended.")
            cv2.destroyAllWindows()
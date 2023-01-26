import cv2
import os
import time
import uuid

IMAGES_PATH='tensorflow/workspace/images/collectedimages'

number_imgs = 15
label=input('Enter label to be collected:')

print('collecting'+label)
time.sleep(2)
for imgnum in range(number_imgs):
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    imgname = os.path.join(label+'{}.jpg'.format(str(uuid.uuid1())))
    cv2.imshow("Capturing", frame)
    cv2.imwrite(filename=imgname, img=frame)
    webcam.release()
    cv2.destroyAllWindows()
    print(label,imgnum)
    time.sleep(2)
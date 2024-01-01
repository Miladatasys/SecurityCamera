import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Create a mask that captures areas of the frame within the green range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', hsv)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''BGR_color = np.array([[[0, 255, 0]]])
color = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
color[0][0]'''

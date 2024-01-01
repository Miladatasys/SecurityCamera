import numpy as np 
import cv2

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read() 
    width = int(cap.get(3)) # width property of my videocapture
    height = int(cap.get(4)) # height of my videocapture

    image = np.zeros(frame.shape, np.uint8) 
    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)

    '''
    the : (colon) and // (floor division) are used for slicing and dividing the image into different sections. 
    '''
    # Place smaller frames in four quadrants of the image and rotate some of them
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top-left
    image[height//2:, :width//2] = smaller_frame  # Bottom-left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) 
    image[height//2:, width//2:] = smaller_frame  # Bottom-right

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): 
        break  

cap.release() 
cv2.destroyAllWindows()
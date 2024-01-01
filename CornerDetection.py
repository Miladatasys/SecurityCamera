import numpy as np
import cv2

img = cv2.imread('assets/chess.jpg')
img = cv2.resize(img, (0,0), fx = 0.60, fy = 0.60)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Use the Shi-Tomasi corner detection method to find corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

# Draw circles around detected corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 5, (0, 0, 255), -1)

# Connect the detected corners with lines
for i in range(len(corners)):
    for j in range(i +1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])

        # Generate a random color for each line using lambda
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size = 3)))
        cv2.line(img, corner1, corner2, color, 1)


cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Shi-Tomasi is a corner detection algorithm that selects prominent corners in an image based on a scoring function.
cv2.goodFeaturesToTrack detects corners in an image using the Shi-Tomasi method.
lambda is an Anonymous function used for concise operations. Here, it's used to map random values to a tuple for color generation.
'''
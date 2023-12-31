import random
import cv2

img = cv2.imread('assets/hyperballad.png', -1)# Load the image
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)

'''
Red (First Value): Intensity of the red color component.
Green (Second Value): Intensity of the green color component.
Blue (Third Value): Intensity of the blue color component.
Alpha (Fourth Value): The transparency level of the pixel.
'''
for i in range(100):# change the pixel color for the first 100 rows of my image
    for j in range(img.shape[1]):# change the pixel color for every column of each of those rows 
        img[i][j] = [random.randint(0,255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Select a region of the image
# Here, y1:y2 is the vertical range and x1:x2 is the horizontal range
tag = img[50:150, 50:150]
img[200:300, 200:300] = tag # Assign region to a new location


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

# Load and resize the main image
img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)

# Load and resize the template image
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.8, fy=0.8)

# Get the height and width of the template
h, w = template.shape

# Define different template matching methods to try
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Loop over each template matching method
for method in methods:
    # Create a copy of the main image
    img2 = img.copy()

    # Apply template matching
    result = cv2.matchTemplate(img2, template, method)

    # Find the location with the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Determine the location based on the matching method used
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # Calculate the bottom-right corner of the rectangle
    bottom_right = (location[0] + w, location[1] + h)

    # Draw a rectangle around the detected template
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    # Display the result with the rectangle
    cv2.imshow('Match', img2)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


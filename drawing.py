import cv2

# Initialize video capture from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break  # Exit if frame is not read correctly

    # Get the dimensions of the video frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Draw a green line from top-left to bottom-right
    img = cv2.line(frame, (0,0), (width, height), (0, 255, 0), 6)
    # Draw a red line from bottom-left to top-right
    img = cv2.line(img, (0, height), (width, 0), (255, 0, 0), 3)

    # Draw a gray rectangle from (200, 200) to (300, 300)
    img = cv2.rectangle(img, (200, 200), (300, 300), (140, 140, 140), 3)

    # Draw a filled blue circle with center at (400, 400) and radius 60
    img = cv2.circle(img, (400, 400), 60, (0, 0, 255), -1)

    # Define font for text and add 'Aprendo' near the bottom-left corner
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Aprendo', (10, height -10), font, 4, (0,0, 0), 5, cv2.LINE_AA)

    # Display the modified frame
    cv2.imshow('frame', img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

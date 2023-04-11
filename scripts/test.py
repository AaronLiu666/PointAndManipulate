import cv2

# Load the image
image = cv2.imread('example/demo/oneimage/1.jpeg')

# Display the image
cv2.imshow('Image', image)

# Draw a red circle on the image
point = (100, 100)
radius = 10
color = (0, 0, 255) # BGR format
thickness = -1 # Negative thickness fills the circle
cv2.circle(image, point, radius, color, thickness)

# Display the image with the circle
cv2.imshow('Image with Circle', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

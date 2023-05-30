import cv2
import numpy as np

# Load the grayscale image
img_gray = cv2.imread('image\kucingbelang.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the first and second derivatives using Sobel operator
dx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
dy = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
dxx = cv2.Sobel(img_gray, cv2.CV_64F, 2, 0, ksize=3)
dyy = cv2.Sobel(img_gray, cv2.CV_64F, 0, 2, ksize=3)

# Calculate the edge strength and direction using compass operator
magnitude = np.sqrt(dx**2 + dy**2)
theta = np.arctan2(dy, dx) * 180 / np.pi

# Threshold the magnitude to obtain the edge pixels
threshold = 50
edge_pixels = magnitude > threshold

# Display the edge pixels and magnitude
cv2.imshow('Edges / Pixel Tepi', edge_pixels.astype(np.uint8) * 255)
cv2.imshow('Magnitude / Magnituro ', magnitude / np.max(magnitude))
cv2.imshow('Direction / Arah Tepi', theta / 180)
cv2.waitKey(0)
cv2.destroyAllWindows()

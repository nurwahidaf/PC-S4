import cv2

img = cv2.imread('logo-nf.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
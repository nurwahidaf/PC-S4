import cv2
import numpy as np

img = cv2.imread('img/marin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, biner = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Citra Warna RGB", img)
cv2.imshow("Citra Grayscale", gray)
cv2.imshow("Citra Biner", biner)

cv2.waitKey()
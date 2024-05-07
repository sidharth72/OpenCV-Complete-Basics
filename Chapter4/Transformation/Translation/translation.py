import cv2 as cv
import numpy as np

# Translation of an image will 

img = cv.imread('D:/OpenCV/Assets/newton.jpg')

dx = 50
dy = 30

translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])

translated_image = cv.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))

cv.imshow('window', translated_image)

cv.waitKey(0)
cv.destroyAllWindows()
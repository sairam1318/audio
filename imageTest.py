import cv2
  
image = cv2.imread('hai.png')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, bwimage) = cv2.threshold(grayImage, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('show', image)
cv2.imshow('Gray', grayImage)
cv2.imshow('blackAndWhite', bwimage)
cv2.waitKey(0) 
cv2.destroyAllWindows()
#This will convert a normal colored (RGB) image to almost real-life sketch

import cv2
#Getting Image
img_location = 'C:/Users/Sanket/Desktop/'
filename = 'testme.jpg'

#read image
img = cv2.imread(img_location+filename)

#grayscale conversion
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#inverted gray
inverted_gray = 255 - img_gray

#Blur gray
img_blur = cv2.GaussianBlur(inverted_gray,(21,21),0)

#inverted blur gray
inverted_blur_gray = 255 - img_blur

#pencil sketch
pencil_sketch =cv2.divide(img_gray,inverted_blur_gray,scale=256.0)

#show image
cv2.imshow('Original image',img)

cv2.imshow('New image',pencil_sketch)

cv2.waitKey(0)


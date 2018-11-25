# Image-Processing
Image Processing Basics
You beed Open CV, Numpy and Matplotlib libraries to be able process the iamges

## Important


```bash 
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('O1.jpg')
kernel = np.ones((5,5),np.uint8)
```


## Erosion and Dilation
```bash
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
```
## Opening and Closing
```bash
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```
## Gradient
```bash
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
```
## Gamma Correction
```bash
img = cv2.pow(img, correction)
```
## Smoothening
```bash
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
```



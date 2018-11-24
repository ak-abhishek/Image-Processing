import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('O1.jpg')
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(122),plt.imshow(opening),plt.title('Opeing')
plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(closing),plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.show()
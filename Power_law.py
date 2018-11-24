import numpy as np
import os
import cv2
def gamma(image,gamma = 0.5):
    	img_float = np.float32(image)
    	max_pixel = np.max(img_float)
    	#image pixel normalisation
    	img_normalised = img_float/max_pixel
    	#gamma correction exponent calulated
    	gamma_corr = np.log(img_normalised)*gamma
    	#gamma correction being applied
    	gamma_corrected = np.exp(gamma_corr)*255.0
    	#conversion to unsigned int 8 bit
    	gamma_corrected = np.uint8(gamma_corrected)
    	return gamma_corrected
def logt(image):
    img_float = np.float32(image)
    max_pixel = np.max(img_float)
    #log correction being caluclated
    log_corrected = (255.0*np.log(1+img_float))/np.log(1+max_pixel)
    #conversion to unsigned int 8 bit
    log_corrected = np.uint8(log_corrected)
    return log_corrected
def main():
	img=cv2.imread('O1.jpg',0)
	cv2.imshow('image1',img)
	cv2.waitKey(10000)
	cv2.imwrite("gray.jpg", img)
	im_2=gamma(img,0.2)
	cv2.imshow('image2',im_2)
	cv2.waitKey(10000)
	cv2.imwrite("gamma0_2.jpg",im_2)
	im_4=gamma(img,0.4)
	cv2.imshow('image3',im_4)
	cv2.waitKey(10000)
	cv2.imwrite("gamma0_4.jpg",im_4)
	im2=gamma(img,2)
	cv2.imshow('image4',im2)
	cv2.waitKey(10000)
	cv2.imwrite("gamma2.jpg",im2)
	im4=gamma(img,4)
	cv2.imshow('image5',im4)
	cv2.waitKey(10000)
	cv2.imwrite("gamma4.jpg",im4)
	#imlog=logt(img)
    #cv2.imshow('image6',imlog)
    #cv2.waitKey(10000)
    #cv2.imwrite("log.jpg",imlog)
if __name__=="__main__":
    main()   

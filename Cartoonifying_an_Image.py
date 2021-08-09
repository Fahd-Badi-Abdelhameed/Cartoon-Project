###############################################################################	
# File Name    	: 	Cartoonifying_an_Image.py    		                      #
# Author       	: 	Fahd Badi                                                 #
# Version      	: 	1.0.0                                                     #
# Origin Date  	: 	30/05/2020                                                #   
# Notes        	: 	None                                                      #
###############################################################################

import cv2

img     = cv2.imread('orig.jpg')
greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur  = cv2.medianBlur(greyImg, 5)
edges = cv2.adaptiveThreshold(blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)

color   = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imwrite('cartoon1.jpg',cartoon)  
cv2.imshow ('image', img)
cv2.imshow ('cartoon', cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()

###############################################################################
################################ END OF PROGRAM ###############################
###############################################################################
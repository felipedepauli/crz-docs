import cv2
import numpy




image = cv2.imread("media/Narutim.jpg")


cv2.imshow("Narutim", image)
cv2.waitKey(0)



flipped = cv2.flip(image, 1)


cv2.imshow("Narutim", flipped)
cv2.waitKey(0)



flipped = cv2.flip(image, 0)


cv2.imshow("Narutim", flipped)
cv2.waitKey(0)


flipped = cv2.flip(image, -1)


cv2.imshow("Narutim", flipped)
cv2.waitKey(0)


flipped = cv2.flip(image, 0)
flipped = cv2.flip(flipped, 1)


cv2.imshow("Narutim", flipped)
cv2.waitKey(0)

import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

parse = argparse.ArgumentParser()

parse.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(parse.parse_args())
image = cv2.imread(args["image"])

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get the histogram of the image
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.plot(hist)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray)

# All pixels value greater than 100 will be set to the setValue;
# Otherwise, it will be set to 0 (the light pixels will be white and the dark pixels will be black).
setValue = 255
(T, thresh) = cv2.threshold(gray, 100, setValue, cv2.THRESH_BINARY)
print("Threshold value: {}".format(T))

cv2.imshow("Threshold Image Normal", thresh)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# All pixels value less than 100 will be set to the setValue:
# Otherwise, it will be set to 0 (then light pixels will be black and the dark pixels will be white).
(T, thresh) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
print("Threshold value: {}".format(T))

cv2.imshow("Threshold Image Inverted", thresh)
cv2.waitKey(0)

# But who defines the threshold value?
# We have to look at the histogram of the image to determine the threshold value.
# But there is a better way to do this: Otsu's method.
# Otsu's method automatically calculates the threshold value.
# It is a good method for images with bimodal histograms.

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Otsu's method
(T, thresh) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("Threshold value: {}".format(T))

cv2.imshow("Threshold Image Otsu", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# And if the image has illumination problems, we can use adaptive thresholding.
# Adaptive thresholding divides the image into small regions and calculates the threshold value for each region.
# This method is good for images with uneven illumination.

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Adaptive thresholding
thresh = cv2.adaptiveThreshold(
    gray,                       # Image
    255,                        # Output threshold value
    cv2.ADAPTIVE_THRESH_MEAN_C, # Adaptive method with mean weighting
    cv2.THRESH_BINARY,          # Binary thresholding which will be combined with the adaptive method
    21,                         # Pixel neighborhood size (21 x 21)
    4
)
cv2.imshow("Adaptive Thresholding - Mean", thresh)
thresh = cv2.adaptiveThreshold(
    gray,                           # Image
    255,                            # Output threshold value
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, # Adaptive method with Gaussian weighting
    cv2.THRESH_BINARY,              # Binary thresholding which will be combined with the adaptive method
    21,                             # Pixel neighborhood size
    4
)
cv2.imshow("Adaptive Thresholding - Gaussian", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


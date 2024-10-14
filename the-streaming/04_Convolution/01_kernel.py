import numpy as np
import argparse
import cv2
from skimage.exposure import rescale_intensity

def convolve(image, kernel):
    # Get the spatil dimensions of the image along the spacial dimensions of the kernel
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]
    
    # We need to set the pad size, which is the counting of the cells from begin to the center, without the center
    pad = (kW - 1) // 2
    
    # Now we create a new image with the borders (the new borders will be the same of the actual borders)
    image_with_pad = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    
    output = np.zeros((iH, iW), dtype="float32")
    
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = image_with_pad[y-pad : y+pad+1 , x-pad : x+pad+1]
            k = (roi * kernel).sum()
            
            output[y-pad, x-pad] = k
    
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
    return output

parser = argparse.ArgumentParser(description="Iewi")
parser.add_argument("--image", help="Image to convolute", type=str, default="")
args = parser.parse_args()
image_path = args.image

image = cv2.imread(image_path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

convolveOutput = convolve(image_gray, np.array([[1,1,1], [1, 1, 1], [1, 1, 1]], dtype="float32"))

cv2.imshow("owowow", convolveOutput)
cv2.waitKey()
cv2.destroyAllWindows()


def test_filter(image, title, filter):
    convolve_output = convolve(image, np.array(filter))
    cv2.imshow(title, convolve_output)
    cv2.waitKey(0)

###############################
# Filters
small_blur = np.ones((7,7), dtype="float32") * (1.0 / (7*7))
test_filter(image_gray, "Small Blur", small_blur)

large_blur = np.ones((21, 21), dtype="float32") * (1.0 / (21*21))
test_filter(image_gray, "Large Blur", large_blur)

sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")
test_filter(image_gray, "Sharpen", sharpen)
sharpen = np.array((
	[0, -2, 0],
	[-2, 9, -2],
	[0, -2, 0]), dtype="int")
test_filter(image_gray, "Sharpest", sharpen)

# construct the Laplacian kernel used to detect edge-like
# regions of an image
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
test_filter(image_gray, "Laplaciano", laplacian)
# construct the Sobel x-axis kernel
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
test_filter(image_gray, "Sobel X", sobelX)
# construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")
test_filter(image_gray, "Sobel Y", sobelY)
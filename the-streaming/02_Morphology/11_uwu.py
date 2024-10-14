import argparse
import numpy as np
import cv2
import os

parser = argparse.ArgumentParser(description="Amazing program")
parser.add_argument("-i", "--image", type=str, help="Path to the image")
args = parser.parse_args()
image_path = args.image

PATH_TO_MEDIA = os.environ.get("PATH_TO_MEDIA", "")
image_path = os.path.join(PATH_TO_MEDIA, image_path)
print(image_path)

image = cv2.imread(image_path)

height, width = image.shape[:2]
aspect_ratio = height/width

width = 600
img = cv2.resize(image, (int(width*aspect_ratio), width), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Narutim", img)
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Narutim", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, 3):
    eroded = cv2.erode(image_gray.copy(), None, iterations=i*3)
    cv2.imshow(f"Let's see! Eroded {i+1}", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, 3):
    dilated = cv2.dilate(image_gray.copy(), None, iterations=i*3)
    cv2.imshow(f"Let's look now to the dialate {i}", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, 3):
    dilate_the_eroded = cv2.dilate(eroded, None, iterations=i*3)
    cv2.imshow(f"Dilate the eroded image {i}", dilate_the_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
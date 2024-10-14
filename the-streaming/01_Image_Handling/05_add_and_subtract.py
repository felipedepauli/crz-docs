#!/bin/env python

import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("image", help="Path to the image")
args = parser.parse_args()


image = cv2.imread(args.image)

add_matrix = np.ones(image.shape, dtype="uint8") * 100
sub_matrix = np.ones(image.shape, dtype="uint8") * 50


added = cv2.add(image, add_matrix)
subtracted = cv2.subtract(added, sub_matrix)

cv2.imshow("Narutim", image)
cv2.imshow("Added", added)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)

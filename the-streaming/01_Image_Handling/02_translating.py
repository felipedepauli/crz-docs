import numpy as np
import cv2
import argparse
import os

MEDIA = os.environ.get("MEDIA")

parser = argparse.ArgumentParser(description="Cé dioidia!")
parser.add_argument("-i", "--image", type=str, default=None, help="Image da parada!")
args = parser.parse_args()

image = cv2.imread(os.path.join(MEDIA, args.image))

cv2.imshow("Catinho", image)
cv2.waitKey(0)
cv2.destroyAllWindows()




M = np.float32([[1, 0, 10], [0, 1, 30]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Slk, cachoeira", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()


M = np.float32([[np.cos(theta), -np.sin(theta)], [0, 1, 30]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Slk, cachoeira", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import argparse
import imutils
import sys
import os

parser = argparse.ArgumentParser(description="Iew")
parser.add_argument("-i", "--image", type=str, default=None, help="Give me an image")
args = parser.parse_args()

if not args.image:
    print("You must to give me an image!")
    sys.exit()
print(args.image)


image_path = os.environ.get("MEDIA", "./media")

image = cv2.imread(os.path.join(image_path, args.image))

cv2.imshow("The Image!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Write a rectangle on the Naruto's Face
cv2.rectangle(image, (200, 25), (410, 220), (0, 255, 255), 5)

cv2.imshow("Where is the WallyImage?", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

naruto = image[25:220,200:410]

cv2.imshow("Narutim!", naruto)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Resize the Narutim
height, width, _ = naruto.shape

print(width, "x", height)

ar = width/height

print("Aspect ratio:", ar)


naruto_resized = cv2.resize(naruto, (int(ar*2*width), 2*width), interpolation=cv2.INTER_AREA) 
cv2.imshow("Narutim, but bigger!", naruto_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

methods = [
  ("cv2.INTER_NEAREST" , cv2.INTER_NEAREST),
  ("cv2.INTER_LINEAR"  , cv2.INTER_LINEAR),
  ("cv2.INTER_AREA"    , cv2.INTER_AREA),
  ("cv2.INTER_CUBIC"   , cv2.INTER_CUBIC),
  ("c2.INTER__LACZ0S4" , cv2.INTER_LANCZOS4),
]

for (name, method) in methods:
    print("[INFO] {}", format(name))
    resized = imutils.resize(naruto, width=int(image.shape[1]*ar), inter=method)
    cv2.imshow(f"Method: {name}", resized)
    cv2.waitKey(0)

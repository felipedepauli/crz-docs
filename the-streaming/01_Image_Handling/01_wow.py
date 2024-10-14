import numpy as np
import cv2
import argparse
import os

MEDIA = os.environ.get('MEDIA')

if not MEDIA:
    MEDIA = "./media"
    
parser = argparse.ArgumentParser(description="Slk!")

parser.add_argument("-i", "--image", type=str, default=None, help="Image to parse")

args = parser.parse_args()

image = cv2.imread(os.path.join(MEDIA, args.image))




cv2.rectangle(image, (210, 50), (400, 220), (255, 255, 0), 3)

cv2.circle(image, (210, 480), 90, (0, 255, 255), 3)








cv2.imshow("Narutim", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



my_canvas = np.zeros((600,600, 3), dtype="uint8")
cv2.rectangle(my_canvas, (10, 10), (100, 100), (0, 255, 255), -1)

cv2.circle(my_canvas, (60,60), 10, (255, 0, 0), cv2.FILLED)


cv2.ellipse(my_canvas, (200, 200), (100, 50), 0, 0, 180, (20, 200, 20), cv2.FILLED)
cv2.ellipse(my_canvas, (200, 200), (100, 50), 90, 0, 180, (200, 200, 20), cv2.FILLED)
cv2.ellipse(my_canvas, (200, 200), (100, 50), 180, 0, 180, (200, 20, 20), cv2.FILLED)




pts = np.array([
    [100, 100],
    [200, 200],
    [300, 200],
    [300, 300],
    [200, 300]
], np.int32)

cv2.polylines(my_canvas, [pts], True, (20, 10, 30), 10)

cv2.imshow("Canvas", my_canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()



# while(1):
#     cv2.imshow("Canvas", my_canvas)
#     cv2.waitKey(1)
    

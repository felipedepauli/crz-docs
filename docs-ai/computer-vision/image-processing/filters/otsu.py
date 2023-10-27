import numpy as np
import cv2

# Otsu thresholding is a technique used to segment image. It transform an gray image
# into a binary image (black and white). It is based on the histogram of the image
# and the Otsu method. The Otsu method assumes that the image contains two classes
# with equal probability. It then calculates the optimum threshold separating the two
# classes.

# Create a binary image could be easy using a threshold, but Otsu does more. It
# calculates the optimum threshold separating the two classes. This is useful when
# there are more than two classes. It is also useful when the image has a higher
# contrast.

# Carregue a imagem original
img = cv2.imread("/home/fpauli/git/crz-docs/docs-ai/computer-vision/common/media/pics/gatinhos/02.jpeg")

cv2.imshow("Original", img)

# Converta a imagem para tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplique o threshold
ret, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Threshold", threshold)
cv2.waitKey(0)

# Inverta a máscara
inverted_threshold = 255 - threshold

# Use a máscara invertida para recortar a imagem original colorida
img_cut = cv2.bitwise_and(img, img, mask=inverted_threshold)

cv2.imshow("Cut", img_cut)
cv2.waitKey(0)

import cv2
print(f'[INFO] Opencv version = {cv2.__version__}')

import numpy as np
import time
import os
import matplotlib.pyplot as plt
import zipfile

# Load YOLO
print("[INFO] These are the classes in the COCO dataset:")
labels_path = os.path.sep.join(["../common/yolo/classes", "coco.names"])
LABELS = open(labels_path).read().strip().split("\n")

print(LABELS)
print(f'[INFO] There are {len(LABELS)} classes in the COCO dataset.')

weights_path = os.path.sep.join(["../common/yolo/v4", "yolov4.weights"])
config_path  = os.path.sep.join(["../common/yolo/v4", "yolov4.cfg"])

print("[INFO] Weights path:", weights_path)
print("[INFO] Config path:", config_path)

net = cv2.dnn.readNet(config_path, weights_path)
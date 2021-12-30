#!/usr/bin/env python3

import cv2
import glob

for fname in glob.glob("*.png"):
  src = cv2.imread(fname)
  cv2.imwrite("red_" +fname, src[:,:,2])

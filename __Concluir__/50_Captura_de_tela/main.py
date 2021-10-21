# pip install opencv-python
import numpy as np
import cv2
import pyautogui

image = pyautogui.screenshot()

image = cv2.cvtColor(np.array(image), cv2.COLOR_RBG2BGR)

cv2.imwrite("print.png", image)

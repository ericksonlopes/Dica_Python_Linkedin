# pip install opencv-python
# pip install numpy
# pip install pyautogui

import numpy as np
import cv2
import pyautogui

image = pyautogui.screenshot()

image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

cv2.imwrite("print.png", image)

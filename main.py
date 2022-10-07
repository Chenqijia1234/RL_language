# from Interpreter_RL import interpre
#
# it = interpre.Interpreter()
# it.run_loop()

import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile(r"./c.JPG"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
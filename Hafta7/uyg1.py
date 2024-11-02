import cv2
import numpy as np
from matplotlib import pyplot as plt

gri = cv2.imread("kus.jpg", 0)
cv2.imshow("Kus Resmi", gri)
cv2.waitKey()

print(len(gri))

hist_gray = cv2.calcHist([gri], [0], None, [256], [0,256]) #gri görüntü histogram hesaplama

plt.figure(2)
plt.plot(hist_gray)
plt.show()
    

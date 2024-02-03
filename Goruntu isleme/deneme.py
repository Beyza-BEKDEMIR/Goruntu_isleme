import numpy as np
import matplotlib.pyplot as plt
import cv2

resim=cv2.cvtColor(cv2.imread("ekran.png"), cv2.COLOR_BGR2GRAY)
cv2.imshow("resim", resim)

hist=cv2.calcHist([resim],[0], None, [256], [0,255])
plt.plot(hist)
plt.show()

esik=127 #eşik değerini histograma bakarak belirle. 127 den küçükleri siyah, büyükleri beyaz yapar.
ret,thresh=cv2.threshold(resim, esik, 255, cv2.THRESH_BINARY)
print(ret)

cv2.imshow("sonuc", thresh)
cv2.waitKey()

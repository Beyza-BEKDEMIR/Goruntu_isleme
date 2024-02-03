import cv2

resim = cv2.imread("ekran.png")
cv2.imshow("goruntule", resim)

griresim=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("goruntule2", griresim)

Blue=resim[:,:,0]
Green=resim[:,:,1]
Red=resim[:,:,2]

cv2.imshow("green band", Green)
cv2.imshow("blue band", Blue)
cv2.imshow("red band", Red)

histogram=cv2.calcHist(griresim, [0], None, [256], [0,255])

import matplotlib.pyplot as plt
plt.plot(histogram)
plt.title("Histogram")
plt.show()

cv2.waitKey()
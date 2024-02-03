import cv2
import matplotlib.pyplot as plt
import numpy as np

resim = cv2.imread("ekran.png")
griresim=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("griresim", griresim)

histogram=cv2.calcHist(griresim, [0], None, [256], [0,255])
plt.plot(histogram)
plt.show()

esik_deger=150
yeniresim=np.zeros_like(griresim)
for i in range(griresim.shape[0]):
    for j in range(griresim.shape[1]):
        if(griresim[i][j]>esik_deger):
            yeniresim[i][j]=255
        else:
            yeniresim[i][j]=0

cv2.imshow("yeni resim", yeniresim)

# VEYA--> trh, yeniresim=cv2.threshold(yeniresim,esik_deger,255,cv2.THRESH_BINARY)

cv2.waitKey()
import cv2
import matplotlib.pyplot as plt
import numpy as np

resim = cv2.imread("ekran.png")
griresim=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("griresim", griresim)

filtre=np.array(([1,1,1],
                [1,1,1],
                [1,1,1]))/9

sonuc_resim=cv2.filter2D(src=griresim, ddepth=-1, kernel=filtre)
cv2.imshow("filtreleme", sonuc_resim)

filtre2=np.array(([1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1]))/25

sonuc2=cv2.filter2D(src=griresim, ddepth=-1, kernel=filtre2)
cv2.imshow("5x5 ortalama", sonuc2)

sonuc3=cv2.blur(src=griresim, ksize=(3,3)) #ksize değeri arttıkça bulanıklaşır.
cv2.imshow("3x3 blur", sonuc3)

sonuc4=cv2.GaussianBlur(src=griresim, ksize=(5,5), sigmaX=1)
cv2.imshow("5x5 Gaussian", sonuc4)

sonuc5=cv2.Sobel(src=griresim, ddepth=-1, dx=1, dy=0)
cv2.imshow("Sobel", sonuc5)

sonuc6=cv2.Canny(griresim,50,150)
cv2.imshow("Canny", sonuc6)
cv2.waitKey()
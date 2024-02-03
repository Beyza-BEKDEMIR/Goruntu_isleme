import numpy as np
import matplotlib.pyplot as plt
import cv2

resim=cv2.cvtColor(cv2.imread("ekran.png"), cv2.COLOR_BGR2GRAY)
cv2.imshow("resim", resim)

hist=cv2.calcHist([resim],[0], None, [256], [0,255])
plt.plot(hist)
plt.show()

esik=133 #esik değeri histograma bakarak belirle
sonuc=resim   #threshold fonksiyonunu kullanmadan manuel olarak yapma
sonuc[sonuc<133]=0 #75 den küçük olan değerler 0, büyük olanlar beyaz olur.
sonuc[(sonuc<133) & (resim<210)]=127
sonuc[sonuc>=210]=255 


cv2.imshow("sonuc", sonuc)
cv2.waitKey()

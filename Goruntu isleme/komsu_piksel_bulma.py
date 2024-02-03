import cv2
import numpy as np
import matplotlib.pyplot as plt

resim=cv2.cvtColor(cv2.imread("coins.png"), cv2.COLOR_BGR2GRAY)
#cv2.imshow("coins", resim)

esik=10 #eşik değerini belirleyerek ve bu eşik değeri üzerinden bir kontrol yaparak komşu piksellerin belirlenmesini sağlar. 

N=np.array([[100,100]])  #mevcut pikselin sol ve sağdaki değerleri kontrol edilir.

if np.abs(resim[N[0,0], N[0,1]] - resim[N[0,0]-1, N[0,1]]) <= esik: #soldaki komşu pikseli bulur. 
    N=np.append(N, [[N[0,0]-1, N[0,1]]], axis=0)

if np.abs(resim[N[0,0], N[0,1]] - resim[N[0,0]+1, N[0,1]]) <= esik: #sağdaki komşu pikseli bulur.
    N=np.append(N, [[N[0,0]+1, N[0,1]]], axis=0)

print(N) #N nin komşu piksellerini de yazdırır.
#ilk başta N dizisinde sadece [100,100] dizisi vardır if kontrolünden sonra bu dizinin komşu pikselleri elde edilip yazdırılır.

for piksel in N: 
    print(resim[piksel[0], piksel[1]]) # piksellerin değerlerini yazdırır.Mesela [100,100] pikselinin değeri=113 gibi
#piksel[0]=satır piksel[1]=sütun

#cv2.waitKey(0)
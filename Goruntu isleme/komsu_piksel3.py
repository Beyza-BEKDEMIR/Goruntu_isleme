import cv2
import numpy as np
import matplotlib.pyplot as plt

resim=cv2.cvtColor(cv2.imread("coins.png"), cv2.COLOR_BGR2GRAY)
cv2.imshow("orjinal resim", resim)

N=np.array([[100,100]])  
esik=32 

def komsuKontrol(N,x,y): #komşu pikselleri tespit edip n dizisine ekliyor ve bu pikselleri beyaz yapıyor.

    current=resim[x,y]
    sag=resim[x+1,y]
    sol=resim[x-1,y]
    ust=resim[x,y-1]
    alt=resim[x,y+1]
    resim[x,y]=255

    if np.abs(current-sol)<=esik:
        N=np.append(N,[[x-1,y]], axis=0)
        #resim[x-1,y]=255

    if np.abs(current-sag)<=esik:
        N=np.append(N,[[x+1,y]], axis=0)
        #resim[x+1,y]=255 

    if np.abs(current-ust)<=esik:
        N=np.append(N,[[x,y-1]], axis=0)
        #resim[x,y-1]=255 

    if np.abs(current-alt)<=esik:
        N=np.append(N,[[x,y+1]], axis=0)
        #resim[x,y+1]=255 

    return N

N=komsuKontrol(N, N[0][0], N[0][1])

i=0
while i<len(N):
    N=komsuKontrol(N, N[i][0], N[i][1])
    i+=1
    if i>10000:       #N dizisine ekleme yapılacak ama i>10000 olursa ekleme yapmayı bırakacak.
        break         

print(len(N))

for piksel in N:
    resim[piksel[0], piksel[1]]=255

cv2.imshow("sonuc", resim.astype(np.int8))
cv2.waitKey(0)
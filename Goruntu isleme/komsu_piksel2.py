import cv2
import numpy as np
import matplotlib.pyplot as plt

resim=cv2.cvtColor(cv2.imread("coins.png"), cv2.COLOR_BGR2GRAY)

N=np.array([[100,100]])  
esik=10 

current=resim[N[0][0], N[0][1]]
sag=resim[N[0][0]+1, N[0][1]]
sol=resim[N[0][0]-1, N[0][1]]
ust=resim[N[0][0], N[0][1]-1]
alt=resim[N[0][0], N[0][1]+1]

if np.abs(current-sol)<=esik:
    N=np.append(N,[[N[0,0]-1, N[0,1]]], axis=0)

if np.abs(current-sag)<=esik:
    N=np.append(N,[[N[0,0]+1, N[0,1]]], axis=0)  

if np.abs(current-ust)<=esik:
    N=np.append(N,[[N[0,0], N[0,1]-1]], axis=0)

if np.abs(current-alt)<=esik:
    N=np.append(N,[[N[0,0], N[0,1]+1]], axis=0)
print(N) 

for piksel in N: 
    print(resim[piksel[0], piksel[1]]) # piksellerin değerlerini yazdırır.Mesela [100,100] pikselinin değeri=113 gibi
#piksel[0]=satır piksel[1]=sütun

#cv2.waitKey(0)
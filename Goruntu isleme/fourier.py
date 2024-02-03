import cv2
import numpy as np

resim=cv2.imread("noiseball.png")

griresim=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("resim", griresim)

fourier=cv2.dft(np.float32(griresim), flags=cv2.DFT_COMPLEX_OUTPUT)  #fourier dönüşümü yapar.fft fourier dönüşümü yapar.
fourier_shift = np.fft.fftshift(fourier) #fftshift merkeze kaydırır (0,0) noktasını
magnitude = 20*np.log(cv2.magnitude(fourier_shift[:,:,0], fourier_shift[:,:,1]))

magnitude=cv2.normalize(magnitude, None, 0,255, cv2.NORM_MINMAX, cv2.CV_8UC1)
magnitude=cv2.resize(magnitude,[800,800])#yeniden boyutlandırdı resmi büyütmek için

inv_fft=np.fft.ifftshift(fourier_shift) #ters fouier ile orjinal resim elde edilir yani gürültüsüz resim
inv_image=cv2.idft(inv_fft)
norm_image=cv2.normalize((inv_image[:,:,1]), None,0,255, cv2.NORM_MINMAX, cv2.CV_8UC1)

cv2.imshow("fourier donusum", magnitude)
cv2.imshow("ters resim", norm_image)

cv2.waitKey()
cv2.destroyAllWindows()

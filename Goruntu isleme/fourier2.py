import cv2
import numpy as np

resim=cv2.imread("noiseball.png")

griresim=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("resim", griresim)

fourier=cv2.dft(np.float32(griresim), flags=cv2.DFT_COMPLEX_OUTPUT)  #fourier dönüşümü yapar.fft fourier dönüşümü yapar.
fourier_shift = np.fft.fftshift(fourier) #fftshift merkeze kaydırır (0,0) noktasını
#fourier_shift[255,255]=0
fourier_shift[179-2:179+2,183-3:183+4]=0 #resimdeki merkez dışında olan parlaklıkları yani gürültüleri yok etmek için sıfıraa eşitleriz o bölgeyi
fourier_shift[178-2:178+2,150-3:150+3]=0 
fourier_shift[80-2:80+2,172-3:172+3]=0 
fourier_shift[80-2:80+2,135-3:135+3]=0 

#fourier_shift[256-2:256+2,256-15:256+20]=0

magnitude = 20*np.log(cv2.magnitude(fourier_shift[:,:,0], fourier_shift[:,:,1]+1))
magnitude=cv2.normalize(magnitude, None, 0,255, cv2.NORM_MINMAX, cv2.CV_8UC1)
magnitude=cv2.resize(magnitude,[600,600])#yeniden boyutlandırdı resmi büyütmek için

inv_fft=np.fft.ifftshift(fourier_shift) #ters fouier ile orjinal resim elde edilir yani gürültüsüz resim
inv_image=cv2.idft(inv_fft)
inv_image = cv2.magnitude(inv_image[:, :, 0], inv_image[:, :, 1])
norm_image=np.uint8(cv2.normalize(inv_image, None, 0, 255, cv2.NORM_MINMAX))

cv2.imshow("fourier donusum", magnitude)
cv2.imshow("ters resim", norm_image)

cv2.waitKey()
cv2.destroyAllWindows()

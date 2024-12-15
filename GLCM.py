import os
import cv2
import numpy as np
from PIL import Image

# Resimlerin bulunduğu dizin
data_dir = r"C:\Users\Lenovo\OneDrive\Masaüstü\LBP_Yontemi\img"

# Dizindeki tüm resim dosyalarını alalım
image_files = [f for f in os.listdir(data_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Her resim için işlem yap
for image_file in image_files:
    # Resmin tam yolunu oluştur
    image_path = os.path.join(data_dir, image_file)

    try:
        # PIL ile resmi aç
        pil_image = Image.open(image_path)
        # PIL resmini numpy array'e çevir
        resim = np.array(pil_image)
    except Exception as e:
        print(f"Resim okunamadı: {image_path}. Hata: {e}")
        continue

    # Gri tonlamaya dönüştür
    gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

    GLCM = np.zeros((256, 256), dtype="float16")

    n, m = gri_resim.shape

    aci = 0
    uzaklik = 1

    if (aci == 0):
        distx = uzaklik
        disty = 0
    elif (aci == 45):
        distx = uzaklik
        disty = uzaklik
    elif (aci == 90):
        distx = 0
        disty = uzaklik

    for x in range(n - distx):
        for y in range(m - disty):
            kaynak = gri_resim[x, y]
            hedef = gri_resim[x + distx, y + disty]

            GLCM[kaynak, hedef] = GLCM[kaynak, hedef] + 1

    # GLCM'den öznitelikleri çıkar
    kontrast = 0
    enerji = 0
    homojenlik = 0
    entropi = 0
    ortalama_x = 0
    ortalama_y = 0
    standart_sapma_x = 0
    standart_sapma_y = 0
    korelasyon = 0

    # İlk önce GLCM üzerinde hesaplamaları yap
    for i in range(256):
        for j in range(256):
            if GLCM[i, j] > 0:  # Sıfır olmayan değerler için
                kontrast += (i - j) ** 2 * GLCM[i, j]
                enerji += GLCM[i, j] ** 2
                homojenlik += 1 / (1 + (i - j) ** 2) * GLCM[i, j]
                entropi = entropi + GLCM[i, j] * np.log(GLCM[i, j] + 0.01)

                ortalama_x += i * np.sum(GLCM[i, :])  # x için ortalama
                ortalama_y += j * np.sum(GLCM[:, j])  # y için ortalama

                standart_sapma_x += ((i - ortalama_x) ** 2) * np.sum(GLCM[i, :])
                standart_sapma_y += ((j - ortalama_y) ** 2) * np.sum(GLCM[:, j])
                korelasyon += (i * j * GLCM[i, j])  # Korelasyon hesaplaması

    # Standart sapmayı bul
    standart_sapma_x = np.sqrt(standart_sapma_x)
    standart_sapma_y = np.sqrt(standart_sapma_y)

    # Korelasyon hesapla
    korelasyon = (korelasyon - (ortalama_x * ortalama_y)) / (standart_sapma_x * standart_sapma_y)

    # Sonuçları yazdır
    print(f'Resim: {image_file}')
    print(f'Kontrast: {kontrast}')
    print(f'Enerji: {enerji}')
    print(f'Homojenlik: {homojenlik}')
    print(f'Entropi: {entropi}')
    print(f'Ortalama X: {ortalama_x}')
    print(f'Ortalama Y: {ortalama_y}')
    print(f'Standart Sapma X: {standart_sapma_x}')
    print(f'Standart Sapma Y: {standart_sapma_y}')
    print(f'Korelasyon: {korelasyon}')
    print('--------------------------')

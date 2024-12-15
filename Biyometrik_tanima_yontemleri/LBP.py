import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import os

# Komşularla karşılaştırma yaparak 0/1 değerini döndüren fonksiyon
def set_0_1(img, center, x, y):
    if x < 0 or y < 0 or x >= img.shape[0] or y >= img.shape[1]:
        return 0
    return 1 if img[x][y] >= center else 0

# LBP hesaplayan fonksiyon
def lbp_calculated_pixel(img, x, y):
    center = img[x][y]
    val_ar = []
    
    # 8 komşu pikselle karşılaştırma yapılıyor
    val_ar.append(set_0_1(img, center, x-1, y-1))  # top_left
    val_ar.append(set_0_1(img, center, x-1, y))    # top
    val_ar.append(set_0_1(img, center, x-1, y+1))  # top_right
    val_ar.append(set_0_1(img, center, x, y+1))    # right
    val_ar.append(set_0_1(img, center, x+1, y+1))  # bottom_right
    val_ar.append(set_0_1(img, center, x+1, y))    # bottom
    val_ar.append(set_0_1(img, center, x+1, y-1))  # bottom_left
    val_ar.append(set_0_1(img, center, x, y-1))    # left
    
    # İkili değeri ondalığa dönüştür
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
    
    return val

# Resimlerin bulunduğu dizin
data_dir = r"C:\Users\Lenovo\OneDrive\Masaüstü\LBP_Yontemi\img"

# Dizindeki tüm resim dosyalarını alalım
image_files = [f for f in os.listdir(data_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Her resim için işlem yap
for image_file in image_files:
    # Resmin tam yolunu oluştur
    image_path = os.path.join(data_dir, image_file)
    
    # Görüntüyü PIL ile oku ve numpy array'e çevir
    img_pil = Image.open(image_path)
    img_bgr = np.array(img_pil)

    # Görüntü başarıyla yüklendiyse işleme devam et
    if img_bgr is not None:
        # Gri tonlamaya çevir
        img_gray = np.array(img_pil.convert('L'))

        height, width = img_gray.shape

        # LBP görüntüsü için boş matris oluştur
        img_lbp = np.zeros((height, width), np.uint8)

        # Her piksel için LBP hesapla
        for i in range(0, height):
            for j in range(0, width):
                img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)

        # Orijinal ve LBP görüntüsünü görselleştir
        plt.figure(figsize=(10,5))
        plt.subplot(1, 3, 1)
        plt.imshow(img_bgr)
        plt.title('Orijinal Görüntü')

        plt.subplot(1, 3, 2)
        plt.imshow(img_lbp, cmap="gray")
        plt.title('LBP Görüntüsü')

        # LBP histogramını oluştur
        plt.subplot(1, 3, 3)
        plt.hist(img_lbp.ravel(), bins=256, range=(0, 256), density=True)
        plt.title('LBP Histogramı')

        # Görselleştirme
        plt.tight_layout()
        plt.show()
    else:
        print(f"Resim yüklenemedi: {image_path}")

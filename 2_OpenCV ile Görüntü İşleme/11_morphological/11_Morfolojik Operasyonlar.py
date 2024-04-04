import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("datai_team.jpg",0)
# resmi siyah beyaz olarak içeri aktarmayı sağlar 0
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cmap değeri siyah ve beyaz olarak görüntüyü gösteriyor
plt.figure(), plt.imshow(img,cmap="gray"), plt.axis("off"), plt.title("Orijinal Img")

# %% erozyon -> Sınırlar küçültülür ve bir kutucuk oluşturulur ve resim üzerinde dolaşır
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1) #iterations ->resime kaç kez erozyon yapılacağı
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")

# %%  genişleme dilation

result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genisleme")

# %% white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])# 0 ile 1 arasında random sayılar oluşturuyorum
#shape bize 3 tane değer döndürüyor ama şimdilik 2 değeri alsak yeterli
#height weidht (channel=rgb) 1080 1920 3
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("White Noise")

noise_img = whiteNoise + img # kendi resmimiz üzerine ekliyoruz
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("Img w White Noise")

# %% açılma -> Beyaz Gürültüyü azaltmak için kullanılır. 
'''
# açılma işlemi erozyon+genişleme işleminin art arda olmasıyla elde edilir
result1 = cv2.erode(noise_img.astype(np.float32), kernel, iterations = 1) #iterations ->resime kaç kez erozyon yapılacağı
plt.figure(), plt.imshow(result1, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")

result2 = cv2.dilate(result1, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Er+Gen")
'''
#burada açılma işlemi uygulanıyor ikisi şuan aynı işlemi yaptı.

opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Acilma")

# %% black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise")

black_noise_img = blackNoise + img 
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise Img")

# %% kapatma
# Kapatma işlemi genişleme + erozyon işlemlerinin sırasıyla yapılması ile elde edilir
'''
result1 = cv2.dilate(black_noise_img.astype(np.float32), kernel, iterations = 1) #iterations ->resime kaç kez erozyon yapılacağı
plt.figure(), plt.imshow(result1, cmap = "gray"), plt.axis("off"), plt.title("Genişletme")

result2 = cv2.erode(result1.astype(np.float32), kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genişletme+Erozyon")
'''
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Kapama")

# %% gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradyan")

























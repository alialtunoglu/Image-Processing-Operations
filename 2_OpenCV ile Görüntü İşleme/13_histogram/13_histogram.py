import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis)

print(img.shape)
# mask -> Maskeleme işlemi resmin belirli bir kısmını almakla ilgili
# histSize -> Histogram Boyutu 0 ile 255 arasında 256 tane değer olduğu için 
# ranges -> Aralık belirtiyoruz 0 ile 255 arasında diye 
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist)

# %%
color = ("b", "g", "r")
plt.figure()
for i, c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color = c)
    
# %%
golden_gate = cv2.imread("goldenGate.jpg")

golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate_vis)    
    
print(golden_gate.shape)

# %%
mask = np.zeros(golden_gate.shape[:2], np.uint8)
#resimdeki kadar sutun ve satır boyutunda olan sıfır matrisi oluşturuyoruz
plt.figure(), plt.imshow(mask, cmap = "gray")  

'''
#♦ Buradaki gibi zero ile belirli bölgeleri 255 olarak işaretliyoruz
zero = np.zeros((7,5))
zero[2:5, 2:4] = 255
zero
'''
mask[1500:2000, 1000:2000] = 255 
#1500 ile 2000 arasını alsın x ekseninde
#1000 ile 2000 arasını alsın y ekseninde  ve bunları 255(beyaz) yapsın diyoruz
plt.figure(), plt.imshow(mask, cmap = "gray") 

# %%
masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask = mask)
plt.figure(), plt.imshow(masked_img_vis, cmap = "gray") 

masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask = mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [0], mask = mask, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(masked_img_hist) 

# %%

imgg = cv2.imread("hist_equ.jpg")
cv2.imshow("winname", imgg) 
# imread fonksiyonu resmi bgr formatında alıyor ve imshow da aynı şekilde bgr formatında
# aldığı için resim normal gözüküyor 
# fakat plt.imshow ise resmi rgb formatında bekliyor ve bgr olarak gelen renkler b r ile 
# eşleşerek blue rengi red gibi gözükeceğinden renkler tersleşiyor
# düzeltmek için bgr2rgb dönüşümü yapmak gerekir Bunu yaptığımızda cv2 resmi rgb formata çevirmiş olur
# ve düşünüldüğü gibi plt için güzel bir şey olur fakat cv2.imshow yine değeri bgr olarak bekliyeceği için 
# bu sefer cv2.imshowda renkleri ters olur görüntünün

imgg_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(imgg_vis) 


#%%
# histogram eşitleme
# karşıtlık arttırma

img = cv2.imread("hist_equ.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray") 

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap = "gray") 

eq_img_hist = cv2.calcHist([eq_hist], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(eq_img_hist)




















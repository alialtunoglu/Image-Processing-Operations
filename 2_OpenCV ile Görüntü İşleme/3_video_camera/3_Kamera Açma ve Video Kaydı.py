import cv2
#open cv kütüphanesi


# capture
cap = cv2.VideoCapture(0) 
#0- default kamera masaüstünde olan kamera veya laptoptaki
#iki tane varsa 0 yada 1 hangi kamerayı kullanmak istersek


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #frame genişliğini alıyor resimler birer framedir 
#video art arda gelen framelerden oluşur
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#frame yüksekliğini alıyor
print(width, height)

# video kaydet
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))

while True:
    
    #cap nesnesi üzerinden frame okur burada cap nesnesi bir kamera
    #ret frame'nin gelip gelmediğini true false şeklinde doğrular hata olup olmadığını piksellerin tam gelip gelmediğini
    ret, frame = cap.read() #burada fonksiyon bir tuple döndürüyor yani 2 tane değer döndürüyor
    #değerlerden 1i ret ile eşleşecek olan true/false bir değer diğeri ise
    #okunan kareyi temsil eden bir NumPy dizisidir (matris). Eğer ret değeri True ise, frame içinde okunan kare bulunur. 
    cv2.imshow("Video",frame)
    
    '''
    cv2.imshow(): Bu fonksiyon, bir pencere oluşturur ve içine bir görüntü yerleştirir. 
    İlk parametre olarak pencerenin adını alır, ikinci parametre olarak ise gösterilecek görüntüyü alır.

    "Video": Bu, oluşturulan pencerenin adıdır. Pencerenin adı, bu adı kullanarak daha sonra 
    bu pencereyle etkileşimde bulunabilirsiniz.

    frame: Bu, gösterilecek görüntüdür. Bu örnekte, frame değişkeni kameradan okunan bir karedir 
    veya bir video dosyasından okunan bir karedir. frame değişkeni, bir NumPy dizisi
    olarak temsil edilir ve bir görüntüyü piksellerin değerleri olarak içerir.
    '''    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()


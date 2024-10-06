import cv2

resim = cv2.imread("cicek.jpg")
#resim = cv2.imread("cicek.jpg", 0)
#resim = cv2.imread("../Hafta 2/daire.png")  

cv2.imshow("Çiçek Resmi", resim)
cv2.imwrite("yeni.png", resim)

cv2.waitKey(0) # 0 dediğimizde kendi kapanmıyor ama 5000 dersek 5 sn ekran açık kalır
cv2.destroyAllWindows()


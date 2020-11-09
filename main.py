import cv2
import numpy as np

img = cv2.imread('galon1.jpg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range = np.array([50, 50, 190], dtype=np.uint8)
upper_range = np.array([106, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_range, upper_range)

kernel = np.ones((10,10),np.uint8)

#Buat di tebelin
dilation = cv2.dilate(mask,kernel,iterations = 1)

#buat itung
# contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#Kopi gambar asli ke variable resultImg
resultImg = (img).copy()

#Array kontur
contour = []
#Perulangan untuk kontur
for i in range(len(contours)):
    #Banyaknya kontur ke variable cnt
    cnt = contours[i]
    #Mencari radius untuk menggambar lingkaran
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    #Pusat lingkaran
    center = (int(x),int(y))
    #Gambar lingkaran
    resultImg = cv2.circle(resultImg,center,int(radius),(0,0,255),3)

    len(contour)
    #add text
    text = "Jumlah Galon : " + str(len(contours)) + " pcs"
    cv2.putText(resultImg, text, (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('images',resultImg)
    #simpan gambar
    cv2.imwrite('galon1-countors.jpg', resultImg)


while (1):
    k = cv2.waitKey(0)
    if (k == 27):
        break

cv2.destroyAllWindows()
import cv2
face_cascade=cv2.CascadeClassifier("D:\Python\supermarkets\Files\haarcascade_frontalface_default.xml")
img=cv2.imread("D:\Python\supermarkets\Files\rahul.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),5)

print(faces)
print(type(faces))

cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

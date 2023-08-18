import cv2

cap = cv2.VideoCapture(1)
goz = cv2.CascadeClassifier("/Users/ibrahimediz/Documents/GitHub/KordsaIntroML/opencv/cascade/eye.xml")
yuz = cv2.CascadeClassifier("/Users/ibrahimediz/Documents/GitHub/KordsaIntroML/opencv/cascade/face.xml")


while True:
    _,img = cap.read()
    gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    yuzler = yuz.detectMultiScale(gri,1.3,5)
    for x,y,w,h in yuzler:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roigri = gri[y:y+h,x:x+w]
        roiimg = img[y:y+h,x:x+w]
        gozler = goz.detectMultiScale(roigri,1.3,5)
        for ex,ey,ew,eh in gozler:
            cv2.rectangle(roiimg,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

    cv2.imshow("",img)
    if cv2.waitKey(3) &  0xFF == ord("e"):
        break 

cap.release()
cv2.destroyAllWindows()
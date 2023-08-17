import cv2

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier("facecascade.xml")

while True:
    _,img= cap.read()
    gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gri,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255), 2)
    cv2.imshow("",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

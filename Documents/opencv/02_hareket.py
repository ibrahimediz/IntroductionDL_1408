import cv2


cap = cv2.VideoCapture(1)

while True:
    _,img = cap.read()
    img[100:150,100:150] = [255,255,255]
    blur = cv2.GaussianBlur(img,(15,15),4)
    cv2.imshow("",img)
    cv2.imshow("blur",blur)

    
    if cv2.waitKey(2) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
### pip install opencv-python
### https://pythonprogramming.net/loading-images-python-opencv-tutorial/

import cv2

img = cv2.imread("/Users/ibrahimediz/Documents/GitHub/KordsaIntroML/57.png")

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img[20:30,50:100])
cv2.imshow("",img)

cv2.waitKey(0) 
cv2.destroyAllWindows()
# & 0xFF == ord("q")
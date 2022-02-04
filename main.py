import numpy as np 
import cv2
import time


cap=cv2.VideoCapture(0)

time.sleep(5)
bg= 0

for i in range(60):
    ret,bg=cap.read()

bg= np.flip(bg,axis=1)

while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask = cv2.inRange(hsv, u_black, l_black)

    res= cv2.bitwise_and(img, img, mask=mask)
   

    final_output = cv2.addWeighted(res, 1, res, 1, 0)
    output_file.write(final_output)
cap.release()
out.release()
















    


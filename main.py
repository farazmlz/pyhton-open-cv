import cv2
import numpy


kernel = numpy.ones((5, 5), numpy.uint8)
x = cv2.imread("G:\\Python-projects\\python openCV\\section 3\\1.jpg", 1)
# print(x.sape)
x = cv2.resize(x, (700, 700))
xgray = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
xinv = cv2.bitwise_not(xgray)
no = cv2.blur(xinv, (3,3))
no2 = cv2.blur(no, (3,3))                  
er = cv2.erode(no2, kernel, iterations=3)  
di = cv2.dilate(er, kernel, iterations=3)
_,th = cv2.threshold(no2, 60, 255, cv2.THRESH_BINARY)
#ca = cv2.Canny(di,100,255)
counto,tree = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

c=0
for i in range(0,len(counto)):
    if(cv2.contourArea(counto[i])>400):
        x=cv2.drawContours(x,counto, i, (0, 0, 255), 2)                 
        
        cv2.imshow("output",x)       
        cv2.waitKey(10)       
        c = c + 1
       

print(" Real count of cells : ", c)

cv2.imshow("final_output",x)       
cv2.waitKey(0)
import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_smile.xml')


while True: 
    success, image= cap.read()
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg, 1.1, 4)
    
    cnt = 1
    keyPressed = cv2.waitKey(1)
    for x,y,w,h in faces:
        smiles = smileCascade.detectMultiScale(grayImg, 1.8, 15)
        for x,y,w,h in smiles:   
            path = '/images/image' + str(cnt) + '.jpg'
            cv2.imwrite(path, image)
            cnt +=1
            if (cnt>=2):
                break
                   
    cv2.imshow("Selfie",image)
       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break
        
cap.release()
cv2.destroyAllWindows()
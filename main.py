#-->importing opencv module into our IDE
import cv2

#-->For capturing video
face_cap = cv2.CascadeClassifier("C:/Users/mahto/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0) #-->WILL TURN ON OUR CAMERA
while True:
    ret , video_data = video_cap.read() #-->it will read our photos and videos
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY) #-->Convert into black and white so as to understand facial textures
    #-->Defining some parameters for capturing face
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    #--> For the box
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("video_live",video_data) #-->Making the frame of our camera (The backgrnd in which video will be shown)
    if cv2.waitKey(10) == ord("k"):
        break

video_cap.release()    
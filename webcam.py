
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
while True:
    success, img = cap.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(faces)
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w+w, y + h+y), (0, 255, 0), 2)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

"""
frameWidth = 640 and frameHeight = 480: These lines define the width and height of the frames that the video capture will capture from the camera. Here, the width is set to 640 pixels, and the height is set to 480 pixels. You can adjust these values according to your requirements.
cap = cv2.VideoCapture(0): This line creates a VideoCapture object named cap, which is used to capture video from a camera. The argument 0 specifies the index of the camera to be used. Here, 0 typically represents the default camera connected to the system. If you have multiple cameras, you can specify the index of the camera you want to use.
cap.set(3, frameWidth) and cap.set(4, frameHeight): These lines set the width and height of the frames that the video capture will capture from the camera. The function cap.set() is used to set properties of the video capture device. The first argument (3 and 4 respectively) corresponds to the properties CV_CAP_PROP_FRAME_WIDTH and CV_CAP_PROP_FRAME_HEIGHT, which represent the width and height of the frames. The second argument (frameWidth and frameHeight) specifies the values to which these properties will be set.
cap.set(10, 150): This line sets the brightness of the video capture. The first argument (10) corresponds to the property CV_CAP_PROP_BRIGHTNESS, which represents the brightness of the video capture. The second argument (150) specifies the brightness level to be set. This value can typically range from 0 to 255, where 0 represents the darkest and 255 represents the brightest. You can adjust this value based on your requirements to control the brightness of the captured video."""
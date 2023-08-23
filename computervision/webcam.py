import cv2  #library

CAM_IDX = 0  # 0 : default camera
cam = cv2.VideoCapture(CAM_IDX)
while cam.isOpened():
    state,frame = cam.read()
    if not state:
        print('camera is not available')
        break
    #teen panch karo
    print(state,frame.shape)
    cv2.imshow('webcam',frame)
    if cv2.waitkey(1) == 27:  #esckey
        break
cam.release()
cv2.destroyAllWindows()
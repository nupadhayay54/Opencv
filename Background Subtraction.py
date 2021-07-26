import cv2
cap = cv2.VideoCapture('video.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while 1:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask', fgmask)
    cv2.imshow('frame', frame)
# Using Esc button exit from window
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

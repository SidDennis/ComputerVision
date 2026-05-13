import cv2
from PIL import Image
import numpy as np

Video = cv2.VideoCapture(0)

while True:
  rev, frame = Video.read()

  blur_frame = cv2.medianBlur(frame, 21)
  hsv_frame = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv_frame, np.array([20, 100, 100]), np.array([30, 255, 255]))
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  for cont in contours:
    print(cv2.contourArea(cont))
    if cv2.contourArea(cont) > 400: 
      x, y, w, h = cv2.boundingRect(cont)
      frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
    

Video.release()
cv2.destroyAllWindows()
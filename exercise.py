import numpy as np
import pandas as pd
import cv2

#importing video files
spinning_donut1=cv2.VideoCapture("exp_video.mp4")
spinning_donut2=cv2.VideoCapture("exp_video2.mp4")


#writing both videos
while True:
    ret,frame=spinning_donut1.read()
    ret,frame1=spinning_donut2.read()
    smaller_frame=cv2.resize(frame1,(0,0),fx=0.5,fy=0.5)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("q"):
     break

    cv2.imshow("frame1",smaller_frame)
    if cv2.waitKey(1)==ord("q"):
     break


cv2.destroyAllWindows()
# frame.release()
# frame1.release()
# cv2.destroyAllWindows()

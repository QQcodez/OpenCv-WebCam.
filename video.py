#WEBCAM OPENCV PROJECT
"""In this program I have used OpenCV library which provides functions like Video Capture that allows us to capture the video from the webcam by streaming multiple frames of numpy arrays(images) ->VIDEO STREAM using a while loop.

I have also displayed a hsv image only showing the hue , saturation and brightness of pixels
I also go ahead to filter blue pixels only for my stream

"""



# importing modules
import numpy as np
import cv2

# activating the webcam using cv2.VideoCapture(path of video file;webcam=0)
web_cam=cv2.VideoCapture(0)

#Looping through the image frames to get a video
while True:
    ret, frame = web_cam.read()
# resizing for 4 frames
# start by creating an empty array for frame 
    image=np.ones(frame.shape, np.uint8)
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
# filling the 4 resized images in the frame
    image[0:240 ,0:320 ]=smaller_frame
    image[240:480 ,320:640 ]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[240:480 ,0:320 ]=smaller_frame
    image[0:240 ,320:640]=smaller_frame

#drawing a shape (line) in the frame :cv2.line()
# image=cv2.line(image,(0,0),(50,50),(0,0,23),5)

# converting to hsv for color hue,saturation and brightness to filter out pixels in the desired range
    hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# creating a range for blue in this instance
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])

# Filtering out pixels in the given range and storing them in a mask 
# Colours in the range are lit up
    mask=cv2.inRange(hsv,lower_blue,upper_blue)

# {cv2.bitwise_and()} does an add operation to get pixels that are lit in a 1*1 condition only in the two required src images 1 and 2.
# In this case we pass the same image twice 
    result=cv2.bitwise_and(image,image, mask=mask)

# Displaying the original images, masked images & and the filtered images(blue pixels)
    cv2.imshow("video",image)
    cv2.imshow("frame", result)
    cv2.imshow("mask",mask)

# Waiting for "q" key to be pressed to break out of the while loop using cv2.waitkey()
# 1 is for 1ms before looping.This creates a stream
    if cv2.waitKey(1)==ord("q"):
        break

web_cam.release()
cv2.destroyAllWindows()
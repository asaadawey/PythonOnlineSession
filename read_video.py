#Install libraries using pip

# Copy this and paste it into terminal : pip install cv2

# 1- Import cv2

import cv2;

VIDEO_NAME = './0001.mp4'
FRAME_NAME = './frame80.jpg'
FRAME_NUMBER = 80
# 2- Open the video

video = cv2.VideoCapture(VIDEO_NAME)

# 3- Get total number of frames

frame_numbers = video.get(cv2.CAP_PROP_FRAME_COUNT);
print(frame_numbers);

# 4- Get frame number 50 for example

video.set(cv2.CAP_PROP_POS_FRAMES , FRAME_NUMBER);
# Read the current frame
ret , frame = video.read();
cv2.imwrite(FRAME_NAME,frame);
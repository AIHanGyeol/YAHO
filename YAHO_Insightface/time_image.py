'''
file: box_pos.py
Author: 이한결
date: 2022.11.17
note: 
    사람의 얼굴을 mediapipe 로 감지하고 그 박스의 좌표를 image, label 폴더에 저장한다.
'''
import os
import cv2
import mediapipe as mp
import time




if 'image' not in os.listdir():
  os.mkdir('./image')
else:
  pass

image_save_path = './image'

start_time = int()

# camera = 0

# cap = cv2.VideoCapture(camera)

#가로 세로 크기 640으로 고정.

count_time = 0
count = 1

user_id = 'user_id'

# while cap.isOpened():
#   success, image = cap.read()
#   if not success:
#     print("Ignoring empty camera frame.")
#     continue

  
# image = cv2.resize(image , (640,640))

if count_time == 0:
  start_time = int(time.time())
try:
  if start_time + count_time == int(time.time()):
    # cv2.imwrite(f'{image_save_path}/{user_id}_{str(count).zfill(4)}.jpg', image)
    count_time += 10      
    count += 1
except:
  print('error')  


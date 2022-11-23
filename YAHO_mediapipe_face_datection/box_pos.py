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

if 'label' not in os.listdir():
  os.mkdir('./label')
else:
  pass


image_save_path = './image'
label_save_path = './label'

start_time = int()
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

camera = 0

cap = cv2.VideoCapture(camera)

#가로 세로 크기 640으로 고정.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 가로
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640) # 세로

count_time = 0
count = 1

user_id = 'user_id'

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    
    image = cv2.resize(image , (640,640))
    

    x = image.shape[0]
    y = image.shape[1]
    image = cv2.flip(image, 1)
    image.flags.writeable = False
    results = face_detection.process(image)


    '''박스에 선 그리기.
    # xmin = int(results.detections[0].location_data.relative_bounding_box.xmin * x)
    # ymin = int(results.detections[0].location_data.relative_bounding_box.ymin * y)
    # width = int(results.detections[0].location_data.relative_bounding_box.width * x) + xmin 
    # height = int(results.detections[0].location_data.relative_bounding_box.height * y) + ymin
    # print(xmin , ymin , width , height)
    # cv2.line(image,(xmin , ymin) , (width , height) , (0,255,0) ,thickness=3)
    '''

    
    if count_time == 0:
      start_time = int(time.time())
    try:
      if start_time + count_time == int(time.time()):
        xmin = results.detections[0].location_data.relative_bounding_box.xmin
        ymin = results.detections[0].location_data.relative_bounding_box.ymin
        width = results.detections[0].location_data.relative_bounding_box.width + xmin 
        height = results.detections[0].location_data.relative_bounding_box.height + ymin
        jj = str(0)+ ' ' +str(xmin) + ' ' + str(ymin)+ ' ' + str(width) + ' ' +  str(height)
        cv2.imwrite(f'{image_save_path}/{user_id}_{str(count).zfill(4)}.jpg', image)
        f = open(f'{label_save_path}/{user_id}_{str(count).zfill(4)}.txt' , 'w')
        f.write(jj)
        f.close()
        count_time += 10      
        count += 1
    except:
      print('error')  

    image.flags.writeable = True
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
    # Flip the image horizontally for a selfie-view display.
    # cv2.imshow('MediaPipe Face Detection',image)

    if count == 100:
      cv2.destroyAllWindows()
      break

    # if cv2.waitKey(5) & 0xFF == 27:  #ESC
    #   cv2.destroyAllWindows()
    #   break


cv2.destroyAllWindows()
cap.release()
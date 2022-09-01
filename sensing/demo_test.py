import cv2
import mediapipe as mp
import time
import numpy as np
import easyocr
import asyncio
from jamo import h2j, j2hcj
import brailleTable
# import RPi.GPIO as GPIO
# from picamera import PiCamera

mode = 0

signal = 0

# Toggle mode
def toggleMode():
  if mode == 0:
      mode = 1
      print(mode)
      Boom("101010")
      time.sleep(0.3)
      Boom("101010")
  else:
      mode = 0
      print(mode)
      Boom("010101")
      time.sleep(0.3)
      Boom("101010")
    

# Direction check
def checkDir(direction):
  dir_left = 0.3
  dir_right = 0.7
  if direction>dir_left and direction<0.5:
    return "101010"
  if direction>0.5 and direction < dir_right:
    return "010101"
  return 0


# Send stimulation
async def sendStimul(power, arr):
  last = power
  for i in range(3):
    if last > 0:
      Boom(arr) # to be continued
      last = last - 1
    asyncio.sleep(0.3)


# Boom !!
def Boom(arr):
  print("Boom !!", arr)
  return


# Alert Function
async def sendAlert(distance, direction):
  # Distance define
  distance_short = -0.5
  distance_middle = -0.3
  distance_long = -0.1
  
  dir = checkDir(direction)
  if dir != 0:
    if distance < distance_short:
      await sendStimul(3,dir)
    elif distance < distance_middle:
      await sendStimul(2,dir)
    elif distance < distance_long:
      await sendStimul(1,dir)


 


# # event interrupt
# GPIO.add_event_detect(20, GPIO.FALLING, callback=toggleMode)

# class InterruptExecution (Exception):
#     pass

# def function_a():
#     while some_condition_is_true():
#         do_something()
#         if callback_time():
#             try:
#                 function_b()
#             except InterruptExecution:
#                 break
#         do_something_else()
#     do_final_stuff()


# def function_b():
#     do_this_and_that()
#     if interruption_needed():
#         raise (InterruptExecution('Stop the damn thing'))



reader = easyocr.Reader(['ko']) 

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

arr = []
# For webcam input:
cap = cv2.VideoCapture(0)
startTime = time.time()


with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    timeNow = time.time()

    # # Mode switch
    # if timeNow-startTime >0.3 and signal ==1:
    #     startTime = timeNow
    #     if mode == 0:
    #         mode = 1
    #     else:
    #         mode = 0
    
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    
    
    if mode == 0:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # Flip the image horizontally for a selfie-view display.
        # print(results.pose_landmarks.landmark[0].z)
        if results.pose_landmarks:
          if len(arr) < 8:
              arr.append(results.pose_landmarks.landmark[0].z)
          else:
              arr = arr[1:8]
              arr.append(results.pose_landmarks.landmark[0].z)

          if timeNow-startTime > 1.2:
              startTime = timeNow
              # print("distance : " , round(np.mean(arr), 3))
              print(results.pose_world_landmarks.landmark[0].z)
              print(results.pose_landmarks.landmark[0].x)
              asyncio.run(sendAlert(results.pose_landmarks.landmark[0].z, results.pose_landmarks.landmark[0].x))
    
    
    if mode == 1:
        result_ocr = reader.readtext(image)
        width = [result_ocr[i][0][1][0]-result_ocr[i][0][0][0] for i in range(len(result_ocr))]
        height = [result_ocr[i][0][2][1]-result_ocr[i][0][0][1] for i in range(len(result_ocr))]
        print(width)
        print(height)

        # title select
        if len(result_ocr) > 0:
          biggest = np.argmax(height)
          title = result_ocr[biggest][1]
          print(title)
          title_filtered = ''.join(char for char in title if char.isalnum())
          print(title_filtered)
          jamo_str = j2hcj(h2j(title_filtered))
          print(jamo_str)
          brailleTable.alertKorean(jamo_str)



    
    
    cv2.imshow('Sixth Sense - Team Boyjo No.1', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
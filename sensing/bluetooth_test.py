import serial, time
# import RPi.GPIO as GPIO
# from picamera import PiCamera
ser = serial.Serial(
    port='COM9',
    baudrate=115200,
)



# Boom !!
def Boom(arr):
  ser.write(arr)
  return


for i in range(3):
    Boom("111111".encode())
    time.sleep(0.5)

ser.close()
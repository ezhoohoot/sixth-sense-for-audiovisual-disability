import serial, time
# import RPi.GPIO as GPIO
# from picamera import PiCamera
ser = serial.Serial(
    port='COM3',
    baudrate=115200,
)



# Boom !!
def Boom(arr):
  # ser.open()
  ser.write(arr.encode())
  # ser.close()
  return


from DRONEIMPORT import *
import keyboard
import time
import cv2


i = 0

def keyboardcontrol():

 LEFTRIGHT,FORWARDSBACKWARDS,UPDOWN,ANGLE=0,0,0,0
 speed = 120
 global i

 if keyboard.is_pressed("a"):
  print("GOING LEFT")
  LEFTRIGHT=-speed
 elif keyboard.is_pressed("d"):
  print("GOING RIGHT")
  LEFTRIGHT=speed

 if keyboard.is_pressed("w"):
  print("MOVING FORWARD")
  FORWARDSBACKWARDS=speed

 elif keyboard.is_pressed("s"):
  print("MOVING BACK")
  FORWARDSBACKWARDS=-speed

 if keyboard.is_pressed("up"):
  print("FLYIGN HIGER")
  UPDOWN=speed
 elif keyboard.is_pressed("down"):
  print("GOING LOWER")
  UPDOWN=-speed
 if keyboard.is_pressed("left"):
  print("ROTATING LEFT")
  ANGLE=speed

 elif keyboard.is_pressed("right"):
  print("ROTATING RIGHT")
  ANGLE=-speed

 if keyboard.is_pressed("q"):
  print("INITIALIZING")
  drone.takeoff()
  time.sleep(0.2)
 #do sleep for 3 sec for saftey

 elif keyboard.is_pressed("e"):
  print("LANDING")
  drone.landoff()

 if keyboard.is_pressed("k"):
  drone.flip_back()
  time.sleep(0.2)

 elif keyboard.is_pressed("j"):
  print("FLIPPING LEFT ")
  drone.flip_left()
  time.sleep(0.2)

 if keyboard.is_pressed("l"):
  print("FLIPPING  RIGHT ")
  drone.flip_right()
  time.sleep(0.2)


 elif keyboard.is_pressed("i"):
   print("FLIPPING FORWARDS")
   drone.flip_forward()
   time.sleep(0.2)

 if keyboard.is_pressed("b"):
  print(drone.get_battery())

 elif keyboard.is_pressed("p"):
  i=i+1
  print("taking photo")
  a=cv2.imwrite('drone photo' + str(i) + '.jpg', image)
  print(i)
  time.sleep(0.2)

 if keyboard.is_pressed("h"):
  print(drone.get_height())

 return [LEFTRIGHT, FORWARDSBACKWARDS,UPDOWN,ANGLE]



while True:

 user= keyboardcontrol()
 drone.send_rc_control(user[0], user[1], user[2], user[3])
 image = drone.get_frame_read().frame
 image = cv2.resize(image, (1280, 720))
 cv2.imshow("DRONE VIEW", image)
 cv2.waitKey(1)  # display a window for given milliseconds

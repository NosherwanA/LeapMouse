#Leap Python mouse controller POC
import sys
from leap import Leap, Mouse
from PalmControl import Palm_Control_Listener  #For palm-tilt based control

def main():
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
    #Default
    finger_mode = False
    palm_mode = True
    motion_mode = False
    smooth_aggressiveness = 8
    smooth_falloff = 1.3

    listener = Palm_Control_Listener(Mouse)
    controller = Leap.Controller()  #Get a Leap controller
    controller.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES)
    controller.add_listener(listener)  #Attach the listener

    #Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()
    #Remove the sample listener when done
    controller.remove_listener(listener)

main()

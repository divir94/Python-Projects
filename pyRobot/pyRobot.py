# pyRobot Project
# Written by Zach Dodds and modified by Ran Libeskind-Hadas

import RobotCanvas
import tkinter
import time
import threading
import random
import queue
import math
import sys
from roombaSim import *

def toDegrees(theta): return theta*180/math.pi
       
class Robot(ThreadedClient):
    """
    A class defining the graphical display and the behavior of
    a Roomba-like robot with a laser rangefinder.
    """
        
    def simulator(self):
        # THIS SIMULATOR BEGINS WITH A NUMBER OF SETTINGS THAT YOU 
        # CAN IGNORE AND SHOULD NOT CHANGE OR MODIFY IN THE CODE.
        # Pause for a second to let the graphics initialize.
        # BEGINNING OF SETTINGS...
        time.sleep(1)
        rangeHeading = 0.0      # Angle to point our range finder
        oldgoal = (0.0, 0.0)    # The old goal position
        goal = (0.0, 0.0)       # The current goal position
        RADIUS = 16         # The roomba's radius in cm
        # ... END OF SETTINGS

        # These constants are the robot's translational
        # and rotational velocities.  Please don't change these values.
        # You will see them being used - further down in this program -
        # to make the robot move and turn.
        FV = 50.0                       # MAX FORWARD VELOCITY IS 50 cm/sec
        RV = 40.0                       # MAX ROTATIONAL VELOCITY IS 40 deg/sec

        lowerBound = 10
        upperBound = 30
        lastRangeFinder = self.getRange(rangeHeading)

        # The robot is always in some state.  
        # The constants below represent some different tasks/states.
        # YOU WILL ALMOST CERTAINLY NEED TO ADD SOME ADDITIONAL STATES
        # TO CONTROL THE ROBOT!  EACH TIME YOU INTRODUCE A NEW STATE,
        # GIVE IT A STATE NAME/NUMBER HERE.  You may also want to modify
        # or even remove some of the simple states that we have included
        # here.

        # In the current setup, the robot's behavior is governed by 
        # just 5 states.  These states are numbers, but for convenience we give
        # them names below.  In our setup here, these states are
        # called KBD, STOP, GO, GOFOR, and TURN.  
        # The robot starts in state 1, which we also call 
        # KBD, which stands for "KeyBoarD".
        # This state "listens" for the user to enter
        # single keyboard presses that represent rudimentary commands.
        # This effectively lets the user "drive" the robot.
        # The keyboard commands are described on the project webpage and
        # you can also find them in the code below.

        # HERE IS WHERE YOU CAN ADD/MODIFY YOUR STATES

        KBD = 1     # This is the start state where we listen to keyboard.
        STOP = 2    # In this state, the robot stops moving.
        GO = 3      # In this state, the robot goes forward in its current
                    # heading/direction.
        TURN = 4    # In this state, the robot turns in place for 3 seconds.
                    # How does it know to time out after 3 seconds?  It uses the
                    # GOFOR state!
        GOFOR = 5   # In this state, some other state is used for 
                    # a given period of time before entering the next state.
                    # This is very useful for doing a task for a specified
                    # amount of time.  Please see the website and/or the code
                    # for the GOFOR state for a complete description.
        START = 6
        #ON_TRACK = 7
        #TOO_CLOSE = 8
        #TOO_FAR = 9

        # We keep track of the current state in a variable called state.
        # Initially, state is the KBD state...
        state = KBD      

        # Now that we have defined our states and initialized the start state
        # (the state) to the KBD state, we enter an infinite loop
        # which controls the robot.  

        # Each time we go through this loop, the following actions will occur:
        #   1.  The robot gets its data including its x and y coordinates, its
        #       current heading, information from its bump sensors, and the 
        #       distance to the obstacle detected by the laser rangefinder.  
        #   2.  We read the keyboard and the mouse to see if the human user has
        #       entered any data that way.  We can exit by typing "Q" in the robot
        #       window or control-C in the IDLE window.
        #   3.  We check what state the robot is in and execute the code 
        #       corresponding to that state.

        while True:
            currentState = state
            # Each time through the loop, we begin by reading the robot's sensors...
            #
            # x is the x coordinate of the robot
            # y is the y coordinate of the robot
            # thd is the robot's heading in degrees
            # bump is a list of two bump sensor readings: left and right.
            # These sensors are activated when the robot bumps into something.

            [x,y,thd], bump = self.getData()
          
            # Next, we point the laser rangefinder in the direction
            # specified by the variable rangeHeading.  This angle is 
            # measured in DEGREES and is RELATIVE to the heading of the robot.
            # It must be in the range -180 degrees to +180 degrees.  Note that
            # 0 degrees is straight ahead with respect to thd, the robot's
            # angle in degrees.  The value in rangeFinder is the distance
            # to the nearest obstacle.
            rangeFinder = self.getRange(rangeHeading)

            # Next, w get any keypresses and goal locations (mouse clicks)
            # that are entered by the user.
            key, goal = self.getWindowEvents()  
            # At start, key == ''

            # Now we check to see if the user has moved the goal using the 
            # mouse and "g" key.
            if goal != oldgoal: 
                # The user has pressed mouse-button and g to indicate
                # the location of a new goal.
                print('New goal at x =', goal[0], 'and y =', goal[1])
                self.showGoal( goal )           # Displays the goal in green
                oldgoal = goal                  # Reset the old goal

            # Next, check to see if robot has reached the goal.  If so, 
            # print a message, stop the robot, and return control to the user
            # by entering the KBD state.
            if state != STOP and state != KBD:
                [realx, realy, realthr] = self.getRealPose()
                distToGoal = math.sqrt( (realx-goal[0])**2 + (realy-goal[1])**2 )
                if distToGoal < RADIUS:
                    print('AT GOAL!')
                    self.setVels(0,0)           # Stop robot movement
                    state = KBD                 # Set state back to KBD

            # HERE'S AN EXAMPLE OF AN ACTION THAT OCCURS 
            # REGARDLESS OF WHAT STATE THE ROBOT IS IN...  IT SAYS
            # "REGARDLESS OF WHAT STATE THE ROBOT IS IN, IF A BUMP SENSOR IS TRIPPED
            # THEN ENTER THE STOP STATE".  bump[0] is True if the left bump sensor
            # has been tripped and bump[1] is True if the right bump sensor has
            # been tripped.
            """if bump[0] or bump[1]:
                print('BUMP!', end=' ')
                print('  [Left bump sensor:',  bump[0], ']  ', end=' ')
                print('  [Right bump sensor:', bump[1], ']  ')
                robotTask = STOP"""

            
            if bump[0] or bump[1]:
                self.setVels(-FV, RV)
                print('BUMP!', end=' ')
                print('  [Left bump sensor:',  bump[0], ']  ', end=' ')
                print('  [Right bump sensor:', bump[1], ']  ')
                pause_stop = time.time() + 0.3
                nextState = "ON_TRACK"
                state = GOFOR


            # HERE IS WHERE WE HAVE DEFINED OUR STATES.  THIS IS WHERE YOU 
            # WILL DEFINE THE BEHAVIOURS OF YOUR OWN STATES.  YOU MAY WISH TO
            # MODIFY OR DELETE SOME OF THE EXAMPLE STATES THAT WE HAVE INCLUDED
            # HERE AND YOU WILL CERTAINLY NEED TO DEFINE SOME OF YOUR OWN NEW
            # STATES AS WELL.

            # Define the behavior for the STOP state
            if state == STOP:  
                self.setVels(0,0)   # Stop by setting forward velocity and rotational
                                    # velocities to 0...  The first argument to setVels is
                                    # is the forward velocity and the second argument is the
                                    # rotational velocity.
                state = KBD         # And return to the KBD state.

            # Define the behavior for the GO state
            if state == GO:
                # Point the laser rangefinder in the same direction
                # as the robot's heading - that is, 0 degrees away from the thd heading.
                rangeHeading = 0    
                # If the rangeFinder reports a distance within 2 times the RADIUS of the
                # robot then change the state to the TURN state.
                if rangeFinder < 2*RADIUS:
                    rangeHeading -= 90
                    state = "TOO_CLOSE"
                # Otherwise, tell the robot to move at full speed ahead!
                else:
                    self.setVels(FV, 0)

            # Define the behavior for the TURN state
            if state == TURN:
                # Tell the robot to turn at maximum rotational velocity.  Note that the
                # the robot will continue turning at this velocity until we stop it!
                self.setVels(0, RV)
                # Set a variable called paused_stop to the current time (time.time())
                # plus 3 seconds.
                pause_stop = time.time() + 90/RV
                # Set a local variable called nextState that indicates that the next
                # state that we want to enter (at time pause_stop - that is 3 seconds
                # from now) is the GO state
                nextState = GO
                # But enter the GOFOR state now.  This state will essentially watch the
                # clock.  When the clock gets to time pause_stop, it will say "OK, it's
                # time to enter the nextState".  In this case, it will make the state
                # become nextState which is GO!
                state = GOFOR

            # The GOFOR state allows us to simply wait until time reaches
            # the pause_stop time that we set before executing the next task.
            # Remember that while we're waiting, whatever parameters we've
            # set for the robot are being executed!  For example, if the robot
            # was left turning by setting its motors through the setVels function
            # before we entered GOFOR, then it will continue
            # turning while the clock marches forward!
            if state == GOFOR:
                if time.time() > pause_stop:
                    state = nextState

            # In state KBD keypresses can
            # override or set our actions
            if state == KBD:
                if key == 'r': 
                    rangeHeading += 5
                    if rangeHeading > 180: rangeHeading -= 360
                elif key == 'R':
                    rangeHeading -= 5
                    if rangeHeading < -180: rangeHeading += 360
                elif key == 'i': self.setVels(FV,0)
                elif key == 'k': self.setVels(-FV,0)
                elif key == 'j': self.setVels(0,RV)
                elif key == 'l': self.setVels(0,-RV)
                elif key == 's': state = START
                elif key == ' ': 
                    self.setVels(0,0)   
                elif key == 'q': break    # 'Q' quits the program

            """ ------------------- My Functions START ------------------ """

            if state == START:
                # get relative goal points (x1, y1)
                x1, y1 = goal[0]-x, goal[1]-y
                # alpha = angle b/w relative goal and x-axis 
                alpha = toDegrees(math.atan2(y1, x1))
                if alpha<0: alpha += 360 # 0<=alpha<=360
                # delTheta = reltaive angle to goal
                delTheta = alpha-thd
                #print("Alpha: {0}, Thd: {1}, Diff: {2}".format(alpha, thd, delTheta))

                # move anticlockwise, if closer
                if 0<=delTheta<=180: self.setVels(0, RV)
                else: self.setVels(0, -RV)
                if delTheta>180: delTheta = 360 - delTheta

                # change heading
                pause_stop = time.time() + abs(delTheta)/RV
                nextState = GO
                state = GOFOR

            if state == "ON_TRACK":
                if lowerBound < rangeFinder < upperBound:
                    state = "ON_TRACK"
                elif rangeFinder < lowerBound:
                    state = "TOO_CLOSE"
                elif rangeFinder > upperBound:
                    state = "TOO_FAR"
                self.setVels(FV,0)
                print ("lastdist: {}, dist: {}".format(lastRangeFinder,rangeFinder))
                lastRangeFinder=rangeFinder

            if state == "TOO_FAR":
                if lowerBound < rangeFinder < upperBound:
                    state = "ON_TRACK"
                elif rangeFinder < lowerBound:
                    state = "TOO_CLOSE"
                elif rangeFinder > upperBound:
                    state = "TOO_FAR"
                if lastRangeFinder>rangeFinder: self.setVels(5,RV)
                else: self.setVels(10,-RV)
                print ("lastdist: {}, dist: {}".format(lastRangeFinder,rangeFinder))
                lastRangeFinder=rangeFinder

            if state == "TOO_CLOSE":
                if lowerBound < rangeFinder < upperBound:
                    state = "ON_TRACK"
                elif rangeFinder < lowerBound:
                    state = "TOO_CLOSE"
                elif rangeFinder > upperBound:
                    state = "TOO_FAR"
                if lastRangeFinder>rangeFinder: self.setVels(5,RV)
                else: self.setVels(10,-RV)
                print ("lastdist: {}, dist: {}".format(lastRangeFinder,rangeFinder))
                lastRangeFinder=rangeFinder
                               

#            if state != currentState:
 #               print ("currentState: {},   nextState: {}".format(currentState, state))
                
            """ ------------------- My Functions END ------------------ """

            # Regardless of our state, if we press the space key
            # key we should be able to reenter the KBD state...
            if key == ' ':
                self.setVels(0, 0)
                state = KBD

# STOP READING HERE.  NOTHING BELOW IS NEEDED FOR YOUR PROJECT.

            # We sleep to let the graphics catch up...
            # Don't sleep elsewhere (it makes the program
            # unresponsive, since the key is not being
            # checked!) Instead, use the PAUSE state.
            time.sleep(0.025) # 1/40 of a second
                 
        # if the while loop ends, we shutdown the gui, too. 
        self.gui.shutdown()

    def __init__(self, mapname):
        """
         This constructor delegates a couple graphics-specific things
         to the ThreadedClient class
        """
        self.mapname = mapname
        ThreadedClient.__init__(self, mapname)
        
if __name__ == '__main__':
        
    # you might try one of these maps:
    MAPS = [ 'map0.txt',  # 0
             'map1.txt',  # 1
             'map2.txt'   # 2
        ]

    while True:
        mapstring = input("Enter a map number between 0 and 2: ")
#        mapstring=1
        mapnumber = int(mapstring)
        if mapnumber >= 0 and mapnumber <= 2: break
             
    R = Robot(MAPS[mapnumber])
    R.run()


    

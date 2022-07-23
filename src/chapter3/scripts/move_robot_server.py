#!/usr/bin/env python3
'''Action Server Code'''

import time
import actionlib
import rospy
from chapter3.msg import MoveRobotAction
from chapter3.msg import MoveRobotFeedback
from chapter3.msg import MoveRobotResult

ACTION_SERVER = None

def move_robot_callback(received_goals):
    ''' Callback '''
    global ACTION_SERVER
    reached_goals = []
    delay = 3 #wait time in seconds
    rate = rospy.Rate(1)
    rospy.loginfo("Goals have been received")
    rospy.loginfo(received_goals)
    success = False
    preempted = False
    i = 0

    while not rospy.is_shutdown():
        #Taking each goal one by one and moving the robot towards it
        current_goal = received_goals.goals[i]
        rospy.loginfo("Moving to goal " + str(current_goal) + " ...")
        time.sleep(delay) #Dummy delay
        rospy.loginfo("Reached goal " + str(current_goal))
        reached_goals.append(current_goal)
        i = i+1
        if ACTION_SERVER.is_preempt_requested():
            preempted = True
            break
        if reached_goals == received_goals.goals:
            success = True
            break
        feedback_msg = MoveRobotFeedback()
        feedback_msg.goals_reached_till_now = reached_goals
        ACTION_SERVER.publish_feedback(feedback_msg)
        rate.sleep()

    result = MoveRobotResult()
    if success:
        result.result = "All goals visited !"
    else:
        result.result = "All goals not visited ..."
    rospy.loginfo("sent goal result to client")

    if preempted:
        rospy.loginfo("Preempted")
        ACTION_SERVER.set_preempted(result)
    elif success:
        rospy.loginfo("Success")
        ACTION_SERVER.set_succeeded(result)
    else:
        rospy.loginfo("Failure")
        ACTION_SERVER.set_aborted(result)

def main():
    '''Main'''
    global ACTION_SERVER
    ACTION_SERVER = actionlib.SimpleActionServer('/move_robot', MoveRobotAction, execute_cb=move_robot_callback, auto_start=False)
    ACTION_SERVER.start()

if __name__ == '__main__':
    rospy.init_node('move_robot_action_server')
    main()
    rospy.spin()
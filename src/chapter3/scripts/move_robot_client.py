#!/usr/bin/env python3
'''Action Client Code'''

import rospy
import actionlib
from chapter3.msg import MoveRobotAction
from chapter3.msg import MoveRobotGoal

def done_callback(status, result):
    '''Completed Callback'''
    rospy.loginfo("Status: " + str(status))
    rospy.loginfo("Result: " + str(result))

def feedback_callback(feedback):
    '''Status Callback'''
    rospy.loginfo("Feedback: " + str(feedback))

def main(action_client):
    '''Main'''
    while(True):
        goals_list = input("\nEnter the goal ID/s separated by commas. Eg- 1,2,3 : ")
        if(len(goals_list)>0):
            goals_list = goals_list.strip().split(',')
            goal = MoveRobotGoal(goals=goals_list)
            action_client.send_goal(goal, done_cb=done_callback, feedback_cb=feedback_callback)
            rospy.loginfo("Calling the action server")
            break
        else:
            continue

if __name__ == '__main__':
    rospy.init_node('move_robot_action_client')
    ACTION_CLIENT = actionlib.SimpleActionClient('/move_robot', MoveRobotAction)
    ACTION_CLIENT.wait_for_server()
    rospy.loginfo("Robot waiting for goals ...")
    main(ACTION_CLIENT)
    rospy.spin()

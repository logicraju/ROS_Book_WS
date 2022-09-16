#!/usr/bin/env python3
'''Subscriber Code'''
import rospy
from chapter3.msg import robot_peripherals

def callback(data):
    '''Callback function'''
    rospy.loginfo("Received Message")
    rospy.loginfo("led_front: %s", data.led_front)
    rospy.loginfo("led_left: %s", data.led_left)
    rospy.loginfo("led_right: %s", data.led_right)
    rospy.loginfo("led_rear: %s", data.led_rear)
    rospy.loginfo("music_id: %s", data.music_id)
    rospy.loginfo("screen_message: %s", data.screen_message)

if __name__ == '__main__':
    rospy.init_node('subscriber_node')
    rospy.Subscriber("/custom_topic", robot_peripherals, callback)
    rospy.spin()

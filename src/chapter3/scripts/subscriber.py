#!/usr/bin/env python3
'''Subscriber Code'''
import rospy
from std_msgs.msg import String

def callback(data):
    '''Callback function'''
    rospy.loginfo("Received Message- %s", data.data)

if __name__ == '__main__':
    rospy.init_node('subscriber_node')
    rospy.Subscriber("pub_topic", String, callback)
    rospy.spin()
    
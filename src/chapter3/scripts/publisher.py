#!/usr/bin/env python3
'''Publisher Code'''

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    try:
        pub = rospy.Publisher('pub_topic', String, queue_size=10)
        rospy.init_node('publisher_node')
        rate = rospy.Rate(1) # Frequency in Hz
        while not rospy.is_shutdown():
            pub.publish("hi !")
            rate.sleep()
    except rospy.ROSInterruptException as e:
        rospy.loginfo("Exception: " + str(e))

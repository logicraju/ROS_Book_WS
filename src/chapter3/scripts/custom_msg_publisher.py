#!/usr/bin/env python3
'''Publisher Code'''

import rospy
from chapter3.msg import robot_peripherals

if __name__ == '__main__':
    try:
        pub = rospy.Publisher('/custom_topic', robot_peripherals, queue_size=10)
        custom_msg = robot_peripherals()
        rospy.init_node('publisher_node')
        rate = rospy.Rate(1) # Frequency in Hz
        while not rospy.is_shutdown():
            custom_msg.led_front = True
            custom_msg.led_left = True
            custom_msg.led_right = True
            custom_msg.led_rear = True
            custom_msg.music_id = 1
            custom_msg.screen_message = "Starting Operations. Waiting for goal input ..."
            pub.publish(custom_msg)
            rate.sleep()
    except rospy.ROSInterruptException as e:
        rospy.loginfo("Exception: " + str(e))

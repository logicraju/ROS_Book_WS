#!/usr/bin/env python3
'''Service Server Code'''

import rospy
from chapter3.srv import robot_accessories, robot_accessoriesResponse

def handle_switch(req):
    '''Service handler'''
    rospy.loginfo("Received Request:")
    rospy.loginfo("led_front: " + str(req.request_msg.led_front))
    rospy.loginfo("led_left: " + str(req.request_msg.led_left))
    rospy.loginfo("led_right: " + str(req.request_msg.led_right))
    rospy.loginfo("led_rear: " + str(req.request_msg.led_rear))
    rospy.loginfo("music_id: " + str(req.request_msg.music_id))
    rospy.loginfo("screen_message: " + str(req.request_msg.screen_message)+"\n")
    rospy.loginfo("Operation Complete !")

    msg = robot_accessoriesResponse()
    msg.respone_msg = True
    return msg

if __name__ == "__main__":
    rospy.init_node('robot_accessories_server')
    s = rospy.Service('/robot_accessories_controller', robot_accessories, handle_switch)
    print("Ready to control robot accessories ...")
    rospy.spin()

#!/usr/bin/env python3
'''Service Client Code'''

import rospy
from chapter3.srv import robot_accessories, robot_accessoriesRequest, robot_accessoriesResponse

if __name__ == '__main__':
    rospy.init_node("robot_accessories_client")
    rospy.wait_for_service("/robot_accessories_controller")

    try:
        response = robot_accessoriesResponse()
        robot_accessories_service = rospy.ServiceProxy("/robot_accessories_controller", robot_accessories)
        led_front = input("Enter ON/OFF for led_front: ")
        led_left = input("Enter ON/OFF for led_left: ")
        led_right = input("Enter ON/OFF for led_right: ")
        led_rear = input("Enter ON/OFF for led_rear: ")
        music_id = input("Enter a number for music_id: ")
        screen_message = input("Enter a text for screen_message: ")

        req = robot_accessoriesRequest()

        req.request_msg.led_front = False
        req.request_msg.led_left = False
        req.request_msg.led_right = False
        req.request_msg.led_rear = False

        if(led_front == "ON"):
            req.request_msg.led_front = True
        if(led_left == "ON"):
            req.request_msg.led_left = True
        if(led_right == "ON"):
            req.request_msg.led_right = True
        if(led_rear == "ON"):
            req.request_msg.led_rear = True

        req.request_msg.music_id = int(music_id)
        req.request_msg.screen_message = screen_message

        response = robot_accessories_service(req) #service call
        rospy.loginfo("Response from Server: " + str(response.respone_msg))
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed: " + str(e))
        rospy.loginfo("Response from Server: Exception !")

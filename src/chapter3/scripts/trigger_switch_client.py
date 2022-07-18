#!/usr/bin/env python3
'''Service Client Code'''

import rospy
from std_srvs.srv import SetBool, SetBoolResponse

if __name__ == '__main__':
    rospy.init_node("trigger_switch_client")
    rospy.wait_for_service("/trigger_switch")

    try:
        response = SetBoolResponse()
        trigger_switch_service = rospy.ServiceProxy("/trigger_switch", SetBool)
        while True:
            trigger = input("Enter ON/OFF to trigger switch: ")
            if(trigger == "ON" or trigger == "on"):
                response = trigger_switch_service(True) #service call
                break
            if(trigger == "OFF" or trigger == "off"):
                response = trigger_switch_service(False) #service call
                break
            rospy.loginfo("Invalid input. Please try again.")
            continue
        rospy.loginfo("Response from Server:")
        rospy.loginfo("success- " + str(response.success))
        rospy.loginfo("message- " + str(response.message))
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed: " + str(e))
        rospy.loginfo("Response from Server:")
        rospy.loginfo("success- " + "False")
        rospy.loginfo("message- " + "Exception !")

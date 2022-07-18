#!/usr/bin/env python3
'''Service Server Code'''

import rospy
from std_srvs.srv import SetBool, SetBoolResponse

def handle_switch(req):
    '''Service handler'''
    rospy.loginfo("received request: " + str(req))
    reply_msg = SetBoolResponse()
    if req.data:
        reply_msg.success = True
        reply_msg.message = "Switch triggered ON"
    else:
        reply_msg.success = True
        reply_msg.message = "Switch triggered OFF"
    return reply_msg

if __name__ == "__main__":
    rospy.init_node('trigger_switch_server')
    s = rospy.Service('/trigger_switch', SetBool, handle_switch)
    print("Ready to trigger switch")
    rospy.spin()

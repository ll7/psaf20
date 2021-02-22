#!/usr/bin/env python3

"""
if the set_position_server is running, i can set a postion

TODO:
- read from ros param and set position
"""

import rospy
from geometry_msgs.msg import Pose

from psaf20_competition_manager.srv import SetPosition

def set_position_client():
    rospy.wait_for_service('set_position')
    try:
        set_position = rospy.ServiceProxy('set_position', SetPosition)
        
        position = Pose()
        
        position.position.x = rospy.get_param('competition/start/position/x')
        position.position.y = rospy.get_param('competition/start/position/y')
        position.position.z = rospy.get_param('competition/start/position/z')
        
        position.orientation.x = rospy.get_param(
            'competition/start/orientation/x')
        position.orientation.y = rospy.get_param(
            'competition/start/orientation/y')
        position.orientation.z = rospy.get_param(
            'competition/start/orientation/z')
        position.orientation.w = rospy.get_param(
            'competition/start/orientation/w')
        print(position)
        
        position_set = set_position(set_position = True, pose = position)
        return position_set
    except rospy.ServiceException as e:
        print("Service call failed: %s" %e)
        return False

if __name__=="__main__":
    print('Requesting to set_position')
    if set_position_client():
        print('position_set successful')
    else:
        print('position_set unsuccessful')
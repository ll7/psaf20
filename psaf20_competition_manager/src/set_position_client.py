#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose

from psaf20_competition_manager.srv import SetPosition

def set_position_client():
    rospy.wait_for_service('set_position')
    try:
        set_position = rospy.ServiceProxy('set_position', SetPosition)
        # TODO: set a pose
        position = Pose()
        position.position.x = 120.0
        position.position.y = 194.0
        position.position.z = 0.0
        print(position)
        #position.orientation = [0.0, 0.0, 0.0, 1.0]
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
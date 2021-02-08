#!/usr/bin/env python3

import rospy

from psaf20_competition_manager.srv import SavePosition

def save_position_client():
    rospy.wait_for_service('save_position')
    try:
        safe_position = rospy.ServiceProxy('save_position', SavePosition)
        saved = safe_position(True)
        return True

    except rospy.ServiceException as e:
        print("Service call failed: %s" %e)
        return False

if __name__ == '__main__':
    print("Requesting save_position")
    save_position_client()

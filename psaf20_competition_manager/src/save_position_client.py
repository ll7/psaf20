#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix
from rosgraph_msgs.msg import Clock

from psaf20_competition_manager.srv import SavePosition

def save_position_client(odom):
    rospy.wait_for_service('save_position')

    try:
        safe_position = rospy.ServiceProxy('save_position', SavePosition)
        saved = safe_position(save = True, position = odom, GPS = NavSatFix())
        return saved
    except rospy.ServiceException as e:
        print("Service call failed: %s" %e)
        return False

if __name__ == '__main__':
    print("Requesting save_position")
    print(rospy.wait_for_message('/carla/ego_vehicle/odometry', Odometry, timeout=1))
    try:
        odom = rospy.wait_for_message("carla/ego_vehicle/odometry", Odometry, timeout=1)
    except rospy.ROSException as e:
        odom = Odometry()
        print("wait_for_message failed: %s" %e)

    save_position_client(odom)

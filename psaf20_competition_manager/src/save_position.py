#!/usr/bin/env python3

import rospy

from nav_msgs.msg import Odometry

odom = Odometry()

def save_odom(data):
    if rospy.get_param('/save_position'):
        print(data)
        rospy.set_param('/save_position', False)

def listener():
    rospy.init_node('save_position', anonymous=True)
    rospy.Subscriber('/carla/ego_vehicle/odometry', Odometry, save_odom)
    rospy.spin()

if __name__ == '__main__':
    rospy.set_param('/save_position', False)
    listener()
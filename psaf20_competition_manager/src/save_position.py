#!/usr/bin/env python3

import rospy
import carla

from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix

positions = dict()


def save_odom(data):
    if rospy.get_param('/save_position'):
        map = world.get_map()
        map_name = map.name
        print('Current Town: ' + map_name)
        print('')
        print('=== Odometry ===')
        print(data)
        rospy.set_param('/save_position', False)

def save_gps(data):
    if rospy.get_param('/save_position'):
        print('=== GPS ===')
        print(data)
        rospy.set_param('/save_position', False)

def listener():
    rospy.init_node('save_position', anonymous=True)
    rospy.Subscriber('/carla/ego_vehicle/odometry', Odometry, save_odom)
    rospy.Subscriber('/carla/ego_vehicle/gnss/gnss1/fix', NavSatFix, save_gps)
    rospy.spin()

if __name__ == '__main__':
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0) # seconds
    world = client.get_world()
    rospy.set_param('/save_position', False)
    listener()
#! /usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point


def get_distance(A: Point, B: Point):
    """
    return distance of two points
    """
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2 + (A.z - B.z) ** 2) ** 0.5


def callback(data):
    rospy.logdebug(data)
    current_postion = data.pose.pose.position
    goal_position = Point(
        x=rospy.get_param('competition/goal/position/x'),
        y=rospy.get_param('competition/goal/position/y'),
        z=rospy.get_param('competition/goal/position/z'))
    distance_to_goal = get_distance(current_postion, goal_position)
    rospy.loginfo('distance to goal: {}'.format(distance_to_goal))
    
    start_position = Point(
        x=rospy.get_param('competition/start/position/x'),
        y=rospy.get_param('competition/start/position/y'),
        z=rospy.get_param('competition/start/position/z'))
    distance_to_start = get_distance(current_postion, start_position)
    rospy.loginfo('distance to start: {}'.format(distance_to_start))
    

def competition_manager():
    rospy.init_node('competion_manager')
    rospy.Subscriber("carla/ego_vehicle/odometry", Odometry, callback)
    rospy.spin()
    
if __name__ == '__main__':
    print('Init competion_manager')
    competition_manager()

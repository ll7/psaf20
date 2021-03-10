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
    
    start_position = Point(
        x=rospy.get_param('competition/start/position/x'),
        y=rospy.get_param('competition/start/position/y'),
        z=rospy.get_param('competition/start/position/z'))
    distance_to_start = get_distance(current_postion, start_position)

    if not rospy.get_param('competition/finished'):
        rospy.loginfo('distance to goal: {}'.format(distance_to_goal))
        rospy.loginfo('distance to start: {}'.format(distance_to_start))
    
    if not rospy.get_param('competition/started'):
        if distance_to_start > 0.5:
            rospy.set_param('competition/started', True)
            rospy.set_param(
                'competition/start_time', rospy.get_rostime().to_sec())
            rospy.logwarn(
                'competition started at: {}'.format(
                    rospy.get_param('/competition/start_time')))

    if rospy.get_param('competition/started') and not rospy.get_param('competition/finished'):
        if distance_to_goal < 1.0:
            rospy.set_param('competition/finished', True)
            rospy.set_param(
                'competition/finish_time', rospy.get_rostime().to_sec())
            duration = (rospy.get_param('competition/finish_time')
                - rospy.get_param('competition/start_time'))
            rospy.set_param('competition/duration', duration)
            rospy.logwarn(
                'The competition was completed in {} seconds'.format(duration))



def competition_manager():
    rospy.init_node('competion_manager')
    rospy.Subscriber("carla/ego_vehicle/odometry", Odometry, callback)
    rospy.set_param('competition/ready_for_ego', True)
    rospy.spin()
    
if __name__ == '__main__':
    print('Init competion_manager')
    rospy.set_param('competition/started', False)
    rospy.set_param('competition/finished', False)
    competition_manager()

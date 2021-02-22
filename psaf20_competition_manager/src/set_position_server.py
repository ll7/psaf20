#!/usr/bin/env python3

import rospy
from psaf20_competition_manager.srv import SetPosition
from geometry_msgs.msg import PoseWithCovarianceStamped

def handle_set_position(req):

    if req.set_position:
        print('set_position now')
        
        position_publisher = rospy.Publisher(
        '/carla/ego_vehicle/initialpose', 
        PoseWithCovarianceStamped, queue_size=10)
        position = PoseWithCovarianceStamped()
        position.pose.pose = req.pose
        position_publisher.publish(position)
        
        # Timing
        now = rospy.get_rostime().to_sec()
        rospy.set_param('competition/init/start_time', now)
        rospy.loginfo('position set at rostime: {}'.format(now))

        return True
    else:
        print('Dont set position')
        return False

def set_position_server():
    rospy.init_node('set_position_server')
    service = rospy.Service(
        'set_position', SetPosition, handle_set_position)
    print('Ready to set_position.')
    rospy.spin()

if __name__ == '__main__':
    set_position_server()
#!/usr/bin/env python3

import rospy
from psaf20_competition_manager.srv import SavePosition

def handle_save_position(req):
    """
    @param args:
    save: bool =
    Odometry: nav_msgs/Odometry
    """

    if req.save:
        print('save new position now')
        print('=== Odomentry ===')
        print(req.position)
        print('')
        print('=== GPS ===')
        print(req.GPS)
        return True
    else:
        print('dont save position now')
        return False

def save_position_server():
    rospy.init_node('save_position_server')
    service = rospy.Service('save_position', SavePosition, handle_save_position)
    print('Ready to save a position.')
    rospy.spin()

if __name__ == '__main__':
    save_position_server()
    

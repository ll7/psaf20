#!/usr/bin/env python3

import rospy
from psaf20_competition_manager.srv import SavePosition

def handle_save_position(req):
    
    prefix = '/competition/current_pose'
    if req.save:
        print('save new position now')

        # save position
        rospy.set_param(
            prefix + '/position/x', req.position.pose.pose.position.x)
        rospy.set_param(
            prefix + '/position/y', req.position.pose.pose.position.y)
        rospy.set_param(
            prefix + '/position/z', req.position.pose.pose.position.z)
        
        # save orientation
        rospy.set_param(
            prefix + '/orientation/x', req.position.pose.pose.orientation.x)
        rospy.set_param(
            prefix + '/orientation/y', req.position.pose.pose.orientation.y)
        rospy.set_param(
            prefix + '/orientation/z', req.position.pose.pose.orientation.z)
        rospy.set_param(
            prefix + '/orientation/w', req.position.pose.pose.orientation.w)
        
        print('saved ego_vehicle position to ' + prefix + 'in the parameters')
        print('save to yaml with: ')
        print('rosparam dump ~/carla-ros-bridge/psaf20/psaf20_competition_manager/config/TownXY/PositionXY.yaml '+ prefix)
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
    

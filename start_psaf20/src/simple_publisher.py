#!/usr/bin/env python

import rospy
from carla_msgs.msg import CarlaEgoVehicleControl

def simple_publisher():
    role_name = rospy.get_param('~role_name', 'ego_vehicle')
    pub = rospy.Publisher("/carla/" + role_name + "/vehicle_control_cmd",
            CarlaEgoVehicleControl, CarlaEgoVehicleControl, queue_size=10)
    rospy.init_node('simple_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10 Hz
    while not rospy.is_shutdown():
        control = CarlaEgoVehicleControl()
        control.throttle = 0.7
        # rospy.loginfo(control.throttle)
        pub.publish(control)
        rate.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass
    


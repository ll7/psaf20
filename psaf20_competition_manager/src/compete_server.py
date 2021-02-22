#! /usr/bin/env python3

import rospy

import actionlib
from std_msgs.msg import float32
import psaf20_competition_manager.msg

class compete_action(object):
    _feedback = psaf20_competition_manager.msg.CompeteFeedback
    _result = psaf20_competition_manager.msg.CompeteResult

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, psaf20_competition_manager.CompeteAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()

    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True

        rospy.loginfo('%s: Executing.' % (self._action_name))




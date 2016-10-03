#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.

import roslib
roslib.load_manifest('social_navigation')
import rospy

import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
  br = tf.TransformBroadcaster()
  br.sendTransform((msg.x, msg.y, 0),
                   tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                   rospy.Time.now(),
                   turtlename,
                   "world")

if __name__ == '__main__':
  rospy.init_node('turtle_tf_broadcaster')
  turtlename = rospy.get_param('~turtle')
  rospy.Subscriber('/%s/pose' % turtlename,
                   turtlesim.msg.Pose,
                   handle_turtle_pose,
                   turtlename)
  rospy.spin()

#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import numpy

def simple_subscriber():
    pub = rospy.Publisher('random_float_log', Float32, queue_size=10)
    rospy.init_node('simple_subscriber')
    def callback(data):
        pub.publish(numpy.log(data.data))
    rospy.Subscriber('my_random_float', Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    simple_subscriber()

#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import random

def simple_publisher():
    pub = rospy.Publisher('my_random_float', Float32, queue_size=10)
    rospy.init_node('simple_publisher')
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        random_number = random.random()*10
        pub.publish(random_number)
        rate.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass

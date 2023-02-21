#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace

def open_space_publisher():
    pub = rospy.Publisher('open_space', OpenSpace, queue_size=10)
    rospy.init_node('open_space_publisher')
    def callback(scan):
        max_range = max(scan.ranges)
        index_max = scan.ranges.index(max_range)
        angle = scan.angle_min + index_max*scan.angle_increment
        space = OpenSpace(angle=angle, distance=max_range)
        pub.publish(space)
    rospy.Subscriber('fake_scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher()

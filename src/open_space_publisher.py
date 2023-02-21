#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

def open_space_publisher():
    pub_distance = rospy.Publisher('open_space/distance', Float32, queue_size=10)
    pub_angle = rospy.Publisher('open_space/angle', Float32, queue_size=10)
    rospy.init_node('open_space_publisher')
    def callback(scan):
        max_range = max(scan.ranges)
        index_max = scan.ranges.index(max_range)
        angle = scan.angle_min + index_max*scan.angle_increment
        pub_distance.publish(max_range)
        pub_angle.publish(angle)
    rospy.Subscriber('fake_scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher()

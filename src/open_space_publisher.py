#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace

def open_space_publisher():
    rospy.init_node('open_space_publisher')
    subscriber_topic = rospy.get_param("subscriber_topic", "fake_scan")
    publisher_topic = rospy.get_param("publisher_topic", "open_space")
    pub = rospy.Publisher(publisher_topic, OpenSpace, queue_size=10)
    def callback(scan):
        max_range = max(scan.ranges)
        index_max = scan.ranges.index(max_range)
        angle = scan.angle_min + index_max*scan.angle_increment
        space = OpenSpace(angle=angle, distance=max_range)
        pub.publish(space)
    rospy.Subscriber(subscriber_topic, LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher()

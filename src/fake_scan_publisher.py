#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
import math
import random

def fake_scan_publisher():
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
    rospy.init_node('fake_scan_publisher')
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        time = rospy.get_rostime()
        frame = "base_link"
        angle_min = math.pi*-2/3
        angle_max = math.pi*2/3
        angle_increment = math.pi/300
        scan_time = 1/20
        range_min = 1
        range_max = 10
        ranges = [random.random()*(range_max-range_min) + range_min for e in range(0, int(round((angle_max-angle_min)/angle_increment) + 1))]
        scan = LaserScan(
            header=Header(
                stamp=time,
                frame_id=frame
            ),
            angle_min=angle_min,
            angle_max=angle_max,
            angle_increment=angle_increment,
            time_increment=scan_time,
            range_min=range_min,
            range_max=range_max,
            ranges=ranges)
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_scan_publisher()
    except rospy.ROSInterruptException:
        pass

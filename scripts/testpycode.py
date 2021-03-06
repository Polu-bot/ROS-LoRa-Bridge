#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8

def talker():
    pub = rospy.Publisher('rcommand', Int8, queue_size=10)
    rospy.init_node('testcommand', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = 1
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

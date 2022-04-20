#!/usr/bin/python3

from shutil import move
from turtle import pos
import rospy
from geometry_msgs.msg import Twist
import sys
from turtlesim.msg import Pose


def move_turtle(line_vel, ang_vel):
    rospy.init_node("turtlemove", anonymous=True)
    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    while True:

        vel.linear.x = line_vel
        vel.linear.y = line_vel
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel

        pub.publish(vel)
        rate.sleep()


move_turtle(1.0, 2.5)

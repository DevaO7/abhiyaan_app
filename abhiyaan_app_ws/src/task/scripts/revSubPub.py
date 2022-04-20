#!/usr/bin/python3
# Subscribes to /team_abhiyaan and Publishes the
# received string in reverse to /naayihba_maet
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

# Subscriber


def listener():

    rospy.init_node('listenerAndtalkerS', anonymous=True)

    rospy.Subscriber('/team_abhiyaan', String, callback)

    rospy.spin()

# Publisher


def talker():
    pub = rospy.Publisher('/naayihba_meet', String, queue_size=10)
    rospy.init_node('listenerAndtalkerP', anonymous=True)
    rate = rospy.Rate(1)  # 10hz
    while not rospy.is_shutdown():
        hello_str = listener()
        rospy.loginfo(hello_str)
        pub.publish(hello_str[::-1])
        rate.sleep()


if __name__ == '__main__':
    listener()
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

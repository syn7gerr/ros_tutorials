#!/usr/bin/env python

import rospy

from std_msgs.msg import String

def process_data(data_a, data_b):
  processed_data = '\n' + data_a + '\n' + data_b
  return processed_data

if __name__ == '__main__':
  try:
    rospy.init_node('example_node', anonymous=True)

    channel = rospy.get_param("~channel")
    data_a = rospy.get_param("~data_1")
    data_b = rospy.get_param("~data_2")

    pub = rospy.Publisher(channel, String, queue_size = 10)
    ros_string = String()

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
      ros_string.data = process_data(data_a,data_b)
      pub.publish(ros_string)
      rate.sleep()

  except rospy.ROSInterruptException:
    pass
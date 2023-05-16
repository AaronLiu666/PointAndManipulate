#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Point

def point_pairs_cb(msg):
    # Convert received message to list of tuples representing point pairs
    point_pairs = []
    for i in range(0, len(msg.data), 6):
        point1 = (msg.data[i], msg.data[i+1], msg.data[i+2])
        point2 = (msg.data[i+3], msg.data[i+4], msg.data[i+5])
        point_pairs.append((point1, point2))

    # Create Marker message for line strip
    line_strip_msg = Marker()
    line_strip_msg.pose.orientation.x = 0
    line_strip_msg.pose.orientation.y = 0
    line_strip_msg.pose.orientation.z = 0
    line_strip_msg.pose.orientation.w = 1

    line_strip_msg.header.frame_id = 'world'
    line_strip_msg.type = Marker.LINE_STRIP
    line_strip_msg.action = Marker.ADD
    line_strip_msg.scale.x = 0.1 # Line thickness
    line_strip_msg.color.r = 1.0 # Line color (red)
    line_strip_msg.color.a = 1.0 # Line alpha (opacity)

    # Update the points of the line strip
    points = []
    for point_pair in point_pairs:
        points.extend([Point(x=p[0], y=p[1], z=p[2]) for p in point_pair])
    line_strip_msg.points = points

    # Publish the line strip to marker topic
    line_strip_msg.header.stamp = rospy.Time.now()
    marker_pub.publish(line_strip_msg)

if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('line_strip_visualizer')

    # Set up ROS publisher for marker topic
    marker_pub = rospy.Publisher('/lines', Marker, queue_size=10)

    # Set up ROS subscriber for point pairs topic
    point_sub = rospy.Subscriber('/coords', Float32MultiArray, point_pairs_cb)

    # Spin until shutdown
    rospy.spin()

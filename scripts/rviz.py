#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2

def callback(data):
    # Convert Float32MultiArray to list of tuples
    n_points = len(data.data) // 3
    points = [tuple(data.data[i:i+3]) for i in range(0, len(data.data), 3)]

    # Set up PointCloud2 message
    header = rospy.Header(frame_id='world')
    fields = [point_cloud2.PointField(name='x', offset=0, datatype=7, count=1),
              point_cloud2.PointField(name='y', offset=4, datatype=7, count=1),
              point_cloud2.PointField(name='z', offset=8, datatype=7, count=1)]
    cloud = point_cloud2.create_cloud(header, fields, points)

    # Publish PointCloud2 message
    pub.publish(cloud)

if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('point_cloud_publisher')

    # Define publisher
    pub = rospy.Publisher('my_point_cloud_topic', PointCloud2, queue_size=10)

    # Define subscriber
    sub = rospy.Subscriber('coords', Float32MultiArray, callback)

    # Spin until node is stopped
    rospy.spin()

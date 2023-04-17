#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray

class JitteringFilterNode:
    def __init__(self):
        # Initialize ROS node, subscribers, and publisher
        rospy.init_node('jittering_filter_node')
        self.sub = rospy.Subscriber('/coords', Float32MultiArray, self.data_callback)
        self.pub = rospy.Publisher('/filtered_coords', Float32MultiArray, queue_size=1)

        # Initialize filter variables
        self.window_size = rospy.get_param('~window_size', 5)  # Get window size from parameter server
        self.data_buffer = []

    def data_callback(self, msg):
        # Convert sensor data message to numpy array
        data = np.array(msg.data)

        # Apply moving average filter to remove jittering
        if len(self.data_buffer) < self.window_size:
            # Fill buffer with initial data
            self.data_buffer.append(data)
            filtered_data = data
        else:
            # Remove oldest data point and add newest data point to buffer
            self.data_buffer.pop(0)
            self.data_buffer.append(data)

            # Compute moving average of data in buffer
            filtered_data = np.mean(self.data_buffer, axis=0)

        # Publish filtered data
        filtered_msg = Float32MultiArray()
        filtered_msg.data = filtered_data.tolist()
        self.pub.publish(filtered_msg)

if __name__ == '__main__':
    try:
        node = JitteringFilterNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

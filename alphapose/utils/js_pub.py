import rospy
from std_msgs.msg import Float32MultiArray

def talker(coord):
    # initialize node and publisher
    rospy.init_node('tensor_publisher')
    pub = rospy.Publisher('/tensor_coordinates', Float32MultiArray, queue_size=10)

    # create message
    msg = Float32MultiArray()
    msg.data = coord

    # publish message
    # while not rospy.is_shutdown():
        # pub.publish(msg)
    pub.publish(msg)
    
if __name__ == '__main__':
    try:
        talker([1,2,3])
    except rospy.ROSInterruptException:
        pass
    
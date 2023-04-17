import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray
import ros_numpy as rn

diff = []

def callback1(data):
    global diff
    # rospy.loginfo(data)
    # print('111')
    # print(type(data))
    a = np.array(data.data, dtype=np.float32)
    a = np.array(a).reshape(-1,3)
    diff = a
    # a = rn.numpify(data.data)
    print(a) #EB_L ,EB_R,WR_L,WR_R
    
def callback2(data):
    global diff
    # rospy.loginfo(data)
    # print('111')
    # print(type(data))
    a = np.array(data.data, dtype=np.float32)
    a = np.array(a).reshape(-1,3)
    diff -= a
    # a = rn.numpify(data.data)
    # print(a) #EB_L ,EB_R,WR_L,WR_R
    
def calculate():
    rospy.loginfo(diff)
    
    
    
def listener():
    rospy.init_node('comparer', anonymous=True)
    rospy.Subscriber('/coords', Float32MultiArray, callback1, queue_size=10)
    rospy.Subscriber('/filtered_coords', Float32MultiArray, callback2, queue_size=10)
    rospy.spin()
    
if __name__ == '__main__':
    listener()

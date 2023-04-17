import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray
import ros_numpy as rn

def callback(data):
    # rospy.loginfo(data)
    # print('111')
    # print(type(data))
    a = np.array(data.data, dtype=np.float32)
    a = np.array(a).reshape(-1,3)
    # a = rn.numpify(data.data)
    print(len(data.data)) #EB_L ,EB_R,WR_L,WR_R
    
    
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/coords', Float32MultiArray, callback, queue_size=10)
    rospy.spin()
    
if __name__ == '__main__':
    listener()

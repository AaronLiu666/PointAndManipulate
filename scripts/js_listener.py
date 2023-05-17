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
    # print(a) #EB_L ,EB_R,WR_L,WR_R
    line_left = line_equation(a[0], a[2])
    line_right = line_equation(a[1], a[3])
    left_location = get_xy_at_z(line_left,0)
    print(left_location)
    
def line_equation(point1, point2):
    """
    计算空间中已知两点位置的直线方程

    Parameters:
        point1 (tuple or list): 直线上的第一个点坐标，格式为 (x, y, z)
        point2 (tuple or list): 直线上的第二个点坐标，格式为 (x, y, z)

    Returns:
        tuple: 包含直线方向向量和截距的元组，格式为 (direction_vector, intercept)
        
    """
    # 计算直线方向向量
    direction_vector = (point2[0]-point1[0], point2[1]-point1[1], point2[2]-point1[2])
    
    # 计算直线截距
    intercept = point1[1] - ((point1[1]-point2[1])/(point1[0]-point2[0]))*point1[0]
    
    return (direction_vector, intercept)

def get_xy_at_z(line_equation, z):
    """
    计算给定直线方程在指定 z 坐标处的 xy 坐标

    Parameters:
        line_equation (tuple): 直线方程，包含方向向量和截距信息，格式为 ((x,y,z), intercept)
        z (float): 指定的 z 坐标

    Returns:
        tuple: 包含 x 和 y 坐标的元组，格式为 (x, y)
        
    """
    # 解方程 x = (z - b) / a
    x = (z - line_equation[1]) / line_equation[0][2]
    
    # 使用 x 求解 y 
    y = line_equation[0][1] + line_equation[0][0]*(x - line_equation[0][0])/line_equation[0][2]
    
    return (x, y)

    
    
    
def listener():
    rospy.init_node('listener', anonymous=True)
    # rospy.Subscriber('/filtered_coords', Float32MultiArray, callback, queue_size=10)
    rospy.Subscriber('/coords', Float32MultiArray, callback, queue_size=10)
    rospy.spin()
    
if __name__ == '__main__':
    listener()

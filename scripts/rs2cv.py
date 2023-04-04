import cv2
import pyrealsense2 as rs
import numpy as np

# 配置pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# 启动pipeline
pipeline.start(config)

# 获取视频流
while True:
    # 等待下一帧
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()

    # 转换为OpenCV格式
    color_image = np.asanyarray(color_frame.get_data())
    cv2.imshow("video", color_image)

    # 按'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
pipeline.stop()
cv2.destroyAllWindows()

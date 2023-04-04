import pyrealsense2 as rs
import cv2
import numpy as np

# create pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
pipeline.start(config)

# create virtual video device
out = cv2.VideoWriter('/dev/video8', cv2.VideoWriter_fourcc(*'YUYV'), 30.0, (640, 480), isColor=True)

try:
    while True:
        # wait for a new frame
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        # convert color frame to YUYV format
        color_image = color_frame.as_frame().get_data()
        color_image = np.array(color_image)
        color_yuyv = cv2.cvtColor(color_image, cv2.COLOR_RGB2YUV_IYUV)

        # write YUYV frame to virtual video device
        out.write(color_yuyv)
        # print('done')

finally:
    # cleanup
    pipeline.stop()
    out.release()

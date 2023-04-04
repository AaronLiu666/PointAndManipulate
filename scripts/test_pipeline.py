import pyrealsense2 as rs
import cv2
import numpy as np

# create pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

try:
    while True:
        # wait for new frames
        frames = pipeline.wait_for_frames()

        # get color frame
        color_frame = frames.get_color_frame()

        # convert color frame to OpenCV format
        color_image = np.asanyarray(color_frame.get_data())
        color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)

        # display color frame in window
        cv2.imshow('RealSense D435i', color_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # cleanup
    pipeline.stop()
    cv2.destroyAllWindows()

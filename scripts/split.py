import pyrealsense2 as rs
import cv2 as cv
import numpy as np

# create pipeline for video source
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

# create video capture objects
depth_capture = cv.VideoCapture(8)
color1_capture = cv.VideoCapture(9)
color2_capture = cv.VideoCapture(10)

while True:
    # read frames from pipeline
    frames = pipeline.wait_for_frames()

    # extract depth frame
    depth_frame = frames.get_depth_frame()

    # extract color frames
    color1_frame = frames.get_color_frame()
    color2_frame = frames.get_color_frame()

    # convert frames to numpy arrays
    depth_image = np.asanyarray(depth_frame.get_data())
    color1_image = np.asanyarray(color1_frame.get_data())
    color2_image = np.asanyarray(color2_frame.get_data())

    # display frames
    cv.imshow('Depth Frame', depth_image)
    cv.imshow('Color Frame 1', color1_image)
    cv.imshow('Color Frame 2', color2_image)

    # check for exit key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
pipeline.stop()
depth_capture.release()
color1_capture.release()
color2_capture.release()
cv.destroyAllWindows()

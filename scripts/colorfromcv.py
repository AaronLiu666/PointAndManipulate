import cv2
import pyrealsense2 as rs
import numpy as np

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

profile = pipeline.start(config)
align = rs.align(rs.stream.color)

capture = cv2.VideoCapture(6)

while True:
    _, color_image = capture.read()
    # cv2.imshow(color_image)

    # Get aligned depth frame
    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)
    depth_frame = aligned_frames.get_depth_frame()

    if not depth_frame:
        continue

    depth_image = np.asanyarray(depth_frame.get_data())

    # do something with the aligned color and depth frames
    # cv2.imshow(color_image)

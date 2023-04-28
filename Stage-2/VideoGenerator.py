# This code helps in building a new video file using extracted key frames
# Here the key frames are extracted using Frame Interval Method

import cv2


input_file = "Sample-1-HR.mp4" # name of input video file
output_file = "output_video.mp4" # name of output video file
max_frames = 100000000000 # maximum number of frames to extract
start_frame = 0 # starting frame number
frame_interval = 10 # interval between extracted frames

cap = cv2.VideoCapture(input_file)
if not cap.isOpened():
    print("Error opening video file")

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

count = 0
while cap.isOpened() and count < max_frames:
    ret, frame = cap.read()
    if not ret:
        break
    if count < start_frame:
        count += 1
        continue
    if count % frame_interval != 0:
        count += 1
        continue

    # process frame here (e.g. apply filters or object detection)

    out.write(frame) # write the frame to the output video file
    count += 1

cap.release()
out.release()
cv2.destroyAllWindows()

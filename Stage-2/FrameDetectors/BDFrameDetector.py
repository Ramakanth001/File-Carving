import cv2
import os

# Create output directory to save the frames
output_dir = r'D:\File-Carving\Stage-2\ExtractedFrames\BGSub_Frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open input video file
video_path = r"VideoSamples/Sample-1-HR.mp4"
cap = cv2.VideoCapture(video_path)

# Initialize key frame detection parameters
# params = cv2.SimpleBlobDetector_Params()
# params.minThreshold = 50
# params.maxThreshold = 200
# params.filterByArea = True
# params.minArea = 200
# params.filterByCircularity = False
# params.filterByConvexity = False
# params.filterByInertia = False
# params.minDistBetweenBlobs = 50
# detector = cv2.SimpleBlobDetector_create(params)

params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 50
params.maxThreshold = 200
params.filterByArea = True
params.minArea = 200
params.filterByCircularity = True
params.minCircularity = 0.8
params.filterByConvexity = True
params.minConvexity = 0.9
params.filterByInertia = True
params.minInertiaRatio = 0.2
params.filterByColor = False
params.blobColor = 255
params.minDistBetweenBlobs = 50

detector = cv2.SimpleBlobDetector_create(params)

try:
  # Loop over video frames and detect key frames
  count = 0
  while cap.isOpened():
    # Read next video frame
    ret, frame = cap.read()
    if not ret:
        break

    # Detect key points in frame using blob detection
    key_points = detector.detect(frame)

    # If key points are detected, save frame as output image
    if len(key_points) > 0:
        # Save frame as image
        frame_path = os.path.join(output_dir, 'frame_{:04d}.png'.format(count))
        cv2.imwrite(frame_path, frame)
        print('Saved key frame: {}'.format(frame_path))
        count += 1

except KeyboardInterrupt :
     print("Blob Detection Frame Extraction Halted!!!\nNumber of Frames Extracted :" , count)

# Release input video file
cap.release()
cv2.destroyAllWindows()
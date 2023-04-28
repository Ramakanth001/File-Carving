import cv2
import os

# Set threshold for absolute difference
threshold = 15500000

# Create output directory to save the frames
output_dir = r'D:\File-Carving\Stage-2\ExtractedFrames\AMD_Frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open input video file
video_path = r"VideoSamples/Sample-1-HR.mp4"
cap = cv2.VideoCapture(video_path)

# Read first frame
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

try:
  # Loop over video frames and detect key frames
  count = 0
  while cap.isOpened():
    # Read next video frame
    ret, frame = cap.read()
    if not ret:
        break
    # Convert to grayscale and calculate absolute difference
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prev_gray, gray)

    # If difference is greater than threshold, save frame as output image
    if diff.sum() > threshold:
        frame_path = os.path.join(output_dir, f'frame_{count:04d}.png')
        cv2.imwrite(frame_path, frame)
        print('Saved key frame: {}'.format(frame_path))
        count += 1

    # Set current frame as previous frame for next iteration
    prev_gray = gray.copy()

except KeyboardInterrupt :
        print("AMD Frame Extraction Halted!!! \nNumber of Frames Extracted :" , count)
# Release input video file
cap.release()
cv2.destroyAllWindows()
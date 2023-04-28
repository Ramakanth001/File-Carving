import cv2
import numpy as np
import os

# Set video path
video_path = r"VideoSamples/Sample-1-HR.mp4"
cap = cv2.VideoCapture(video_path)

# set the output directory path to save the frames
output_dir = r'D:\File-Carving\Stage-2\ExtractedFrames\RMS_Frames'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set threshold value for frame difference
threshold = 9

# Read first frame
ret, previous_frame = cap.read()

# Convert frame to grayscale
# previous_frame = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
previous_frame = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2RGB)

# Set frame counter
frame_counter = 0
try:
    # Loop through video frames
    while(cap.isOpened()):

        # Read current frame
        ret, current_frame = cap.read()

        # Break loop if end of video
        if not ret:
            break

        # Convert current frame to grayscale
        # current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)

        # Compute absolute difference between current frame and previous frame
        diff = cv2.absdiff(current_frame, previous_frame)

        # Compute root mean square difference between current frame and previous frame
        rms_diff = np.sqrt(np.mean(np.square(diff)))

        # If RMS difference exceeds threshold, save frame to output directory
        if rms_diff > threshold:
            current_frame_rgb = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
            output_path = os.path.join(output_dir, 'frame_{0:04d}.png'.format(frame_counter))
            cv2.imwrite(output_path, current_frame_rgb)
            frame_counter += 1
            print('Saved key frame: {}'.format(output_path))

        # Set previous frame to current frame for next iteration
        previous_frame = current_frame

except KeyboardInterrupt:
    print("RMS Frame Extraction Halted!!! \nNumber of Frames Extracted :", frame_counter)

# Release video capture and destroy windows
cap.release()
cv2.destroyAllWindows()



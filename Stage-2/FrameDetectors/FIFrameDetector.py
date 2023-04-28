# BASED ON SAVING EVERY 10TH FRAME (key_frame_interval)
import cv2
import os

output_dir = r'D:\File-Carving\Stage-2\ExtractedFrames\FI_Frames'
# Create the output directory if it doesn't already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video_path = r"VideoSamples/Sample-1-HR.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")

current_frame = 0
key_frame_interval = 10  # Change this value to adjust the key frame extraction interval
# output_dir = "OutputFrames"
# 6000/10 = 600
try:
    count = 0
    # Loop through all frames in the video
    while True:
        # Read the next frame from the video
        ret, frame = cap.read()
        if not ret:
            # End of video
            break

        # Check if this is a key frame
        if current_frame % key_frame_interval == 0:
            # Save the key frame as a PNG image
            # frame_path = os.path.join(output_dir, 'frame_{:04d}.png'.format(count))
            output_path = os.path.join(output_dir, f"frame{current_frame:04}.png")
            cv2.imwrite(output_path, frame)
            print('Saved key frame: {}'.format(output_path))
            count += 1

        # Increment the frame counter
        current_frame += 1

except KeyboardInterrupt:
    print("Frequency Interval Frame Extraction Halted!!! \nNumber of Frames Extracted :", count)
# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()


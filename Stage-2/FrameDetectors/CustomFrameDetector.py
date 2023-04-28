import cv2
import os

video_path = r"VideoSamples/Sample-1-HR.mp4"
cap = cv2.VideoCapture(video_path)

output_dir = r'D:\File-Carving\Stage-2\ExtractedFrames\Custom_Frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

n = int(input("Enter the number of Frames:\n"))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps

print("FPS: ", fps, "\nFrame_count: ", frame_count, "\nDuration", duration)
if not cap.isOpened():
    print("Error opening video file")

current_frame = 0
frame_interval = int(frame_count/n)
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
        if current_frame % frame_interval == 0:
            # Save the key frame as a PNG image
            # frame_path = os.path.join(output_dir, 'frame_{:04d}.png'.format(count))
            output_path = os.path.join(output_dir, f"frame{current_frame:04}.png")
            cv2.imwrite(output_path, frame)
            print('Saved key frame: {}'.format(output_path))
            count += 1

        # Increment the frame counter
        current_frame += 1

except KeyboardInterrupt:
    print("Custom Key Frame Extraction Halted!!! \nNumber of Frames Extracted :", count)
print("Number of Frames Extracted :", count)
# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()


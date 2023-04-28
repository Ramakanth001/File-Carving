import os
import cv2
import shutil
import subprocess

# Define function to split the video into frames
def split_video_into_frames(video_path, output_path):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Initialize variables
    count = 0
    success = True

    # Loop through video frames and save each frame as an image file
    while success:
        # Read next video frame
        success, image = cap.read()

        if success and count < 200:

            # Save frame as image file
            frame_path = os.path.join(output_path, "frame{:06d}.png".format(count))
            cv2.imwrite(frame_path, image)
            print("Frame saved: Frame-", count)
        else:
            break

        # Increment frame count
        count += 1

    # Release video file
    cap.release()

    # Print message to indicate completion
    print("Splitting video into frames completed.")

# Define function to stitch frames back into a video
def stitch_frames_into_video(input_path, output_path, fps):
    # Get a list of all the frame files in the directory
    frame_files = os.listdir(input_path)

    # Sort frame files by their frame number
    frame_files = sorted(frame_files, key=lambda x: int(x[5:-4]))

    # Open the first frame to get frame size and type
    frame_path = os.path.join(input_path, frame_files[0])
    frame = cv2.imread(frame_path)
    height, width, channels = frame.shape

    # Fix for "muxing overhead too high" error when using mp4v codec
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fourcc = cv2.VideoWriter_fourcc(*"X264")

    # Create video writer object
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Loop through the frame files and add them to the video
    for frame_file in frame_files:
        if int(frame_file[5:-4]) % 10 == 0:
            frame_path = os.path.join(input_path, frame_file)

            # Copy frame to output directory using shutil
            shutil.copy2(frame_path, output_path)

            frame = cv2.imread(frame_path)

            # Fix for video stuttering issue in VLC Media Player
            # Write the same frame multiple times
            for i in range(5):
                video_writer.write(frame)

    # Release the video writer
    video_writer.release()

    # Print message to indicate completion
    print("Stitching frames into video completed.")

import cv2
import os

def create_video(frames_path, output_video_path, fps):
    frame_files = os.listdir(frames_path)
    frame_files.sort()

    # Get first image dimensions
    first_frame = cv2.imread(os.path.join(frames_path, frame_files[0]))
    height, width, _ = first_frame.shape

    # Initialize VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write frames to video
    for frame_file in frame_files:
        frame_path = os.path.join(frames_path, frame_file)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)

    print("Video construction is complete")

    # Release resources
    video_writer.release()
    cv2.destroyAllWindows()


# Define input and output paths
video_path = "VideoSamples/Sample-1-HR.mp4"

frames_path = "my_frames"
# Split video into frames
split_video_into_frames(video_path, frames_path)

# Example usage

output_video_path = "output_video.mp4"
fps = 30
create_video(frames_path, output_video_path, fps)

# Stitch frames into a video
# stitch_frames_into_video(frames_path, output_video_path, fps)

# Use VLC Media Player to play the output video
vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" # Change this to your own path

# Fix for video not playing in VLC Media

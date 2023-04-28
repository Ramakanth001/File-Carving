# Function to perform file carving based on background subtraction
# This code extracts frames from a video file based on background subtraction and saves only
# those frames where significant changes in foreground objects are detected.
# The foreground objects identified by the background subtraction algorithm are represented by white pixels in the resulting binary imag
# This binary image can be used to extract the foreground objects from the original frame, for example by applying a mask.

import cv2
import os

# Create output directory to save the frames
output_dir = r'D:\File-Carving\Stage-2\ExtractedFrames\BGSub_Frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

Foreground_Obj_Dir = r'D:\File-Carving\Stage-2\ExtractedFrames\RMS_Frames\ForeGroundObjects'
if not os.path.exists(Foreground_Obj_Dir):
    os.makedirs(Foreground_Obj_Dir)

# Open input video file
video_path = r"VideoSamples/Sample-1-HR.mp4"
cap = cv2.VideoCapture(video_path)

# Define ROI for background subtraction
roi = (500, 200, 800, 500)

# Initialize variables
count = 0
frame_num = 0
try :
    # Loop through video frames and carve out frames based on background subtraction
    while True:
        # Read next video frame
        ret, frame = cap.read()
        if not ret:
            break

        # Skip frames to reduce overall number of frames processed
        if frame_num % 5 != 0:
            frame_num += 1
            continue

        # Get ROI from the current frame
        x, y, w, h = roi
        roi_frame = frame[y:y + h, x:x + w]

        # Convert ROI to grayscale
        gray_roi = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the ROI
        blur_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)

        # Define background subtractor
        fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=99999, detectShadows=False)

        # Apply background subtraction to ROI
        fgmask = fgbg.apply(blur_roi)

        # If significant changes in the foreground are detected, save frame
        if cv2.countNonZero(fgmask) > 5000:
            cv2.imwrite(os.path.join(output_dir, "frame{:06d}.png".format(count)), frame)
            print("Saved: ", "frame{:06d}.png".format(count))
            count += 1
    # Display the foreground objects identified
        cv2.imwrite(os.path.join(Foreground_Obj_Dir, "Foreground_Object{:06d}.png".format(count)), fgmask)
        print("Foreground Object Saved: ", "Foreground_Object{:06d}.png".format(count))

        # Update frame number
        frame_num += 1
except KeyboardInterrupt :
        print("AMD Frame Extraction Halted!!! \nNumber of Frames Extracted :" , count)
# Release video file
cap.release()

# Print message to indicate completion
print("background Substraction completed")


# import cv2
# import os
#
# # Create output directory to save the frames
# output_dir = r'C:\Users\ramak\OneDrive\Desktop\Project\Stage-2\ExtractedFrames\BGSub_Frames'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# Foreground_Obj_Dir = r'C:\Users\ramak\OneDrive\Desktop\Project\Stage-3\ExtractedFrames\BGSub_Frames\Foreground_Objects'
# if not os.path.exists(Foreground_Obj_Dir):
#     os.makedirs(Foreground_Obj_Dir)
#
# # Open input video file
# video_path = r"C:\Users\ramak\OneDrive\Desktop\Project\Stage-3\VideoSamples\Sample-1-HR.mp4"
# cap = cv2.VideoCapture(video_path)
#
# # Define ROI for background subtraction
# roi = (500, 200, 800, 500)
#
# # Initialize variables
# count = 0
# frame_num = 0
#
# # Loop through video frames and carve out frames based on background subtraction
# while True:
#     # Read next video frame
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Get ROI from the current frame
#     x, y, w, h = roi
#     roi_frame = frame[y:y + h, x:x + w]
#
#     # Convert ROI to grayscale
#     gray_roi = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)
#
#     # Apply Gaussian blur to the ROI
#     blur_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)
#
#     # Define background subtractor
#     fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=99999, detectShadows=False)
#
#     # Apply background subtraction to ROI
#     fgmask = fgbg.apply(blur_roi)
#
#     # If significant changes in the foreground are detected, save frame
#     if cv2.countNonZero(fgmask) > 399999:
#         cv2.imwrite(os.path.join(output_dir, "frame{:06d}.png".format(count)), frame)
#         print("Frame Saved: ", "frame{:06d}.png".format(count))
#         count += 1
#
#     # Display the foreground objects identified
#     cv2.imwrite(os.path.join(Foreground_Obj_Dir, "Foreground_Object{:06d}.png".format(count)), fgmask)
#     print("Foreground Object Saved: ", "Foreground_Object{:06d}.png".format(count))
#     # cv2.imshow('Foreground Objects', fgmask)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break
#
#     # Update frame number
#     frame_num += 1
#
# # Release video file
# cap.release()
#
# # Destroy all windows
# cv2.destroyAllWindows()
#
# # Print message to indicate completion
# print("background Substraction completed")

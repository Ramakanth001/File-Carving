# Horn-Schunck method Implimentation
# (Farneback method Implimentation - Commented at EOF)
# We can get better optical flow param value in Farneback method

import cv2
import numpy as np
import os

# Create output directory to save the frames
output_dir = r'D:\File-Carving\Stage-2\ExtractedFrames\OptFlow_Frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open input video file
video_path = r"VideoSamples/Sample-1-HR.mp4"
cap = cv2.VideoCapture(video_path)

# Set up parameters for Horn-Schunck method
alpha = 0.1
num_iterations = 10
epsilon = 0.1

# Define color for flow visualization
color = (0, 255, 0)

# Get first frame and convert it to grayscale
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Initialize u and v as zeros with the same shape as the grayscale image
u = np.zeros_like(prev_gray)
v = np.zeros_like(prev_gray)

# Loop through video frames
# Loop through video frames
count = 0
try:
    while True:
        # Read current frame and convert it to grayscale
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Compute dense optical flow using Horn-Schunck method
        for i in range(num_iterations):
            # Compute derivatives of u, v, and grayscale image
            du_dx = cv2.Sobel(u, cv2.CV_64F, 1, 0, ksize=5)
            du_dy = cv2.Sobel(u, cv2.CV_64F, 0, 1, ksize=5)
            dv_dx = cv2.Sobel(v, cv2.CV_64F, 1, 0, ksize=5)
            dv_dy = cv2.Sobel(v, cv2.CV_64F, 0, 1, ksize=5)
            dt = prev_gray.astype(np.float64) - gray.astype(np.float64) + du_dx + dv_dy

            # Update u and v using the Horn-Schunck equations
            u_avg = cv2.boxFilter(u, cv2.CV_64F, (3,3))
            v_avg = cv2.boxFilter(v, cv2.CV_64F, (3,3))
            u = u_avg - (du_dx * (du_dx*u_avg + dv_dx*v_avg + dt)) / (alpha**2 + du_dx**2 + dv_dx**2 + epsilon)
            v = v_avg - (dv_dy * (du_dx*u_avg + dv_dx*v_avg + dt)) / (alpha**2 + du_dx**2 + dv_dx**2 + epsilon)

        # Draw flow vectors on frame
        for y in range(0, frame.shape[0], 30):
            for x in range(0, frame.shape[1], 30):
                dx, dy = u[y, x], v[y, x]
                if abs(dx) > 10 or abs(dy) > 10:
                    cv2.arrowedLine(frame, (x, y), (int(x + dx), int(y + dy)), color, 1)
        print("Values of params" ,du_dx, du_dy, dv_dx, dv_dy)

        # Display current frame with flow vectors and save it

        # Compute average optical flow magnitude
        flow_mag = np.sqrt(u ** 2 + v ** 2)
        mean_flow = np.mean(flow_mag)

        if count%10 ==0 :
            # Display current frame with flow vectors and save it
            print("Saved: ", "frame{:06d}.png".format(count))
            # cv2.imwrite("frame{:06d}.png".format(count), frame)
            cv2.imwrite(os.path.join(output_dir, "frame{:06d}.png".format(count)), frame)
            print("Optical flow for frame{:06d}.png: {:.2f}".format(count, mean_flow))

        # Update previous frame and grayscale image
        prev_gray = gray
        count += 1

    # Release video file and close all windows
    cap.release()
    cv2.destroyAllWindows()

except KeyboardInterrupt:
    print("Frequency Interval Frame Extraction Halted!!! \nNumber of Frames Extracted :", count)

# Farneback method Implimentation

# import os
# import cv2
#
# # Read video file
# cap = cv2.VideoCapture("Sample-1-HR.mp4")
#
# output_dir = r'C:\Users\ramak\OneDrive\Desktop\Project\Stage-3\opticalFlow'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# # Set parameters for Farneback method
# params = dict(pyr_scale=0.5, levels=3, winsize=15, iterations=3, poly_n=5, poly_sigma=1.2, flags=0)
#
# # Define color for flow visualization
# color = (0, 255, 0)
#
# # Loop through video frames
# ret, prev_frame = cap.read()
# prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
# count = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Convert current frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Compute optical flow using Farneback method
#     flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, **params)
#     flow_mean = cv2.mean(flow)[0]
#     print("Frame {:d}: Optical flow: {:f}".format(count, flow_mean))
#
#     # Draw flow vectors on frame
#     for y in range(0, frame.shape[0], 20):
#         for x in range(0, frame.shape[1], 20):
#             dx, dy = flow[y, x]
#             if abs(dx) > 1 or abs(dy) > 1:
#                 cv2.arrowedLine(frame, (x, y), (int(x + dx), int(y + dy)), color, 1)
#
#     # Display current frame with flow vectors
#     cv2.imwrite(os.path.join(output_dir, "frame{:06d}.png".format(count)), frame)
#     print("Saved frame {:d}".format(count))
#
#     # Update previous frame and grayscale image
#     prev_gray = gray
#     count += 1
#
# # Release video file and close all windows
# cap.release()
# cv2.destroyAllWindows()

Congrats on making it this far!!!!

In this stage, we will try to identify all the frames from the given video 
 
Identification of anchor frames is done using 4 methods:
1. Frame-Interval Method (FIM)
2. Blob Detection using a set of Detection Parameters (BDM)
3. Absolute Mean Difference Method (AMD)
4. Root Mean Square Method (RMS)

FI_Frames Contains output frames of Frame-Interval Method
BD_Frames Contains output frames of
AMD_Frames Contains output frames of
RMS_Frames folder contains output frames of RMS Method

AMD METHOD:

FRAMES : A B C D E ..... Y Z
Threshold = 8 (Assume)
VAL_AB=DELTA(A-B)
VAL_AB> Threshold:
	classify-KF
	Frame-1=Frame-2
Frame-2 : Updates to next Frame

VAL_BD=DELTA(A-B)
VAL_AB> Threshold:
	classify-KF
	Frame-1=Frame-2
Frame-2 : Updates to next Frame






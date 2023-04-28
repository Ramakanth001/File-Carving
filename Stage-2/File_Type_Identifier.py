# This program helps us identify the type of the given file (partial or accessible) using various methods:
# 1. Based on FileType Module
# 2. Based on Signature
# 3. Based on Metadata
# 4. Based on Content

import magic
import filetype
import cv2
from collections import Counter

def carve_by_signature(file_path):
    signature_mapping = {
        b"\xFF\xD8\xFF": "jpg",
        b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A": "png",
        b"\x47\x49\x46\x38\x37\x61": "gif",
        b"\x47\x49\x46\x38\x39\x61": "gif",
        b"\x42\x4D": "bmp",
        b"\x49\x49\x2A\x00\x10\x00\x00\x00\x43\x52\x02\x00\x06\x00\x00\x00": "cr2",
        b"\x49\x20\x49": "tif",
        b"\x49\x49\xBC\x01": "orf",
        b"\x00\x00\x01\x00": "ico",
        b"\x00\x01\x00\x00": "ico",
        b"\x46\x4F\x52\x4D\x00": "mov",
        b"\x66\x74\x79\x70\x4D\x53\x4E\x56": "mp4",
        # b"\x52\x49\x46\x46\x??\x??\x??\x??\x57\x45\x42\x50": "webp",
        b"\x1A\x45\xDF\xA3": "webm",
        b"\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C": "asf",
        b"\x80\x75\x67\x70\x35\x61": "heic",
        b"\x30\x31\x4F\x52": "orf",
        b"\x52\x49\x46\x46\x3C\xD3\x9C\x00\x57\x41\x56\x45": "wav",
        b"\x52\x49\x46\x46\x54\x57\x44\x41\x57\x41\x56\x45": "wav",
    }

    with open(file_path, 'rb') as f:
        data = f.read()
        for signature, ext in signature_mapping.items():
            if signature in data:
                # print(f"Found {ext} signature in {file_path}")
                return ext
    return None


def carve_by_metadata(file_path):
    # In this code, magic library is used to determine the MIME type of a file. MIME types are a way of identifying files based on their content, rather than relying solely on their extension or file name. The mime parameter in magic.Magic() constructor is set to True which tells the magic library to only return the MIME type of the file, rather than a full textual description. This can be useful when trying to identify the type of a file, especially when the file extension has been changed or is missing. By using magic library, the carve_by_metadata() function is able to identify video files by their MIME type and return the corresponding file extension, which can be used to identify and carve the file.
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    if "video" in file_type:
        # print(f"Found video metadata in {file_path}")
        return "mp4"
    return None



def carve_by_content(file_path):
    # Initialize key frame detection parameters
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 50
    params.maxThreshold = 200
    params.filterByArea = True
    params.minArea = 200
    params.filterByCircularity = False
    params.filterByConvexity = False
    params.filterByInertia = False
    params.minDistBetweenBlobs = 50
    detector = cv2.SimpleBlobDetector_create(params)

    # Open input video file
    cap = cv2.VideoCapture(file_path)

    # Loop over video frames and detect key frames
    count = 0
    while cap.isOpened():

        # Read next video frame
        ret, frame = cap.read()
        if not ret:
            break

        # Detect key points in frame
        keypoints = detector.detect(frame)

        # Check if frame contains key points
        if len(keypoints) > 0:
            print(f"Found key frame in {file_path} at frame {count}")

            # Write key frame to output file
            output_file = f"key_frame_{count}.jpg"
            cv2.imwrite(output_file, frame)
        count += 1
    cap.release()
    return None

# file_path = "CorruptedImage"
file_path = "Samples_Other_Formats_Sample-3g2"
# file_path = r"C:\Users\ramak\OneDrive\Desktop\Project\Stage-2\VideoSamples\Sample-1-HR.mp4"

# Flag variable
FileExtensionFound = 0
Possibilities=[]

print("Output by following Carving techniques on {file_path}:\n")
# Try to identify the file type using the filetype module
ftype = filetype.guess(file_path)
if ftype is not None:
    print("1. Carve by Filetype Module:")
    print(f"Found filetype {ftype.extension} \n")
    FileExtensionFound = 1
    Possibilities.append(ftype.extension)

# Try to identify the file type using file signature
cbs = carve_by_signature(file_path)
if cbs is not None:
    print("2. Carve Based on Signature:")
    print(f"Found filetype {cbs} \n")
    FileExtensionFound = 1
    Possibilities.append(cbs)

# Try to identify the file type using Metadata
cmd = carve_by_metadata(file_path)
if cmd is not None:
    print("3. Carve Based on Metadata:")
    print(f"Found filetype {cmd} \n")
    FileExtensionFound = 1
    Possibilities.append(cmd)

# Try to identify the file type using Content of file
cbc = carve_by_metadata(file_path)
if cbc is not None:
    print("4. Carve Based on File Content:")
    print(f"Found filetype {cbc} \n")
    FileExtensionFound = 1
    Possibilities.append(cbc)

if (FileExtensionFound==0):
    print(" File Extension NOT Found")
    exit(0)

# Method to find most frequently occuring item in list#Method to find most frequently occuring item in list
counter = Counter(Possibilities)
most_common = counter.most_common(1)[0][0]
print("Possibilities of filetype are:" , Possibilities)
print("Mostly it is a ", most_common)


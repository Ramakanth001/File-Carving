import ffmpeg
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.core import config
import numpy as np
import hashlib
import cv2
import magic
import sys
sys.path.append(r'C:\\Users\Suddala Kavyasree\Desktop\\File Carving\\Stage-1\\')
from UpdatedClassifiers import ftyp_classifier,stbl_classifier, edts_classifier, udta_classifier, free_classifier, mdat_classifier, moov_classifier, mvhd_classifier, trak_classifier, tkhd_classifier, mdia_classifier, mdhd_classifier, hdlr_classifier, minf_classifier, vmhd_classifier, smhd_classifier, dinf_classifier, dref_classifier, sample_atom_classifier, elst_classifier, iods_classifier


l = ['ftyp','edts', 'free', 'mdat', 'moov', 'mvhd', 'trak', 'tkhd', 'mdia', 'mdhd', 'hdlr', 'minf', 'smhd', 'vmhd', 'dinf', 'dref', 'url',
     'stbl', 'stsd', 'stts', 'stss', 'stsc', 'stsz', 'stco', 'ctts', 'sdtp', 'stps', 'cslg', 'udta', 'sgpd', 'sbgp', 'elst', 'iods']
major_brands_dict = {
    '3g2a': '3GPP2 multimedia file format version 2',
    '3g2b': '3GPP2 multimedia file format version 1',
    '3g2c': '3GPP2 multimedia file format version 3',
    '3ge6': '3GPP Release 6 extended-presentation multimedia file format',
    '3ge7': '3GPP Release 7 extended-presentation multimedia file format',
    '3gg6': '3GPP Release 6 general multimedia file format',
    '3gp1': '3GPP multimedia file format version 1',
    '3gp2': '3GPP multimedia file format version 2',
    '3gp3': '3GPP multimedia file format version 3',
    '3gp4': '3GPP multimedia file format version 4',
    '3gp5': '3GPP multimedia file format version 5',
    '3gp6': '3GPP multimedia file format version 6',
    '3gs7': '3GPP Release 7 streaming-server multimedia file format',
    'avc1': 'Advanced Video Coding file format',
    'da1a': 'Dirac (wavelet compression) file format version 1.0',
    'da1b': 'Dirac (wavelet compression) file format version 2.0',
    'dmb1': 'Digital multimedia broadcasting (DMB) file format',
    'drc1': 'Dirac (wavelet compression) file format version 2.2',
    'dv1a': 'Digital video file format version 1, revision 0',
    'dv1b': 'Digital video file format version 1, revision 1',
    'dv2a': 'Digital video file format version 2, revision 0',
    'dv2b': 'Digital video file format version 2, revision 1',
    'dv3a': 'Digital video file format version 3, revision 0',
    'dv3b': 'Digital video file format version 3, revision 1',
    'dvr1': 'Digital video recorder file format version 1',
    'dvt1': 'Digital video tape file format version 1',
    'F4V ': 'Adobe Flash Player or Adobe AIR file format',
    'H264': 'Advanced Video Coding file format',
    'H265': 'High Efficiency Video Coding file format',
    'm4s2': 'ISO/IEC 14496-1 MPEG-4 systems file format with AVC video',
    'm4v ': 'MPEG-4 video file format',
    'mj2s': 'Motion JPEG 2000 Part 2 video file format',
    'mjp2': 'Motion JPEG 2000 Part 2 video file format',
    'mp21': 'MPEG-21 file format',
    'mp41': 'MPEG-4 Part 14 file format version 1',
    'mp42': 'MPEG-4 Part 14 file format version 2',
    'mp71': 'MPEG-7 multimedia content description interface',
    'mp4v': 'MPEG-4 video file format',
    'msnv': 'MobiSaver video format',
    'mss1': 'MSS1 video file format',
    'mss2': 'MSS2 video file format',
    'mts1': 'AVCHD video file format',
    'mts2': 'AVCHD'}


def IsVideoFile_Based_On_AtomPresence(hex_string):
    # Evidence 1 4 11 19
    ascii_string = bytes.fromhex(hex_string).decode('ascii')
    isVideo = False
    for atom in l:
        if atom in ascii_string:
            isVideo = True
            break
    for ext in major_brands_dict:
        if ext in ascii_string:
            isVideo = True
    return isVideo

    # print(IsVideoFile_Based_On_AtomPresence('48656c6c6f20576f726c64'))

def IsVideoFile_Based_On_Ftyp(hex_string):
    # Evidence 2
    # Checks if it is a video file , after identifying ftyp atom
    ascii_string = bytes.fromhex(hex_string).decode('ascii')
    isVideo = False
    if 'ftyp' in ascii_string:
        ftyp_pos = ascii_string.find('ftyp')
        major_brand = ascii_string[ftyp_pos+4:ftyp_pos+8]
        if major_brand in major_brands_dict.keys():
            isVideo = True
        return isVideo
# print(IsVideoFile_Based_On_Ftyp('00000020667479706D703432000000006D703432'))

# Maintain a list of atoms, iterate over it and find the atoms which are present in the hex_string
def IsVideoFile_Based_On_Attributes(hex_string):
    # Evidence 3
    ll=[]
    ascii_string = bytes.fromhex(hex_string).decode('latin-1')
    for atom in l:
        if atom in ascii_string:
            ll.append(atom)
    for cur_atom in ll:
        atom_pos = ascii_string.find(str(cur_atom))
        if (cur_atom == 'stsd' or cur_atom == 'stsc' or cur_atom == 'stts' or cur_atom == 'stss'
                    or cur_atom == 'stsz' or cur_atom == 'stco' or cur_atom == 'ctts' or cur_atom == 'sdtp'
                    or cur_atom == 'stps' or cur_atom == 'cslg' or cur_atom == 'sgpd'or cur_atom == 'sbgp'):
            pointerr =  sample_atom_classifier(cur_atom,0,hex_string[(atom_pos*2)+8:], False)
        else:
            pointerr = eval(str(cur_atom)+'_classifier')(0,hex_string[(atom_pos*2)+8:], False)
        return pointerr

# print(IsVideoFile_Based_On_Attributes('00000020667479706D703432000000006D7034326D70343169736F6D61766331000033','ftyp'))
# print(IsVideoFile_Based_On_Attributes('0000337A6D6F6F760000006C6D76686400000000DBDE74B2DBDE74B2000002','moov'))

import pymp4parse

def IsVideoFile_Based_On_MagicSequence(filename):
    # Evidence 9 18
    with open(filename, 'rb') as f:
        # Read the first few bytes of the file
        header = f.read(32)

        # Check if the file starts with the magic bytes for a video file
        if header.startswith(b'\x00\x00\x00\x20ftyp'):
            return True  # This is a MP4 video file
        elif header.startswith(b'\x1a\x45\xdf\xa3'):
            return True  # This is a WebM video file
        elif header.startswith(b'\x52\x49\x46\x46') and header[8:12] in (b'\x41\x56\x49\x20', b'\x57\x41\x56\x45'):
            return True  # This is an AVI video file
        elif header.startswith(b'\x30\x26\xb2\x75'):
            return True  # This is an MPEG-2 video file
        elif header.startswith(b'\x00\x00\x01\x0b'):
            return True  # This is an MPEG-2 video stream file
        elif header.startswith(b'\x00\x00\x00\x18ftyp3gp') or header.startswith(b'\x00\x00\x00\x20ftyp3gp') or header.startswith(b'\x00\x00\x00\x18ftyp3g2') or header.startswith(b'\x00\x00\x00\x20ftyp3g2'):
            return True  # This is a 3GP/3G2 video file
        elif header.startswith(b'\x00\x00\x01\xba') or header.startswith(b'\x00\x00\x01\xb3') or header.startswith(b'\x00\x00\x01\xbd') or header.startswith(b'\x00\x00\x01\xb7'):
            return True  # This is an MPEG-2 program stream file
        elif header.startswith(b'\x00\x00\x01\xc0') or header.startswith(b'\x00\x00\x01\xe0'):
            return True  # This is an MPEG-1 video file
        elif header.startswith(b'\x1b\x54\x45\x58\x54\x53\x44\x20\x20\x20\x20\x20\x20\x20\x20\x20') or header.startswith(b'\x47\x4f\x4f\x44\x20\x44\x45\x53\x43\x52\x49\x50\x54\x49\x4f\x4e'):
            return True  # This is a QuickTime video file
        elif header.startswith(b'\x52\x49\x46\x46') and header[8:12] in (b'\x41\x56\x49\x20', b'\x57\x41\x56\x45') and header[12:16] == b'\x66\x6d\x74\x20':
            return True  # This is a WAV video file
        else:
            return False  # This is not a video file


# Example usage
# if IsVideoFile_Based_On_MagicSequence(r'C:\\Users\Suddala Kavyasree\Desktop\\File Carving\\VideoSamples\Sample-2-HR.mp4'):
#     print('This is a video file!')
# else:
#     print('This is not a video file.')


def IsVideoFile_Based_On_Frames(filename):
    # Evidence 8 23
    cap = cv2.VideoCapture(filename)
    if not cap.isOpened():
        return False
    while True:
        ret, frame = cap.read()
        if not ret:
            break
    cap.release()
    return True


def IsVideoFile_Based_On_BytesDistribution(filename):
    # Evidence 12
    #  you can use the magic library in Python. This library allows you to identify files based on their
    # contents using a database of file types and their corresponding byte patterns

    # Create a magic object and load the file type database
    mime = magic.Magic(mime=True)

    # Get the MIME type of the file
    file_type = mime.from_file(filename)

    # Check if the MIME type starts with 'video/'
    return file_type.startswith('video/')

 
def IsVideoFile_Based_On_Checksum(filename):
    # Evidence 10
    # Open the file in binary mode
    with open(filename, 'rb') as f:
        # Calculate the SHA256 hash of the file
        hash_object = hashlib.sha256()
        hash_object.update(f.read())
        file_hash = hash_object.hexdigest()

        # Compare the file hash to known video file hashes
        video_hashes = ['a1b2c3d4e5f6g7h8i9j0', 'k1l2m3n4o5p6q7r8s9t0', 'u1v2w3x4y5z6a7b8c9d0']
        if file_hash in video_hashes:
            return True

    return False

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

def IsVideoFile_Based_On_Dimensions(filename):
    # Evidence 5
    try:
        # Configure Hachoir to ignore file size limits
        config.max_size = None

        # Create a parser for the file
        parser = createParser(filename)

        # Extract metadata from the file
        metadata = extractMetadata(parser)

        # Check if the metadata contains video-related data
        video_metadata_keys = ['video_codec', 'video_width', 'video_height', 'frame_rate', 'duration']
        for key in video_metadata_keys:
            if metadata.has(key):
                return True

        # If no video metadata was found, return False
        return False

    except Exception as e:
        # Handle any exceptions that occur during metadata extraction
        print(f"Error while extracting metadata: {e}")
        return False


def IsVideoFile_Based_On_CompressionTechnique(file_path):
    # Evidence 21
    
    """In the above code, we define a function is_video_file that takes a file path as input and checks the
    file header for the presence of MPEG or H.264 codec signatures.
    We first open the file in binary mode and read the first 10 bytes of the file header. Then, we check
    if the header starts with the bytes \x00\x00\x01\xba or \x00\x00\x01\xb3, which are the signatures 
    for MPEG-1 and MPEG-2 codecs, respectively. If either of these signatures is found, we return True,
    indicating that the file is a video file.
    If the file header doesn't match the MPEG signatures, we check for the presence of H.264 codec 
    signature, which starts with \x00\x00\x00\x01\x67. If this signature is found, we return True, 
    indicating that the file is a video file.
    If none of these signatures are found, we return False, indicating that the file is not a video file."""
    
    """Check if the given file is a video file based on its header."""
    # Open the file in binary mode and read the first few bytes
    with open(file_path, 'rb') as f:
        header = f.read(10)
    
    # Check for the presence of MPEG or H.264 codec signatures in the header
    if header.startswith(b'\x00\x00\x01\xba') or header.startswith(b'\x00\x00\x01\xb3'):
        return True
    elif header.startswith(b'\x00\x00\x00\x01\x67'):
        return True
    else:
        return False
    


def IsVideoFile_Based_On_MotionVectors(file_path):
    # Evidence 17
    
    """In the above code, we define a function is_video_file that takes a file path as input and checks 
    if the file is a video file based on the presence of motion vectors and quantization tables.
    We first create a VideoCapture object using the given file path. If the file cannot be opened, 
    we return False to indicate that the file is not a video file.
    We then read the first frame of the video using the cap.read() method. If the read fails, we return
    False to indicate that the file is not a video file.
    Finally, we check if the video has motion vectors and quantization tables by computing the DCT 
    (discrete cosine transform) of the frame using the cv2.dct() method, and then computing the mean
    value of the DCT coefficients using the cv2.mean() method. If the mean value is 0, it indicates that
    the video does not have motion vectors and quantization tables, and we return False. Otherwise, 
    we return True to indicate that the file is a video file."""
    
    """Check if the given file is a video file based on motion vectors and quantization tables."""
    cap = cv2.VideoCapture(file_path)
    
    # Check if the file is a video file
    if not cap.isOpened():
        return False
    
    # Read the first frame of the video
    ret, frame = cap.read()
    if not ret:
        return False
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = frame.astype(np.float32)
    
    if len(frame.shape) > 2:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Check if the video has motion vectors and quantization tables
    if cv2.mean(cv2.dct(frame))[0] == 0:
        return False
    
    return True


def IsVideoFile_Based_On_Pixellation(file_path):
    # Evidence 24
    
    """In the above code, we define a function is_video_file that takes a file path as input and checks 
    if the file is a video file based on the presence of pixelation or blocking.
    We use the cv2.VideoCapture method from the opencv-python library to open the video file and
    read the first frame from the video. If the read is successful, we calculate the mean pixel value 
    and the standard deviation of the pixel values of the frame using the cv2.mean and cv2.meanStdDev
    methods, respectively.
    We then check if the standard deviation is low and the mean value is high, which are both indicative
    of pixelation or blocking. If this condition is true, we return True to indicate that the file is a
    video file with pixelation or blocking. Otherwise, we return False to indicate that the file is not
    a video file with pixelation or blocking."""
    
    """Check if the given file is a video file based on the presence of pixelation or blocking."""
    # Open the video file using OpenCV
    cap = cv2.VideoCapture(file_path)
    
    # Read the first frame from the video
    ret, frame = cap.read()
    
    # If the read is successful, check for pixelation or blocking
    if ret:
        # Calculate the mean pixel value of the frame
        mean_value = cv2.mean(frame)[0]
        
        # Calculate the standard deviation of the pixel values of the frame
        stddev_value = cv2.meanStdDev(frame)[1][0][0]
        print(mean_value,stddev_value)
        # If the standard deviation is low and the mean value is high, the video may have pixelation or blocking
        if stddev_value < 10 and mean_value > 200:
            return True
        
    return False

import cv2

def IsVideoFile_Based_On_TemporalSequence(filename):
    # Evidence 20
    try:
        video = cv2.VideoCapture(filename)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)
        if frame_count > 0 and width > 0 and height > 0 and fps > 0:
            return True
        else:
            return False
    except:
        return False




def StructuralEvidenceBasedVideoVerification():
    hex_string='00000020667479706D703432000000006D7034326D70343169736F6D61766331000033'
    filename=r"C:\\Users\Suddala Kavyasree\Desktop\\File Carving\\VideoSamples\Sample-2-HR.mp4"
    
    print('Based_On_AtomPresence: ',IsVideoFile_Based_On_AtomPresence(hex_string),'\n') 
    print('Based_On_Ftyp: ',IsVideoFile_Based_On_Ftyp(hex_string),'\n')
    print('Based_On_Attributes: ',IsVideoFile_Based_On_Attributes(hex_string),'\n')
    print('Based_On_MagicSequence: ',IsVideoFile_Based_On_MagicSequence(filename),'\n')
    print('Based_On_Frames: ',IsVideoFile_Based_On_Frames(filename),'\n')
    print('Based_On_BytesDistribution: ',IsVideoFile_Based_On_BytesDistribution(filename),'\n')
    print('Based_On_Checksum: ',IsVideoFile_Based_On_Checksum(filename),'\n')
    print('Based_On_Dimensions: ',IsVideoFile_Based_On_Dimensions(filename),'\n')
    print('Based_On_CompressionTechnique: ',IsVideoFile_Based_On_CompressionTechnique(filename),'\n')
    print('Based_On_MotionVectors: ',IsVideoFile_Based_On_MotionVectors(filename),'\n')
    print('Based_On_Pixellation: ',IsVideoFile_Based_On_Pixellation(filename),'\n')
    print(IsVideoFile_Based_On_TemporalSequence(filename))
    
StructuralEvidenceBasedVideoVerification()   




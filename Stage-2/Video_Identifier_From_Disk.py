# This code reads data from a binary file ("disk_fragment.bin") in blocks of size "block_size", starting from the offset
# "offset". It then searches for the file signature "signature" (which is the hexadecimal representation of the MP4 file
# signature) in each block of data. If the file signature is found in a block of data, it extracts the data starting from
# the offset of the file signature and writes it to an output file named "output.mp4" in append mode. This code can be
# used to recover a fragmented MP4 video file from disk fragments by searching for the MP4 file signature in each disk
# fragment and extracting the relevant data.

import binascii
signature = "0000001866747970" # MP4 file signature
block_size = 4096 # size of disk fragments to search
offset = 0 # starting offset of search
output_file = "output.mp4" # name of output file

with open("disk_fragment.bin", "rb") as f:
    while True:
        f.seek(offset)
        block_data = f.read(block_size)
        if not block_data:
            break
        offset += len(block_data)

        # search for file signature in block
        signature_offset = block_data.find(binascii.unhexlify(signature))
        if signature_offset >= 0:
            # file signature found, extract data
            file_data = block_data[signature_offset:]
            with open(output_file, "ab") as out:
                out.write(file_data)
import binascii
#Loading video file contents into 'data'
with open('Samples/Sample-5.mp4','rb') as f:
  data  = str(binascii.hexlify(f.read()))[2:-1]
# with open('zi.txt') as f:
#     for line in f:
#         print(line.strip())
import binascii
#Loading video file contents into 'data'
with open('sample.mp4','rb') as f:
  data  = str(binascii.hexlify(f.read()))[2:-1]
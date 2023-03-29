import binascii
#Loading video file contents into 'data'
with open('VideoSamples/sample-2.mp4','rb') as f:
  data  = str(binascii.hexlify(f.read()))[2:-1]
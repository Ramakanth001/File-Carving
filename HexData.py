import binascii
#Loading video file contents into 'data'
with open('Samples/Sample-1-HR.mp4','rb') as f:
  data  = str(binascii.hexlify(f.read()))[2:-1]
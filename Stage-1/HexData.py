import binascii

with open('VideoSamples/Sample-2-HR.mp4','rb') as f:
  data  = str(binascii.hexlify(f.read()))[2:-1]

# with open('Stage-3\RedundancyPartialFileSamples\CorruptedPartialFile1.txt','r') as f:
#   data=str((f.read()))
  
  
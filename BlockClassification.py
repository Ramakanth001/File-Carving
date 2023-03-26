# Block type identification
from SupportFunctions import litEnd,bigEnd,hex_to_ascii
import codecs
import binascii

myf = open('OutputSamples/output.txt', 'w')
myf.write("FILE CONTENT:\n")


with open('VideoSamples/sample3.mp4','rb') as f:
  data  = str(binascii.hexlify(f.read()))[2:-1]

block_count=0
file_size=0
block_size_H=[]
block_size_D=[]
block_type=[]
block_sub_type=[]
cur_size=0

temp=""
hex_pointer=0

def initial_chunk():
    initial_size = data[:8]
    block_size_H.append(initial_size)
    initial_size_dec = litEnd(initial_size)
    block_size_D.append(initial_size_dec)
    print(initial_size, "   |  ", initial_size_dec)
    block_count += 1
    
try:
  while(data[hex_pointer]!=''):
        temp_size=""
        temp_type=""
        temp_sub_type=""

        for i in range(hex_pointer,hex_pointer+8):
          temp_size+=data[i] 
        print("BLOCK :",block_count+1)
        print("current size chunk is ",temp_size)
        cur_block_size = temp_size
        block_size_H.append(cur_block_size)
        cur_block_size_dec = bigEnd(temp_size)
        block_size_D.append(cur_block_size_dec)
        cur_size+=cur_block_size_dec

        print("Block size is :", cur_block_size_dec)
        

        for j in range(hex_pointer+8,hex_pointer+16):
          temp_type+=data[j]
        cur_type=hex_to_ascii(temp_type)
        block_type.append(cur_type)
        print("current type is ",cur_type)



        if(cur_type=="ftyp"):
          for k in range(hex_pointer+16,hex_pointer+24):
            temp_sub_type+=data[k]
          cur_sub_type=hex_to_ascii(temp_sub_type)
          block_sub_type.append(cur_sub_type)
          print("current sub type is" , cur_sub_type)

        print("(updated size is :" , cur_size, ")\n")
        block_count+=1
        hex_pointer=cur_size*2
except:
  pass

file_size=cur_size
print("Reached end of file")

myf.write("\nBlock sizes in hex:\n")
for iter_var in range(len(block_size_H)):
  myf.write(block_size_H[iter_var]+"\n")

myf.write("\nBlock sizes in Decimal:\n")
for iter_var in range(len(block_size_D)):
  myf.write(str(block_size_D[iter_var])+"\n")

myf.write("\nBlock types :\n")
for iter_var in range(len(block_type)):
  myf.write(block_type[iter_var]+"\n")

myf.write("\nBlock Sub-types :\n")
for iter_var in range(len(block_sub_type)):
  myf.write(block_sub_type[iter_var]+"\n")

myf.write("\nSize of the file is : " + str(file_size) + "bytes")
myf.write("\nNumber of blocks in video :" + str(block_count) + "blocks")

# file_size=cur_size
# print("Reached end of file")

# print("\nBlock sizes in hex:")
# for iter_var in range(len(block_size_H)):
#   print(block_size_H[iter_var])

# print("\nBlock sizes in Decimal:")
# # print(block_size_D)
# for iter_var in range(len(block_size_D)):
#   print(block_size_D[iter_var])

# print("\nBlock types :")
# for iter_var in range(len(block_type)):
#   print(block_type[iter_var])

# print("\nBlock Sub-types :")
# for iter_var in range(len(block_sub_type)):
#   print(block_sub_type[iter_var])

print("\nSize of the file is : " , file_size , "bytes")
print("Number of blocks in video :" , block_count , "blocks")
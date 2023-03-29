from SupportFunctions import litEnd, bigEnd, hex_to_ascii, dprint
from HexData import data

# In FPRINT call DPRINT and write that into file so that data is in the foprm of dictionary in files
myf = open('OutputSamples/output.txt', 'w')
myf.write("FILE CONTENT:\n")
# myf.write(my_file_data)

def atom_seeker(pointer):
    # IMPORTANT CODE PART : (incase we need to work on atoms as per which ever is occuring next as per hex file)
    # SEEKING TILL WE FIND A PARTICULAR ATOM
    # Change conventions of cur_pointer and moov_pointer
    print(data[cur_pointer+1])
    tempo = ""
    temp = ""
    while (temp != "minf"):
        temp = ""
        tempo = ""
        for k in range(cur_pointer, cur_pointer+8):
            tempo += data[k]
        print(tempo)
        try:
            temp = hex_to_ascii(tempo)
            print(temp)
        except:
            pass
        cur_pointer += 1
    print(temp)
    moov_pointer = cur_pointer-1
    # points to 'minf' type starting we need to take it
    # back to 4 bytes to get its size
    moov_pointer -= 8
    for i in range(0, 8):
        print(data[moov_pointer+i])
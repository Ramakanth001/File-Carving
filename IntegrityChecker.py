import SupportFunctions
from HexData import data
def integrity_checker(pointer):
      tempo=""
      moov_pointer=pointer
      for i in range(moov_pointer,moov_pointer+8):
          tempo+=data[i]
      temp_size=SupportFunctions.bigEnd(tempo)
      print()
      print("Next atom size is ", temp_size)
      tempo=""
      for i in range(moov_pointer+8,moov_pointer+16):
           tempo+=data[i]
      temp_atom=SupportFunctions.hex_to_ascii(tempo)
      print("Next atom is ",temp_atom,'\n') 
      return temp_size, temp_atom
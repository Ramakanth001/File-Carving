import codecs
def litEnd(myInp):
    vals = {str(itr):itr for itr in range(10)}
    # vals['a','b','c','d','e','f'] = {10,11,12,13,14,15}
    vals['a'] = 10
    vals['b'] = 11
    vals['c'] = 12
    vals['d'] = 13
    vals['e'] = 14
    vals['f'] = 15
    try:
      return 16*vals[myInp[0]]+vals[myInp[1]]
    except:
      print(myInp)
      return 0

def bigEnd(myInp):
  return int(myInp, 16)

def hex_to_ascii(myInp):
    hex_decode  = codecs.decode(myInp, 'hex').decode("ASCII")
    myOp    = hex_decode.replace(';', '\n- ')
    return myOp

def dprint(my_dict):
  for attribute,value in my_dict.items():
    print("\'",attribute,"\' : ",value,sep="")

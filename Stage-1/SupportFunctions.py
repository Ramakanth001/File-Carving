import codecs



def litEnd(myInp):
    vals = {str(itr): itr for itr in range(10)}
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
    hex_decode = codecs.decode(myInp, 'hex').decode("ASCII")
    myOp = hex_decode.replace(';', '\n- ')
    return myOp


def dprint(my_dict):
    for attribute, value in my_dict.items():
        try:
            print("\'", attribute, "\' : ", value[:1050], sep="")
        except:
            print("\'", attribute, "\' : ", value, sep="")


def test(n,data):
    for i in range(n):
        print(data[i], end="")


def atom_seeker(pointer,data):
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
        
import datetime

def convert_hex_to_datetime(hex_value):
    if hex_value=='00000000':
        return '00000000'
    if '?' in hex_value or '_' in hex_value:
        return ''
    try:
        int_value = int(hex_value, 16)
        seconds_since_1904 = int_value - 2082844800
        # print(datetime.datetime.fromtimestamp(seconds_since_1904))
        return str(datetime.datetime.fromtimestamp(seconds_since_1904))
    except:
        return ''


def convert_string_to_hex(datetime_str):
        if len(datetime_str)==0:
            return '0'
        dt_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        # Convert datetime object to timestamp
        timestamp = int(dt_obj.timestamp())
        # Convert timestamp to number of seconds since midnight, January 1, 1904
        seconds_since_1904 = timestamp + 2082844800
        # Convert to 32-bit integer in hex format
        hex_str = hex(seconds_since_1904)[2:].zfill(8)
        return hex_str.upper()



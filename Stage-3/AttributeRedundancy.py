
import datetime
import sys
sys.path.append(r'C:\\Users\Suddala Kavyasree\Desktop\\File Carving\\Stage-1\\')
import AtomClassification
creation,modif,matrix=AtomClassification.MainAtomClassification()
Final_Creation_Time=''
Final_Modification_Time=''
Final_Matrix=''

def is_timestamp(datetime_str):
    try:
        datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False
    
def is_datetime_less_than_current(datetime_var):
    current_datetime = datetime.datetime.now()
    return datetime.datetime.strptime(datetime_var, '%Y-%m-%d %H:%M:%S') <= current_datetime

def is_datetime_greater_than_StandardTime(datetime_var):
    time_1904 = datetime.datetime(1904, 1, 1)
    return datetime.datetime.strptime(datetime_var, '%Y-%m-%d %H:%M:%S') >= time_1904

def is_creationTime_less_than_modificationTime(c,m):
    return datetime.datetime.strptime(c, '%Y-%m-%d %H:%M:%S')<=datetime.datetime.strptime(m, '%Y-%m-%d %H:%M:%S')

def is_valid_timestamp(datetime_str):
    try:
        dt =datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        if dt.timestamp() >= 0 and any(datetime_str.strip('0')):
            return True
        else:
            return False
    except ValueError:
        return False
    
# 1.Validation checks (timestamp verification-format,future date,expired date wrt epoch,non-negative,modif>=creation)
# 2.Attribute value finalization based on frequency of valid values
def FrequencyBasedAttributeRedundancy(original_dict,name):
    value_freq = {}
    for key, value in original_dict.items():
        if value not in value_freq:
            value_freq[value] = 1
        else:
            value_freq[value] += 1
    if name=='Creation_Time':
        d=value_freq.copy()
        for k,v in d.items():
            if is_timestamp(k) and is_datetime_less_than_current(k) and is_datetime_greater_than_StandardTime(k) and is_creationTime_less_than_modificationTime(k,Final_Modification_Time) and is_valid_timestamp(k):
                pass
            else:
                print("\n"+name+": "+k+" is invalid!!!!\n")
                value_freq.pop(k)
    elif name=='Modification_Time':
        d=value_freq.copy()
        for k,v in d.items():
            if is_timestamp(k) and is_datetime_less_than_current(k) and is_datetime_greater_than_StandardTime(k) and is_valid_timestamp(k):
                pass
            else:
                print("\n"+name+": "+k+" is invalid!!!!\n")
                value_freq.pop(k)
    most_common_value = max(value_freq, key=value_freq.get)
    return most_common_value
# if all are corrupted values, give the datetime.now()
        
def atom_seeker(data,pointer,atom):
    cur_pointer=pointer
    tempo = ""
    temp = ""
    while (temp != atom):
        temp = ""
        tempo = ""
        for k in range(cur_pointer, cur_pointer+8):
            tempo += data[k]
        try:
            temp = AtomClassification.hex_to_ascii(tempo)
        except:
            pass
        cur_pointer += 1
    moov_pointer = cur_pointer-1
    moov_pointer -= 8
    return moov_pointer

# 1.missing values in the file denoted by _ or ?
# 2.missing values in file based on corruption - modification or deletion
    # 2-a. Inclusion of attribute value in its rightful position(deletion)
    # 2-b. Overwriting of attribute values in partial file(modification)
# Note: Occurence of 2-b case might suggest that it is the reason for failure of validation checks  
        
def Reconstruction(creation,modif,matrix):
    #Sample-2-HR fragment is considered from ftyp to dinf
    # MVHD corruption is induced
    # Atoms effected are mvhd,tkhd and mdhd for creation time and modification time 
    # Atoms effetcted are mvhd and tkhd for matrix  
    f2=open('Stage-3\RedundancyPartialFileSamples\FixedPartialFile.txt','w')
    with open('Stage-3\RedundancyPartialFileSamples\CorruptedPartialFile1.txt', "r") as f1:
         data=str((f1.read()))
         mvhd_position=atom_seeker(data,0,'mvhd')
         tkhd_position=atom_seeker(data,0,'tkhd')
         mdhd_position=atom_seeker(data,0,'mdhd')
         pointer=0
         while(pointer<len(data)):
            if pointer!=mvhd_position and pointer!=tkhd_position and pointer!=mdhd_position: 
                f2.write(data[pointer])
                pointer+=1
            if pointer==mvhd_position:
                f2.write(data[pointer:pointer+24])
                pointer=pointer+24
                curr_creation=AtomClassification.convert_hex_to_datetime(data[pointer:pointer+8])
                curr_modifi=AtomClassification.convert_hex_to_datetime(data[pointer+8:pointer+16])
                final_creation=AtomClassification.convert_string_to_hex(creation)
                final_modif=AtomClassification.convert_string_to_hex(modif)
                if curr_modifi!=curr_creation and curr_modifi!=final_creation and curr_modifi!=final_modif:
                    # if modification time is deleted and other attribute value is read in its place
                    f2.write(final_creation)
                    f2.write(final_modif)
                    pointer=pointer+8
                else:
                    if curr_creation != final_creation or '_' in curr_creation or '?' in curr_creation:
                        f2.write(final_creation)
                    else:
                        f2.write(curr_creation)
                    if curr_modifi!=final_modif or '-' in curr_modifi or '?' in curr_modifi:
                        f2.write(final_modif)
                    else:
                        f2.write(curr_modifi)
                    pointer=pointer+16
                f2.write(data[pointer:pointer+48])
                pointer=pointer+48
                f2.write(matrix)
                pointer=pointer+72
                f2.write(data[pointer:pointer+56])
                pointer=pointer+56
            if pointer==tkhd_position:
                f2.write(data[pointer:pointer+24])
                pointer=pointer+24
                curr_creation=AtomClassification.convert_hex_to_datetime(data[pointer:pointer+8])
                curr_modifi=AtomClassification.convert_hex_to_datetime(data[pointer+8:pointer+16])
                final_creation=AtomClassification.convert_string_to_hex(creation)
                final_modif=AtomClassification.convert_string_to_hex(modif)
                if curr_modifi!=curr_creation and curr_modifi!=final_creation and curr_modifi!=final_modif:
                    # if modification time is deleted and other attribute value is read in its place
                    f2.write(final_creation)
                    f2.write(final_modif)
                    pointer=pointer+8
                else:
                    if curr_creation != final_creation or '_' in curr_creation or '?' in curr_creation:
                        f2.write(final_creation)
                    else:
                        f2.write(curr_creation)
                    if curr_modifi!=final_modif or '-' in curr_modifi or '?' in curr_modifi:
                        f2.write(final_modif)
                    else:
                        f2.write(curr_modifi)
                    pointer=pointer+16
                f2.write(data[pointer:pointer+56])
                pointer=pointer+56
                f2.write(matrix)
                pointer=pointer+72
                f2.write(data[pointer:pointer+16])
                pointer=pointer+16
            if pointer==mdhd_position:
                f2.write(data[pointer:pointer+24])
                pointer=pointer+24
                curr_creation=AtomClassification.convert_hex_to_datetime(data[pointer:pointer+8])
                curr_modifi=AtomClassification.convert_hex_to_datetime(data[pointer+8:pointer+16])
                final_creation=AtomClassification.convert_string_to_hex(creation)
                final_modif=AtomClassification.convert_string_to_hex(modif)
                if curr_modifi!=curr_creation and curr_modifi!=final_creation and curr_modifi!=final_modif:
                    # if modification time is deleted and other attribute value is read in its place
                    f2.write(final_creation)
                    f2.write(final_modif)
                    pointer=pointer+8
                else:
                    if curr_creation != final_creation or '_' in curr_creation or '?' in curr_creation:
                        f2.write(final_creation)
                    else:
                        f2.write(curr_creation)
                    if curr_modifi!=final_modif or '-' in curr_modifi or '?' in curr_modifi:
                        f2.write(final_modif)
                    else:
                        f2.write(curr_modifi)
                    pointer=pointer+16
                f2.write(data[pointer:pointer+24])
                pointer=pointer+24                          
    
Final_Modification_Time=FrequencyBasedAttributeRedundancy(modif,'Modification_Time')
Final_Creation_Time=  FrequencyBasedAttributeRedundancy(creation,'Creation_Time')
Final_Matrix=FrequencyBasedAttributeRedundancy(matrix,'Matrix')
print("\nFinal Values of Redundant Attributes based on Frequency:")
print('\nFinal Creation Time:----------------------\n')
print(Final_Creation_Time)
print('\nFinal Modification Time:----------------------\n')
print(Final_Modification_Time)
print('\nFinal Matrix Value:----------------------\n')
print(Final_Matrix)
print()

Reconstruction(creation=Final_Creation_Time,modif=Final_Modification_Time,matrix=Final_Matrix)


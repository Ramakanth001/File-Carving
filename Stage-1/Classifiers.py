from SupportFunctions import bigEnd, hex_to_ascii, dprint, convert_hex_to_datetime
from AtomDictionaries import ftyp, free, mdat, moov, mvhd, trak, tkhd, mdia, mdhd, hdlr, minf, smhd, vmhd, dinf, dref, url, stbl, stsd, stts, stss, stsc, stsz, stco, ctts, sdtp, stps, cslg, udta, sgpd, sbgp, elst, iods
Creation_Time={}
Modification_Time={}
Matrix={}
def ftyp_classifier(pointer, size,data):
    tempo = ""
    for i in range(pointer, pointer+8):
        tempo += data[i]
    ftyp['Size'] = bigEnd(tempo)
    tempo = ""
    for i in range(pointer+16, pointer+24):
        tempo += data[i]
    ftyp['Major_Brand'] = hex_to_ascii(tempo)
    tempo = ""
    for i in range(pointer+24, pointer+32):
        tempo += data[i]
    ftyp['Minor_Version'] = (tempo)
    pointer += 32
    count = (size*2-32)/4
    count = int(count/2)
    tempo = ""
    c_brand = []
    for j in range(0, count):
        c_brand.append(hex_to_ascii(data[pointer:pointer+8]))
        pointer += 8
    ftyp['Compatible_Brands'] += c_brand
    return pointer

def free_classifier(pointer,size,data):
    tempo = ""
    for i in range(pointer, pointer+8):
        tempo += data[i]
    free['Size'] = bigEnd(tempo)
    pointer += 16
    return pointer


def mdat_classifier(pointer,size,data):
    tempo = ""
    for i in range(pointer, pointer+8):
        tempo += data[i]
    mdat['Size'] = bigEnd(tempo)
    pointer += mdat['Size']*2
    return pointer


def moov_classifier(pointer,size,data):
    tempo=""
    for i in range(pointer, pointer+8):
        tempo += data[i]
    moov['Size'] =bigEnd(tempo)
    pointer += moov['Size']*2
    return pointer


def mvhd_classifier(pointerr, size,data):
    pointer=pointerr
    pointer=pointer+16
    mvhd['Size'] = size
    tempo = ""
    for j in range(pointer, pointer+2):
        tempo += data[j]
    mvhd['Version'] = tempo
    tempo = ""
    pointer=pointer+2
    for j in range(pointer, pointer+6):
        tempo += data[j]
    mvhd['Flags'] = tempo
    pointer=pointer+6
    tempo = ""
    for j in range(pointer, pointer+8):
        tempo += data[j]
    tempo2=tempo
    mvhd['Creation_Time'] = convert_hex_to_datetime(tempo)
    Creation_Time['mvhd']=convert_hex_to_datetime(tempo)
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    pointer=pointer+8
    if tempo2!=tempo:        
        mvhd['Modification_Time'] = convert_hex_to_datetime(tempo2)
        Modification_Time['mvhd']=convert_hex_to_datetime(tempo2)
        mvhd['Time_Scale'] = tempo
        tempo = ""
    else:
        mvhd['Modification_Time'] = convert_hex_to_datetime(tempo)
        Modification_Time['mvhd']=convert_hex_to_datetime(tempo)
        tempo = ""    
        for j in range(pointer, pointer+8):
            tempo += data[j]
        mvhd['Time_Scale'] = tempo
        tempo = ""
        pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Duration'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Preferred_Rate'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+4):
        tempo += data[j]
    mvhd['Preferred_Volume'] = tempo
    tempo = ""
    pointer=pointer+4
    for j in range(pointer, pointer+20):
        tempo += data[j]
    mvhd['Reserved'] = tempo
    tempo = ""
    pointer=pointer+20
    for j in range(pointer, pointer+72):
        tempo += data[j]
    mvhd['Matrix'] = tempo
    Matrix['mvhd']=tempo
    tempo = ""
    pointer=pointer+72
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Preview_Time'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Preview_Duration'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Poster_Time'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Selection_Time'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Selection_Duration'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Current_Time'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mvhd['Next_Track_ID'] = tempo
    pointer = pointer+8
    # updating the moov pointer to the seeked position after parsing the attributes
    return pointer

def trak_classifier(pointer,size,data):   
    tempo = ""
    for i in range(pointer, pointer+8):
        tempo += data[i]
    trak['Size'] = bigEnd(tempo)
    pointer += 16
    return pointer

def tkhd_classifier(pointerr, size,data):
    pointer=pointerr
    pointer=pointer+16
    tkhd['Size'] = size
    tempo = ""
    for j in range(pointer, pointer+2):
        tempo += data[j]
    tkhd['Version'] = tempo
    tempo = ""
    pointer=pointer+2
    for j in range(pointer, pointer+6):
        tempo += data[j]
    tkhd['Flags'] = tempo
    pointer=pointer+6
    tempo = ""
    for j in range(pointer, pointer+8):
        tempo += data[j]
    tempo2=tempo
    tkhd['Creation_Time'] = convert_hex_to_datetime(tempo)
    Creation_Time['tkhd']=convert_hex_to_datetime(tempo)
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    pointer=pointer+8
    if tempo2!=tempo:        
        tkhd['Modification_Time'] = convert_hex_to_datetime(tempo2)
        Modification_Time['tkhd']=convert_hex_to_datetime(tempo2)
        tkhd['Track_ID'] = tempo
        tempo = ""
    else:
        tkhd['Modification_Time'] = convert_hex_to_datetime(tempo)
        Modification_Time['tkhd']=convert_hex_to_datetime(tempo)
        tempo = ""    
        for j in range(pointer, pointer+8):
            tempo += data[j]
        tkhd['Track_ID'] = tempo
        tempo = ""
        pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    tkhd['Reserved'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    tkhd['Duration'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+16):
        tempo += data[j]
    tkhd['Reserved_2'] = tempo
    tempo = ""
    pointer=pointer+16
    for j in range(pointer, pointer+4):
        tempo += data[j]
    tkhd['Layer'] = tempo
    tempo = ""
    pointer=pointer+4
    for j in range(pointer, pointer+4):
        tempo += data[j]
    tkhd['Alternative_Group'] = tempo
    tempo = ""
    pointer=pointer+4
    for j in range(pointer, pointer+4):
        tempo += data[j]
    tkhd['Volume'] = tempo
    tempo = ""
    pointer=pointer+4
    for j in range(pointer, pointer+4):
        tempo += data[j]
    tkhd['Reserved_3'] = tempo
    tempo = ""
    pointer=pointer+4
    for j in range(pointer, pointer+72):
        tempo += data[j]
    tkhd['Matrix_Structure'] = tempo
    Matrix['tkhd']=tempo
    tempo = ""
    pointer=pointer+72
    for j in range(pointer, pointer+8):
        tempo += data[j]
    tkhd['Track_Width'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    tkhd['Track_Height'] = tempo
    pointer += 8
    return pointer

def mdia_classifier(pointer,size,data):
    tempo = ""
    for i in range(pointer, pointer+8):
        tempo += data[i]
    mdia['Size'] = bigEnd(tempo)
    pointer += 16
    return pointer


def mdhd_classifier(pointerr, size,data):
    pointer=pointerr
    pointer=pointer+16
    mdhd['Size'] = size
    tempo = ""
    for j in range(pointer, pointer+2):
        tempo += data[j]
    mdhd['Version'] = tempo
    tempo = ""
    pointer=pointer+2
    for j in range(pointer, pointer+6):
        tempo += data[j]
    mdhd['Flags'] = tempo
    pointer=pointer+6
    tempo = ""
    for j in range(pointer, pointer+8):
        tempo += data[j]
    tempo2=tempo
    mdhd['Creation_Time'] = convert_hex_to_datetime(tempo)
    Creation_Time['mdhd']=convert_hex_to_datetime(tempo)
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    pointer=pointer+8
    if tempo2!=tempo:        
        mdhd['Modification_Time'] = convert_hex_to_datetime(tempo2)
        Modification_Time['mdhd']=convert_hex_to_datetime(tempo2)
        mdhd['Time_Scale'] = tempo
        tempo = ""
    else:
        mdhd['Modification_Time'] = convert_hex_to_datetime(tempo)
        Modification_Time['mdhd']=convert_hex_to_datetime(tempo)
        tempo = ""    
        for j in range(pointer, pointer+8):
            tempo += data[j]
        mdhd['Time_Scale'] = tempo
        tempo = ""
        pointer=pointer+8
    for j in range(pointer, pointer+8):
        tempo += data[j]
    mdhd['Duration'] = tempo
    tempo = ""
    pointer=pointer+8
    for j in range(pointer, pointer+4):
        tempo += data[j]
    mdhd['Language'] = tempo
    tempo = ""
    pointer=pointer+4
    for j in range(pointer, pointer+4):
        tempo += data[j]
    mdhd['Predefined'] = tempo
    pointer += 4
    return pointer

def hdlr_classifier(pointer, size,data):
    hdlr['Size'] = size
    pointer += 16
    tempo = ""
    for j in range(pointer, pointer+2):
        tempo += data[j]
    hdlr['Version'] = tempo
    tempo = ""
    for j in range(pointer+2, pointer+8):
        tempo += data[j]
    hdlr['Flags'] = tempo
    tempo = ""
    for j in range(pointer+8, pointer+16):
        tempo += data[j]
    hdlr['Component_Type'] = tempo
    tempo = ""
    for j in range(pointer+16, pointer+24):
        tempo += data[j]
    hdlr['Component_Subtype'] = hex_to_ascii(tempo)
    tempo = ""
    for j in range(pointer+24, pointer+32):
        tempo += data[j]
    hdlr['Component_Manufacturer'] = tempo
    tempo = ""
    for j in range(pointer+32, pointer+40):
        tempo += data[j]
    hdlr['Component_Flags'] = tempo
    tempo = ""
    for j in range(pointer+40, pointer+48):
        tempo += data[j]
    hdlr['Component_Flags_Masks'] = tempo
    flag_pointer = pointer+48
    # Strangely the below thing is working
    # moov_pointer+=(hdlr['Size']-16)*2
    pointer = pointer+(hdlr['Size']*2)

    # Now moov pointer is pointing to next atom this works because
    # we can find variable size of parameter by seeking to end of the atom
    tempo = ""
    for g in range(flag_pointer, pointer-16):
        tempo += data[g]
    try:
        hdlr['Component_Name'] = hex_to_ascii(tempo)
        return pointer-16
    except:
        hdlr['Component_Name'] = (tempo)
        return pointer-16


def minf_classifier(pointer,size,data):
    minf['Size'] = size
    pointer += size*2
    return pointer


def vmhd_classifier(pointer, size,data):
    vmhd['Size'] = size
    tempo = ""
    for j in range(pointer+16, pointer+18):
        tempo += data[j]
    vmhd['Version'] = tempo
    tempo = ""
    for j in range(pointer+18, pointer+24):
        tempo += data[j]
    vmhd['Flags'] = tempo
    tempo = ""
    for j in range(pointer+24, pointer+28):
        tempo += data[j]
        vmhd['Graphics_Mode'] = tempo
    tempo = ""
    for j in range(pointer+28, pointer+40):
        tempo += data[j]
    vmhd['Opcolor'] = tempo
    pointer += 40
    return pointer


def smhd_classifier(pointer, size,data):
    smhd['Size'] = size
    tempo = ""
    for j in range(pointer+16, pointer+18):
        tempo += data[j]
    smhd['Version'] = tempo
    tempo = ""
    for j in range(pointer+18, pointer+24):
        tempo += data[j]
    smhd['Flags'] = tempo
    tempo = ""
    for j in range(pointer+24, pointer+28):
        tempo += data[j]
    smhd['Balance'] = tempo
    tempo = ""
    for j in range(pointer+28, pointer+32):
        tempo += data[j]
    smhd['Reserved'] = tempo
    pointer += 32
    return pointer


def dinf_classifier(pointer, size,data):
    dinf['Size'] = size
    pointer += size*2
    return pointer


def dref_classifier(pointer, size,data):
    dref['Size'] = size
    tempo = ""
    for j in range(pointer+16, pointer+18):
        tempo += data[j]
    dref['Version'] = tempo
    tempo = ""
    for j in range(pointer+18, pointer+24):
        tempo += data[j]
    dref['Flags'] = tempo
    tempo = ""
    for j in range(pointer+24, pointer+32):
        tempo += data[j]
    dref['Number_of_Entries'] = bigEnd(tempo)
    entry_count = dref['Number_of_Entries']
    pointer += 32
    print("\n", "Data Reference Information (dref) Atom Details are:")
    dprint(dref)
    print("\nSince we have ", entry_count, "Number of entries we are going to have",
          entry_count, "number of data references like url atom etc")
    count = 0
    # Write url atoms individaually to files so that all occurances of data references in the form of url atoms can be stored since lastest url atom is kept at the directionary
    while (count < entry_count):
        # cur_atom="url"
        tempo = ""
        for j in range(pointer, pointer+8):
            tempo += data[j]
        url['Size'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        url['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        url['Flags'] = tempo
        pointer += 24
        count += 1
        print('\nurl'.upper()+" Atom Details are:-------------------------------------")
        dprint(url)
    return pointer

def sample_atom_classifier(atom, pointer, size,data):
    cur_size = size
    if (atom == 'stsd'):
        tempo = ""
        for j in range(pointer, pointer+8):
            tempo += data[j]
        stsd['Size'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stsd['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stsd['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stsd['Number_of_Entries'] = tempo
        tempo = ""
        for j in range(pointer+32, pointer+40):
            tempo += data[j]
        stsd['Sample_Description_Size'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+40, pointer+48):
            tempo += data[j]
        stsd['Data_Format'] = hex_to_ascii(tempo)
        tempo = ""
        for j in range(pointer+48, pointer+52):
            tempo += data[j]
        stsd['version'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+52, pointer+56):
            tempo += data[j]
        stsd['Revision_Level'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+56, pointer+64):
            tempo += data[j]
        stsd['Vendor'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+64, pointer+72):
            tempo += data[j]
        stsd['Temporal_Quality'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+72, pointer+80):
            tempo += data[j]
        stsd['Spatial_Quality'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+80, pointer+84):
            tempo += data[j]
        stsd['Media_Width'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+84, pointer+88):
            tempo += data[j]
        stsd['Media_Height'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+88, pointer+96):
            tempo += data[j]
        stsd['Horizontal_Resolution'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+96, pointer+104):
            tempo += data[j]
        stsd['Vertical_Resolution'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+104, pointer+112):
            tempo += data[j]
        stsd['DataSize'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+112, pointer+116):
            tempo += data[j]
        stsd['Frame_Count'] = bigEnd(tempo)
        tempo=""
        t1=""
        t1=t1+data[pointer+116]
        t1=t1+data[pointer+117]
        i=1
        while(t1!='00'):
            tempo=tempo+t1
            t1=""
            t1=t1+data[pointer+117+i]
            t1=t1+data[pointer+117+i+1]
            i=i+2
        stsd['compressorname']=hex_to_ascii(tempo)
        p=pointer+117+i
        tempo = ""
        for j in range(p, p+4):
            tempo += data[j]
        stsd['bits_per_sample'] = bigEnd(tempo)
        tempo = ""
        for j in range(p+4, p+8):
            tempo += data[j]
        stsd['channelcount'] = bigEnd(tempo)
        tempo = ""
        for j in range(p+8, p+12):
            tempo += data[j]
        stsd['samplesize'] = bigEnd(tempo)
        tempo = ""
        for j in range(p+12, p+20):
            tempo += data[j]
        stsd['samplerate'] = bigEnd(tempo)
        tempo = ""
        for j in range(p+20, pointer+(stsd['Size']*2)):
            tempo += data[j]
        stsd['format_specific_data'] =(tempo)
        return pointer+(stsd['Size']*2)
    if (atom == 'stsdd'):
        tempo = ""
        for j in range(pointer, pointer+8):
            tempo += data[j]
        stsd['Size'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stsd['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stsd['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stsd['Number_of_Entries'] = tempo
        tempo = ""
        for j in range(pointer+32, pointer+40):
            tempo += data[j]
        stsd['Sample_Description_Size'] = bigEnd(tempo)
        tempo = ""
        for j in range(pointer+40, pointer+48):
            tempo += data[j]
        stsd['Data_Format'] = hex_to_ascii(tempo)
        tempo = ""
        for j in range(pointer+48, pointer+60):
            tempo += data[j]
        stsd['Reserved1'] = (tempo)
        tempo = ""
        for j in range(pointer+60, pointer+68):
            tempo += data[j]
        stsd['Data_Reference_Index'] = (tempo)
        tempo = ""
        for j in range(pointer+68, pointer+80):
            tempo += data[j]
        stsd['Predefines'] = (tempo)
        tempo = ""
        for j in range(pointer+80, pointer+92):
            tempo += data[j]
        stsd['Reserved2'] = (tempo)
        # Predefines and Reserved are 6 bytes each(moovP:48)
        pointer += (stsd['Size']*2)
        # here sample description size is size of various format types present
        # in stsd atoms - in this atom 'mp4a'. Here we have only 1 entry i.e., stsd['Number_of_entries']
        # fo all those entries re-coumputation of constituent elements has to be done
        # print("\nSample Table Description(stsd) details:")
        # dprint(stsd)
        return pointer
    
    if (atom == 'stts'):
        stts['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stts['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stts['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stts['Number_of_Entries'] = tempo
        tempo = ""
        for j in range(pointer+32, pointer+40):
            tempo += data[j]
        stts['Sample_Duration'] = tempo
        tempo = ""
        for j in range(pointer+40, pointer+48):
            tempo += data[j]
        stts['Sample_Count'] = tempo
        # print("\nSample to Time-Table Samples(stts) details:")
        # dprint(stts)
        pointer += 48
        return pointer
        # we done with stts

    if (atom == 'stss'):
        stss['Size'] = cur_size
        tempo = ""
        cur_pointer = pointer
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stss['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stss['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stss['Number_of_Entries'] = tempo
        flag_pointer = pointer+32
        pointer = cur_pointer+(stss['Size']*2)
        # Now moov pointer is pointing to next atom this works because
        # we can find variable size of parameter by seeking to end of the atom
        tempo = ""
        for f in range(flag_pointer, pointer):
            tempo += data[f]
        stss['Sync-sample-table'] = tempo
        # print("\nSample to Sync Samples(stss) details:")
        # dprint(stss)
        # moov_pointer+=40
        return pointer
        # done with stss

    if (atom == 'stsc'):
        cur_pointer = pointer
        stsc['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stsc['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stsc['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stsc['Number_of_Entries'] = tempo
        flag_pointer = pointer+32
        pointer = cur_pointer+(stsc['Size']*2)
        # print("ziggaaaaa")
        # print(moov_pointer)
        # print(stsc['Size'])
        # Now moov pointer is pointing to next atom this works because
        # we can find variable size of parameter by seeking to end of the atom
        tempo = ""
        for f in range(flag_pointer, pointer):
            tempo += data[f]
        stsc['Sample-to-Chunk_Table'] = tempo
        # The next attribute is sample to chunk table whose size is variable in nature
        # In order to parse without knowing what its size is, we simply move the moov pointer to end of the atom
        # The un-parsed data must belong to the variable size attribute (from cur_pointer to moov_pointer)
        # tempo=""
        # for i in range(cur_pointer,moov_pointer):
        #   tempo+=data[i]
        # stsc['Sample-to-Chunk_Table'] = tempo
        # moov_pointer=moov_pointer+stsc['Size']

        # print("\nSample to sample chunk(stsc) atom details:")
        # dprint(stsc)
        return pointer
        # stsc atom complete

    if (atom == 'stsz'):
        cur_pointer = pointer
        stsz['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stsz['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stsz['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stsz['Sample_Size'] = tempo
        tempo = ""
        for j in range(pointer+32, pointer+40):
            tempo += data[j]
        stsz['Number_of_Entries'] = tempo
        flag_pointer = pointer+40
        pointer = cur_pointer+(stsz['Size']*2)
        tempo = ""
        for f in range(flag_pointer, pointer):
            tempo += data[f]
        stsz['Sample-to-Size_Table'] = tempo
        # print("\nSample to Size Table(stsz) atom details:")
        # dprint(stsz)
        return pointer
        # done with stsz atom

    if (atom == 'stco'):
        cur_pointer = pointer
        stco['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stco['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stco['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stco['Number_of_Entries'] = tempo
        flag_pointer = pointer+32
        pointer = cur_pointer+(stco['Size']*2)
        tempo = ""
        for f in range(flag_pointer, pointer):
            tempo += data[f]
        stco['Chunk_offset_table'] = tempo
        # print("\n Chunk offset (stco) atom  details:")
        # dprint(stco)
        return pointer
        # done with stco

    if (atom == 'ctts'):
        cur_pointer = pointer
        ctts['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        ctts['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        ctts['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        ctts['Entry-Count'] = tempo
        flag_pointer = pointer+32
        pointer = cur_pointer+(ctts['Size']*2)
        tempo = ""
        for f in range(flag_pointer, pointer):
            tempo += data[f]
        ctts['Composition-offset-table'] = tempo
        # print("\nComposition offset Table (ctts) details:")
        # dprint(ctts)
        return pointer

    if (atom == 'sdtp'):
        cur_pointer = pointer
        sdtp['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        sdtp['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        sdtp['Flags'] = tempo
        flag_pointer = pointer+24
        pointer = cur_pointer+(sdtp['Size']*2)
        tempo = ""
        for f in range(flag_pointer, pointer):
            tempo += data[f]
        sdtp['Sample-Dependency-Flags-Table'] = tempo
        # print("\n'Sample Dependency Flag Atom (sdtp) details:")
        # dprint(sdtp)
        return pointer
    
    if (atom == 'stps'):
        cur_pointer = pointer
        stps['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        stps['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        stps['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stps['Entry-Count'] = tempo
        flag_pointer = pointer+32
        pointer = cur_pointer+(ctts['Size']*2)
        tempo = ""
        for f in range(flag_pointer, pointer):
            tempo += data[f]
        stps['Partial-Sync-Sample-Table'] = tempo
        # print("\nPartial Sync Sample (stps) atom details:")
        # dprint(stps)
        return pointer
    
    if (atom == 'cslg'):
        cur_pointer = pointer
        cslg['Size'] = cur_size
        tempo = ""
        for j in range(pointer+16, pointer+18):
            tempo += data[j]
        cslg['Version'] = tempo
        tempo = ""
        for j in range(pointer+18, pointer+24):
            tempo += data[j]
        cslg['Flags'] = tempo
        tempo = ""
        for j in range(pointer+24, pointer+32):
            tempo += data[j]
        stps['CompositionOffsetToDisplayOffset'] = tempo
        tempo = ""
        for j in range(pointer+32, pointer+40):
            tempo += data[j]
        stps['LeastDisplayOffset'] = tempo
        tempo = ""
        for j in range(pointer+40, pointer+48):
            tempo += data[j]
        stps['DisplayStartTime'] = tempo
        tempo = ""
        for j in range(pointer+48, pointer+56):
            tempo += data[j]
        stps['DispalyEndTime'] = tempo
        # print("\ncomposition shift least greatest atom (cslg) atom details:")
        # dprint(cslg)
        return pointer
    
    if (atom == "sgpd"):
        # def sgpd_classifier(atom,pointer,size):
          cur_pointer=pointer
          sgpd['Size'] = size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          sgpd['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          sgpd['Flags'] = tempo
          tempo=""
        #   grouping type is always 'Roll'
          for j in range(pointer+32,pointer+40):
            tempo+=data[j]
          sgpd['DefaultLength'] = tempo
          tempo=""
          for j in range(pointer+40,pointer+48):
            tempo+=data[j]
          sgpd['EntryCount'] = tempo
          tempo=""
          flag_pointer = pointer+48
          pointer = cur_pointer+(sgpd['Size']*2)
          tempo = ""
          for f in range(flag_pointer, pointer):
             tempo += data[f]
          sgpd['PayloadData'] = tempo
          return pointer
    
    if (atom == "sbgp"):
          cur_pointer=pointer
          sbgp['Size'] = size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          sbgp['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          sbgp['Flags'] = tempo
          tempo=""
        #   grouping type is always 'Roll'
          for j in range(pointer+32,pointer+40):
            tempo+=data[j]
          sbgp['EntryCount'] = tempo
          flag_pointer = pointer+40
          pointer = cur_pointer+(sbgp['Size']*2)
          tempo = ""
          for f in range(flag_pointer, pointer):
             tempo += data[f]
          sbgp['TableData'] = tempo
          return pointer
    

def udta_classifier(atom,pointer,size,data):
          cur_pointer=pointer
          udta['Size'] = size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          udta['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          udta['Flags'] = tempo
          flag_pointer = pointer+24
          pointer=cur_pointer+(udta['Size']*2)
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          udta['UserDataList'] = tempo
          return pointer

def elst_classifier(atom,pointer,size,data):
        elst['Size'] = size
        tempo=""
        for j in range(pointer+16,pointer+18):
            tempo+=data[j]
        elst['Version'] = tempo
        tempo=""
        for j in range(pointer+18,pointer+24):
            tempo+=data[j]
        elst['Flags'] = tempo
        tempo=""
        for j in range(pointer+24,pointer+32):
            tempo+=data[j]
        elst['EntryCount'] = tempo
        tempo=""
        for j in range(pointer+32,pointer+40):
            tempo+=data[j]
        elst['EditDuration'] = tempo
        tempo=""
        for j in range(pointer+40,pointer+48):
            tempo+=data[j]
        elst['EditMediaTime'] = tempo
        tempo=""
        for j in range(pointer+48,pointer+56):
            tempo+=data[j]
        elst['PlaybackSpeed'] = tempo
        return pointer+56

def iods_classifier(atom,pointer,size,data):
        cur_pointer=pointer
        iods['Size'] = size
        tempo=""
        for j in range(pointer+16,pointer+18):
            tempo+=data[j]
        iods['Version'] = tempo
        tempo=""
        for j in range(pointer+18,pointer+24):
            tempo+=data[j]
        iods['Flags'] = tempo
        flag_pointer = pointer+24
        pointer=cur_pointer+(iods['Size']*2)
        tempo=""
        for f in range(flag_pointer,pointer):
          tempo+=data[f]
        iods['OtherData'] = tempo
        return pointer
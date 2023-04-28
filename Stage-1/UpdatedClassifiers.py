from SupportFunctions import bigEnd, hex_to_ascii, dprint, convert_hex_to_datetime
from AtomDictionaries import ftyp, stbl,free,edts, mdat, moov, mvhd, trak, tkhd, mdia, mdhd, hdlr, minf, smhd, vmhd, dinf, dref, url, stbl, stsd, stts, stss, stsc, stsz, stco, ctts, sdtp, stps, cslg, udta, sgpd, sbgp, elst, iods
Creation_Time={}
Modification_Time={}
Matrix={}
def ftyp_classifier(pointer,data,inclusion):
    tempo = ""
    pointerr=pointer
    if inclusion==True:
        if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
            ftyp['Size'] = bigEnd(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            (pointerr,ftyp)
        if(pointerr+8<=len(data)):
            ftyp['Type']='ftyp'
            pointerr=pointerr+8
        else:
            (pointerr,ftyp)
    
    if(pointerr+8<=len(data)):
        for i in range(pointerr, pointerr+8):
            tempo += data[i]
        ftyp['Major_Brand'] = hex_to_ascii(tempo)
        tempo = ""
        pointerr=pointerr+8
    else:
        (pointerr,ftyp)
    if(pointerr+8<=len(data)):
        for i in range(pointerr, pointerr+8):
            tempo += data[i]
        ftyp['Minor_Version'] = (tempo)
        tempo = ""
        pointerr=pointerr+8
    if inclusion==True:
        count = (ftyp['Size']*2-32)/4
        count = int(count/2)
        c_brand = []
        for j in range(0, count):
            c_brand.append(hex_to_ascii(data[pointerr:pointerr+8]))
            pointerr += 8
        ftyp['Compatible_Brands'] += c_brand
        return (pointerr,ftyp)
    else:
        c_brand=[]
        while(pointerr+8<=len(data)):
          c_brand.append(hex_to_ascii(data[pointerr:pointerr+8]))  
          pointerr += 8 
        ftyp['Compatible_Brands'] += c_brand
        return (pointerr,ftyp)
    
def free_classifier(pointer,data,inclusion):
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        free['Size'] = bigEnd(tempo)
        pointer += 16
    return (pointer,free)

def edts_classifier(pointer,data,inclusion):
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        edts['Size'] = bigEnd(tempo)
        pointer += 16
    return (pointer,edts)

def stbl_classifier(pointer,data,inclusion):
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        stbl['Size'] = bigEnd(tempo)
        pointer += 16
    return (pointer,stbl)

def mdat_classifier(pointer,data,inclusion):
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        mdat['Size'] = bigEnd(tempo)
        pointer += mdat['Size']*2
    return (pointer,mdat)

def moov_classifier(pointer,data,inclusion):
    if inclusion:
        tempo=""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        moov['Size'] =bigEnd(tempo)
        pointer += moov['Size']*2
    return (pointer,moov)


def mvhd_classifier(pointer,data,inclusion):
    tempo=""
    pointerr=pointer
    if inclusion==True:
        if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
            mvhd['Size'] = bigEnd(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            (pointerr,mvhd)
        if(pointerr+8<=len(data)):
            mvhd['Type']='mvhd'
            pointerr=pointerr+8
        else:
            (pointerr,mvhd)
    if(pointerr+2<=len(data)):
        for j in range(pointerr, pointerr+2):
            tempo += data[j]
        mvhd['Version'] = tempo
        tempo = ""
        pointerr=pointerr+2
    else:
         return (pointerr,mvhd)
    if(pointerr+6<=len(data)):
        for j in range(pointerr, pointerr+6):
            tempo += data[j]
        mvhd['Flags'] = tempo
        pointerr=pointerr+6
        tempo = ""
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        tempo2=tempo
        mvhd['Creation_Time'] = convert_hex_to_datetime(tempo)
        Creation_Time['mvhd']=convert_hex_to_datetime(tempo)
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        pointerr=pointerr+8
        if tempo2!=tempo:        
            mvhd['Modification_Time'] = convert_hex_to_datetime(tempo2)
            Modification_Time['mvhd']=convert_hex_to_datetime(tempo2)
            mvhd['Time_Scale'] = tempo
            tempo = ""
        else:
            mvhd['Modification_Time'] = convert_hex_to_datetime(tempo)
            Modification_Time['mvhd']=convert_hex_to_datetime(tempo)
            tempo = ""    
            if(pointerr+8<=len(data)):
                for j in range(pointerr, pointerr+8):
                    tempo += data[j]
                mvhd['Time_Scale'] = tempo
                tempo = ""
                pointerr=pointerr+8
            else:
                return (pointerr,mvhd)
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Duration'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Preferred_Rate'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        mvhd['Preferred_Volume'] = tempo
        tempo = ""
        pointerr=pointerr+4 
    else:
        return (pointerr,mvhd)
    if(pointerr+20<=len(data)):
        for j in range(pointerr, pointerr+20):
            tempo += data[j]
        mvhd['Reserved'] = tempo
        tempo = ""
        pointerr=pointerr+20
    else:
        return (pointerr,mvhd)
    if(pointerr+72<=len(data)):
        for j in range(pointerr, pointerr+72):
            tempo += data[j]
        mvhd['Matrix'] = tempo
        Matrix['mvhd']=tempo
        tempo = ""
        pointerr=pointerr+72
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Preview_Time'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Preview_Duration'] = tempo
        tempo = ""
        pointerr=pointerr+8 
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Poster_Time'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Selection_Time'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Selection_Duration'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Current_Time'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        mvhd['Next_Track_ID'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,mvhd)
    if inclusion:
        pointerr=pointer+(mvhd['Size']*2)
    return (pointerr,mvhd)

def trak_classifier(pointer, data,inclusion):   
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        trak['Size'] = bigEnd(tempo)
        pointer += 16
    return (pointer,trak)

def tkhd_classifier(pointer,data,inclusion):
    tempo=""
    pointerr=pointer
    if inclusion==True:
        if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
            tkhd['Size'] = bigEnd(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            (pointerr,tkhd)
        if(pointerr+8<=len(data)):
            tkhd['Type']='tkhd'
            pointerr=pointerr+8
        else:
            (pointerr,tkhd)
    if(pointerr+2<=len(data)):
        for j in range(pointerr, pointerr+2):
            tempo += data[j]
        tkhd['Version'] = tempo
        tempo = ""
        pointerr=pointerr+2
    else:
         return (pointerr,tkhd)
    if(pointerr+6<=len(data)):
        for j in range(pointerr, pointerr+6):
            tempo += data[j]
        tkhd['Flags'] = tempo
        pointerr=pointerr+6
        tempo = ""
    else:
        return (pointerr,tkhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        tempo2=tempo
        tkhd['Creation_Time'] = convert_hex_to_datetime(tempo)
        Creation_Time['tkhd']=convert_hex_to_datetime(tempo)
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,tkhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        pointerr=pointerr+8
        if tempo2!=tempo:        
            tkhd['Modification_Time'] = convert_hex_to_datetime(tempo2)
            Modification_Time['tkhd']=convert_hex_to_datetime(tempo2)
            tkhd['Track_ID'] = tempo
            tempo = ""
        else:
            tkhd['Modification_Time'] = convert_hex_to_datetime(tempo)
            Modification_Time['tkhd']=convert_hex_to_datetime(tempo)
            tempo = ""    
            if(pointerr+8<=len(data)):
                for j in range(pointerr, pointerr+8):
                    tempo += data[j]
                tkhd['Track_ID'] = tempo
                tempo = ""
                pointerr=pointerr+8
            else:
                return (pointerr,tkhd)
    else:
        return (pointerr,tkhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        tkhd['Reserved'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,tkhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        tkhd['Duration'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,tkhd)
    if(pointerr+16<=len(data)):
        for j in range(pointerr, pointerr+16):
            tempo += data[j]
        tkhd['Reserved_2'] = tempo
        tempo = ""
        pointerr=pointerr+16
    else:
        return (pointerr,tkhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        tkhd['Layer'] = tempo
        tempo = ""
        pointerr=pointerr+4
    else:
        return (pointerr,tkhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        tkhd['Alternative_Group'] = tempo
        tempo = ""
        pointerr=pointerr+4
    else:
        return (pointerr,tkhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        tkhd['Volume'] = tempo
        tempo = ""
        pointerr=pointerr+4
    else:
        return (pointerr,tkhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        tkhd['Reserved_3'] = tempo
        tempo = ""
        pointerr=pointerr+4
    else:
        return (pointerr,tkhd)
    if(pointerr+72<=len(data)):
        for j in range(pointerr, pointerr+72):
            tempo += data[j]
        tkhd['Matrix_Structure'] = tempo
        Matrix['tkhd']=tempo
        tempo = ""
        pointerr=pointerr+72
    else:
        return (pointerr,tkhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        tkhd['Track_Width'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,tkhd)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        tkhd['Track_Height'] = tempo
        tempo = ""
        pointerr=pointerr+8
    else:
        return (pointerr,tkhd)
    if inclusion:
        pointerr=pointer+(tkhd['Size']*2)
    return (pointerr,tkhd)

def mdia_classifier(pointer,data,inclusion):
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        mdia['Size'] = bigEnd(tempo)
        pointer += 16
    return (pointer,mdia)
    
def mdhd_classifier(pointer,data,inclusion):
        tempo=""
        pointerr=pointer
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                mdhd['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,mdhd)
            if(pointerr+8<=len(data)):
                mdhd['Type']='mdhd'
                pointerr=pointerr+8
            else:
                (pointerr,mdhd)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            mdhd['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,mdhd)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            mdhd['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,mdhd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            tempo2=tempo
            mdhd['Creation_Time'] = convert_hex_to_datetime(tempo)
            Creation_Time['mdhd']=convert_hex_to_datetime(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            return (pointerr,mdhd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            pointerr=pointerr+8
            if tempo2!=tempo:        
                mdhd['Modification_Time'] = convert_hex_to_datetime(tempo2)
                Modification_Time['mdhd']=convert_hex_to_datetime(tempo2)
                mdhd['Time_Scale'] = tempo
                tempo = ""
            else:
                mdhd['Modification_Time'] = convert_hex_to_datetime(tempo)
                Modification_Time['mdhd']=convert_hex_to_datetime(tempo)
                tempo = ""    
                if(pointerr+8<=len(data)):
                    for j in range(pointerr, pointerr+8):
                        tempo += data[j]
                    mdhd['Time_Scale'] = tempo
                    tempo = ""
                    pointerr=pointerr+8
                else:
                    return (pointerr,mdhd)
        else:
            return (pointerr,mdhd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            mdhd['Duration'] = tempo
            tempo = ""
            pointerr=pointerr+8
        else:
            return (pointerr,mdhd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            mdhd['Language'] = tempo
            tempo = ""
            pointerr=pointerr+4
        else:
            return (pointerr,mdhd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            mdhd['Predefined'] = tempo
            tempo = ""
            pointerr=pointerr+4
        else:
            return (pointerr,mdhd)
        if inclusion:
            pointerr=pointer+(mdhd['Size']*2)
        return(pointerr,mdhd)
    
def hdlr_classifier(pointer,data,inclusion):
    tempo=""
    pointerr=pointer
    if inclusion==True:
        if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
            hdlr['Size'] = bigEnd(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            return (pointerr,hdlr)
        if(pointerr+8<=len(data)):
            hdlr['Type']='hdlr'
            pointerr=pointerr+8
        else:
           return (pointerr,hdlr)
    if(pointerr+2<=len(data)):
        for j in range(pointerr, pointerr+2):
            tempo += data[j]
        hdlr['Version'] = tempo
        tempo = ""
        pointerr=pointerr+2
    else:
        return (pointerr,hdlr)
    if(pointerr+6<=len(data)):
        for j in range(pointerr, pointerr+6):
            tempo += data[j]
        hdlr['Flags'] = tempo
        pointerr=pointerr+6
        tempo = ""
    else:
        return (pointerr,hdlr)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        hdlr['Component_Type'] = tempo
        pointerr=pointerr+8
        tempo = ""
    else:
        return (pointerr,hdlr)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        hdlr['Component_Subtype'] =  hex_to_ascii(tempo)
        pointerr=pointerr+8
        tempo = ""
    else:
        return (pointerr,hdlr)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        hdlr['Component_Manufacturer'] =  (tempo)
        pointerr=pointerr+8
        tempo = ""
    else:
        return (pointerr,hdlr)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        hdlr['Component_Flags'] =  (tempo)
        pointerr=pointerr+8
        tempo = ""
    else:
        return (pointerr,hdlr)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        hdlr['Component_Flags_Masks'] =  (tempo)
        tempo = ""
        pointerr=pointerr+8
        if inclusion:
            flag_pointer = pointerr
            end_pointer=pointer+(hdlr['Size']*2)
            for g in range(flag_pointer, end_pointer):
                tempo += data[g]
            try:
                hdlr['Component_Name'] = hex_to_ascii(tempo)
                return (end_pointer,hdlr)
            except:
                hdlr['Component_Name'] = (tempo)
                return (end_pointer,hdlr)
    else:
        return (pointerr,hdlr)
    return(pointerr,hdlr)

def minf_classifier(pointer,data,inclusion):
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        minf['Size'] = bigEnd(tempo)
        pointer += 16
    return (pointer,minf)

def vmhd_classifier(pointer,data,inclusion):
    tempo=""
    pointerr=pointer
    if inclusion==True:
        if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
            vmhd['Size'] = bigEnd(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            (pointerr,vmhd)
        if(pointerr+8<=len(data)):
            vmhd['Type']='vmhd'
            pointerr=pointerr+8
        else:
            (pointerr,vmhd)
    if(pointerr+2<=len(data)):
        for j in range(pointerr, pointerr+2):
            tempo += data[j]
        vmhd['Version'] = tempo
        tempo = ""
        pointerr=pointerr+2
    else:
        return (pointerr,vmhd)
    if(pointerr+6<=len(data)):
        for j in range(pointerr, pointerr+6):
            tempo += data[j]
        vmhd['Flags'] = tempo
        pointerr=pointerr+6
        tempo = ""
    else:
        return (pointerr,vmhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        vmhd['Graphics_Mode'] = tempo
        pointerr=pointerr+4
        tempo = ""
    else:
        return (pointerr,vmhd)
    if(pointerr+12<=len(data)):
        for j in range(pointerr, pointerr+12):
            tempo += data[j]
        vmhd['Opcolor'] = tempo
        pointerr=pointerr+12
        tempo = ""
    else:
        return (pointerr,vmhd)
    if inclusion:
        pointerr=pointer+(vmhd['Size']*2)
    return(pointerr,vmhd)

def smhd_classifier(pointer,data,inclusion):
    tempo=""
    pointerr=pointer
    if inclusion==True:
        if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
            smhd['Size'] = bigEnd(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            (pointerr,smhd)
        if(pointerr+8<=len(data)):
            smhd['Type']='smhd'
            pointerr=pointerr+8
        else:
            (pointerr,smhd)
    if(pointerr+2<=len(data)):
        for j in range(pointerr, pointerr+2):
            tempo += data[j]
        smhd['Version'] = tempo
        tempo = ""
        pointerr=pointerr+2
    else:
        return (pointerr,smhd)
    if(pointerr+6<=len(data)):
        for j in range(pointerr, pointerr+6):
            tempo += data[j]
        smhd['Flags'] = tempo
        pointerr=pointerr+6
        tempo = ""
    else:
        return (pointerr,smhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        smhd['Balance'] = tempo
        pointerr=pointerr+4
        tempo = ""
    else:
        return (pointerr,smhd)
    if(pointerr+4<=len(data)):
        for j in range(pointerr, pointerr+4):
            tempo += data[j]
        smhd['Reserved'] = tempo
        pointerr=pointerr+4
        tempo = ""
    else:
        return (pointerr,smhd)
    if inclusion:
        pointerr=pointer+(smhd['Size']*2)
    return(pointerr,smhd)

def dinf_classifier(pointer,data,inclusion):
    if inclusion:
        tempo = ""
        for i in range(pointer, pointer+8):
            tempo += data[i]
        dinf['Size'] = bigEnd(tempo)
        pointer += 16
    return (pointer,dinf)

def dref_classifier(pointer,data,inclusion):
    tempo=""
    pointerr=pointer
    if inclusion==True:
        if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
            dref['Size'] = bigEnd(tempo)
            tempo = ""
            pointerr=pointerr+8
        else:
            (pointerr,dref)
        if(pointerr+8<=len(data)):
            dref['Type']='dref'
            pointerr=pointerr+8
        else:
            (pointerr,dref)
    if(pointerr+2<=len(data)):
        for j in range(pointerr, pointerr+2):
            tempo += data[j]
        dref['Version'] = tempo
        tempo = ""
        pointerr=pointerr+2
    else:
        return (pointerr,dref)
    if(pointerr+6<=len(data)):
        for j in range(pointerr, pointerr+6):
            tempo += data[j]
        dref['Flags'] = tempo
        pointerr=pointerr+6
        tempo = ""
    else:
        return (pointerr,dref)
    if(pointerr+8<=len(data)):
        for j in range(pointerr, pointerr+8):
            tempo += data[j]
        dref['Number_of_Entries'] = bigEnd(tempo)
        entry_count = dref['Number_of_Entries']
        pointerr=pointerr+8
        print("\n", "Data Reference Information (dref) Atom Details are:")
        dprint(dref)
        print("\nSince we have ", entry_count, "Number of entries we are going to have",
                    entry_count, "number of data references like url atom etc")
        count = 0
        tempo = ""
        while (count < entry_count):
            tempo = ""
            if(pointerr+8<=len(data)):
                for j in range(pointerr, pointerr+8):
                    tempo += data[j]
                url['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+16
            else:
                print(url)
                break
            if(pointerr+2<=len(data)):
                for j in range(pointerr, pointerr+2):
                    tempo += data[j]
                url['Version'] = tempo
                tempo = ""
                pointerr=pointerr+2
            else:
                print(url)
                break
            if(pointerr+6<=len(data)):
                for j in range(pointerr, pointerr+6):
                    tempo += data[j]
                url['Flags'] = tempo
                tempo = ""
                pointerr=pointerr+6
                count += 1
            else:
                print(url)
                break
            print('\nurl'.upper()+" Atom Details are:-------------------------------------")
            dprint(url)
    else:
        return (pointerr,dref)
    if inclusion:
        pointerr=pointer+(dref['Size']*2)
    return (pointerr,dref)

def sample_atom_classifier(atom, pointer, data,inclusion):
    tempo=""
    pointerr=pointer
    cur_size=0
    if(pointerr+8<=len(data)):
            for i in range(pointerr, pointerr+8):
                tempo += data[i]
                cur_size  = bigEnd(tempo)
            tempo = ""
    if(atom=='stsd'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                stsd['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,stsd)
            if(pointerr+8<=len(data)):
                stsd['Type']='stsd'
                pointerr=pointerr+8
            else:
                (pointerr,stsd)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            stsd['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,stsd)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            stsd['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Number_of_Entries'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Sample_Description_Size'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Data_Format'] = hex_to_ascii(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['version'] = (tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['Revision_Level'] = bigEnd(tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Vendor'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Temporal_Quality'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Spatial_Quality'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['Media_Width'] = bigEnd(tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['Media_Height'] = bigEnd(tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Horizontal_Resolution'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['Vertical_Resolution'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['DataSize'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['Frame_Count'] = bigEnd(tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        tempo=""
        t1=""
        if pointerr+2<=len(data):
            t1=t1+data[pointerr]
            pointerr=pointerr+1
            t1=t1+data[pointerr]
            pointerr=pointerr+1
            while(t1!='00' and pointerr+2<=len(data)):
                tempo=tempo+t1
                t1=""
                t1=t1+data[pointerr]
                pointerr=pointerr+1
                t1=t1+data[pointerr]
                pointerr=pointerr+1
        stsd['compressorname']=hex_to_ascii(tempo)
        tempo=""
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['bits_per_sample'] = bigEnd(tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['channelcount'] = bigEnd(tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+4<=len(data)):
            for j in range(pointerr, pointerr+4):
                tempo += data[j]
            stsd['samplesize'] = bigEnd(tempo)
            pointerr=pointerr+4
            tempo = ""
        else:
            return (pointerr,stsd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsd['samplerate'] = bigEnd(tempo)
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsd)
        if inclusion:
            for j in range(pointerr, pointer+(stsd['Size']*2)):
                tempo += data[j]
            stsd['format_specific_data'] =(tempo)
            return (pointer+(stsd['Size']*2),stsd)
        else:
            return (pointerr,stsd)
        
    if(atom=='stts'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                stts['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,stts)
            if(pointerr+8<=len(data)):
                stts['Type']='stts'
                pointerr=pointerr+8
            else:
                (pointerr,stts)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            stts['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,stts)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            stts['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,stts)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stts['Number_of_Entries'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stts)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stts['Sample_Duration'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stts)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stts['Sample_Count'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stts)
        if inclusion:
            pointerr=pointer+(stts['Size']*2)
        return (pointerr,stts)
    if(atom=='stss'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                stss['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,stss)
            if(pointerr+8<=len(data)):
                stss['Type']='stss'
                pointerr=pointerr+8
            else:
                (pointerr,stss)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            stss['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,stss)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            stss['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,stss)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stss['Number_of_Entries'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stss)
        if inclusion:
            last_pointer = pointer+(stss['Size']*2)
            tempo = ""
            for f in range(pointerr,last_pointer):
                tempo += data[f]
            stss['Sync-sample-table'] = tempo
            pointerr=last_pointer
        return (pointerr,stss)
    if(atom=='stsc'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                stsc['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,stsc)
            if(pointerr+8<=len(data)):
                stsc['Type']='stsc'
                pointerr=pointerr+8
            else:
                (pointerr,stsc)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            stsc['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,stsc)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            stsc['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,stsc)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsc['Number_of_Entries'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsc)
        if inclusion:
            last_pointer = pointer+(stsc['Size']*2)
            tempo = ""
            for f in range(pointerr,last_pointer):
                tempo += data[f]
            stsc['Sample-to-Chunk_Table'] = tempo
            pointerr=last_pointer
        return (pointerr,stsc)
    if(atom=='stsz'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                stsz['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,stsz)
            if(pointerr+8<=len(data)):
                stsz['Type']='stsz'
                pointerr=pointerr+8
            else:
                (pointerr,stsz)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            stsz['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,stsz)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            stsz['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,stsz)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsz['Sample_Size'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsz)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stsz['Number_of_Entries'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stsz)
        if inclusion:
            last_pointer = pointer+(stsz['Size']*2)
            tempo = ""
            for f in range(pointerr,last_pointer):
                tempo += data[f]
            stsz['Sample-to-Size_Table'] = tempo
            pointerr=last_pointer
        return (pointerr,stsz)
    if(atom=='stco'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                stco['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,stco)
            if(pointerr+8<=len(data)):
                stco['Type']='stco'
                pointerr=pointerr+8
            else:
                (pointerr,stco)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            stco['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,stco)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            stco['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,stco)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stco['Number_of_Entries'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stco)
        if inclusion:
            last_pointer = pointer+(stco['Size']*2)
            tempoo = ""
            for f in range(pointerr,last_pointer):
                tempoo += data[f]
            stco['Chunk_offset_table'] = tempoo
            pointerr=last_pointer  
        return (pointerr,stco)
    if(atom=='ctts'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                ctts['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,ctts)
            if(pointerr+8<=len(data)):
                ctts['Type']='ctts'
                pointerr=pointerr+8
            else:
                (pointerr,ctts)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            ctts['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,ctts)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            ctts['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,ctts)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            ctts['Entry-Count'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,ctts)
        if inclusion:
            last_pointer = pointer+(ctts['Size']*2)
            tempo = ""
            for f in range(pointerr,last_pointer):
                tempo += data[f]
            ctts['Composition-offset-table'] = tempo
            pointerr=last_pointer
        return (pointerr,ctts)
    if(atom=='sdtp'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                sdtp['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,sdtp)
            if(pointerr+8<=len(data)):
                sdtp['Type']='sdtp'
                pointerr=pointerr+8
            else:
                (pointerr,sdtp)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            sdtp['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,sdtp)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            sdtp['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,sdtp)
        if inclusion:
            last_pointer = pointer+(sdtp['Size']*2)
            tempo = ""
            for f in range(pointerr,last_pointer):
                tempo += data[f]
            sdtp['Sample-Dependency-Flags-Table'] = tempo
            pointerr=last_pointer
        return (pointerr,sdtp)
    if(atom=='stps'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                stps['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,stps)
            if(pointerr+8<=len(data)):
                stps['Type']='stps'
                pointerr=pointerr+8
            else:
                (pointerr,stps)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            stps['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,stps)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            stps['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,stps)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            stps['Entry-Count'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,stps)
        if inclusion:
            last_pointer = pointer+(stps['Size']*2)
            tempo = ""
            for f in range(pointerr,last_pointer):
                tempo += data[f]
            stps['Partial-Sync-Sample-Table'] = tempo
        return (pointerr,stps)
    if(atom=='cslg'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                cslg['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,cslg)
            if(pointerr+8<=len(data)):
                cslg['Type']='cslg'
                pointerr=pointerr+8
            else:
                (pointerr,cslg)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            cslg['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,cslg)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            cslg['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,cslg)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            cslg['CompositionOffsetToDisplayOffset'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,cslg)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            cslg['LeastDisplayOffset'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,cslg)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            cslg['DisplayStartTime'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,cslg)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            cslg['DispalyEndTime'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,cslg)
        if inclusion:
            pointerr=pointer+(cslg['Size']*2)
        return (pointerr,cslg)
    if(atom=='sgpd'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                sgpd['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,sgpd)
            if(pointerr+8<=len(data)):
                sgpd['Type']='sgpd'
                pointerr=pointerr+8
            else:
                (pointerr,sgpd)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            sgpd['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,sgpd)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            sgpd['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,sgpd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            sgpd['DefaultLength'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,sgpd)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            sgpd['EntryCount'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,sgpd)
        if inclusion:
          end_pointer = pointer+(sgpd['Size']*2)
          tempo = ""
          for f in range(pointerr, end_pointer):
             tempo += data[f]
          sgpd['PayloadData'] = tempo
          pointerr=end_pointer
          return (pointerr,sgpd)
        else:
            return (pointerr,sgpd)

    if(atom=='sbgp'):
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                sbgp['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,sbgp)
            if(pointerr+8<=len(data)):
                sbgp['Type']='sbgp'
                pointerr=pointerr+8
            else:
                (pointerr,sbgp)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            sbgp['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,sbgp)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            sbgp['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,sbgp)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            sbgp['EntryCount'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,sbgp)
        if inclusion:
          end_pointer = pointer+(sbgp['Size']*2)
          tempo = ""
          for f in range(pointerr, end_pointer):
             tempo += data[f]
          sbgp['TableData'] = tempo
          pointerr=end_pointer
          return (pointerr,sbgp)
        else:
            return (pointerr,sbgp)
def udta_classifier(pointer,data,inclusion):
        pointerr=pointer
        tempo=''
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                udta['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,udta)
            if(pointerr+8<=len(data)):
                udta['Type']='udta'
                pointerr=pointerr+8
            else:
                (pointerr,udta)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            udta['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,udta)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            udta['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,udta)
        if inclusion:
          end_pointer = pointer+(udta['Size']*2)
          tempo = ""
          for f in range(pointerr, end_pointer):
             tempo += data[f]
          udta['UserDataList'] = tempo
          pointerr=end_pointer
          return (pointerr,udta)
        else:
            return (pointerr,udta)
        
def elst_classifier(pointer,data,inclusion): 
        pointerr=pointer
        tempo=""
        if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                elst['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                (pointerr,elst)
            if(pointerr+8<=len(data)):
                elst['Type']='elst'
                pointerr=pointerr+8
            else:
                (pointerr,elst)
        if(pointerr+2<=len(data)):
            for j in range(pointerr, pointerr+2):
                tempo += data[j]
            elst['Version'] = tempo
            tempo = ""
            pointerr=pointerr+2
        else:
            return (pointerr,elst)
        if(pointerr+6<=len(data)):
            for j in range(pointerr, pointerr+6):
                tempo += data[j]
            elst['Flags'] = tempo
            pointerr=pointerr+6
            tempo = ""
        else:
            return (pointerr,elst)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            elst['EntryCount'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,elst)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            elst['EditDuration'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,elst)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            elst['EditMediaTime'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,elst)
        if(pointerr+8<=len(data)):
            for j in range(pointerr, pointerr+8):
                tempo += data[j]
            elst['PlaybackSpeed'] = tempo
            pointerr=pointerr+8
            tempo = ""
        else:
            return (pointerr,elst)
        if inclusion:
            pointerr=pointer+(elst['Size']*2)
        return (pointerr,elst)
def iods_classifier(pointer,data,inclusion):
    pointerr=pointer
    tempo=""
    if inclusion==True:
            if(pointerr+8<=len(data)):
                for i in range(pointerr, pointerr+8):
                    tempo += data[i]
                iods['Size'] = bigEnd(tempo)
                tempo = ""
                pointerr=pointerr+8
            else:
                return (pointerr,iods)
            if(pointerr+8<=len(data)):
                iods['Type']='iods'
                pointerr=pointerr+8
            else:
                return (pointerr,iods)
    if(pointerr+2<=len(data)):
        for j in range(pointerr, pointerr+2):
            tempo += data[j]
        iods['Version'] = tempo
        tempo = ""
        pointerr=pointerr+2
    else:
        return (pointerr,iods)
    if(pointerr+6<=len(data)):
        for j in range(pointerr, pointerr+6):
            tempo += data[j]
        iods['Flags'] = tempo
        pointerr=pointerr+6
        tempo = ""
    else:
        return (pointerr,iods)
    if inclusion:
          end_pointer = pointer+(iods['Size']*2)
          tempo = ""
          for f in range(pointerr, end_pointer):
             tempo += data[f]
          iods['OtherData'] = tempo
          pointerr=end_pointer
          return (pointerr,iods)
    else:
          return (pointerr,iods)

    

        



    
    
    

        
            
        


        
        
        
        
            
        
        
            
        
            
        
            
            
        
            
        
        
            
            
        
        
        
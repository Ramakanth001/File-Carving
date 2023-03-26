#Atom classification - 1.1
#Implementation using functional programming
#Inclusion of Sample Atoms Classifier
#inclusion of Intergrity checker


# Atom classification
# from traitlets import directional_link
from IntegrityChecker import integrity_checker
from SupportFunctions import litEnd,bigEnd,hex_to_ascii,dprint
from HexData import data
from AtomDictionaries import ftyp,free,mdat,moov,mvhd,trak,tkhd,mdia,mdhd,hdlr,minf,smhd,vmhd,dinf,dref,url,stbl,stsd,stts,stss,stsc,stsz,stco,ctts,sdtp,stps,cslg,udta
# In FPRINT call DPRINT and write that into file so that data is in the foprm of dictionary in files
myf = open('output.txt','w')
myf.write("FILE CONTENT:\n")
# myf.write(my_file_data)


# print("File hex data :\n",data,"\n")
# print("Size in hex | Size in decimal\n")
block_count=0
file_size=0
block_size_H=[]
block_size_D=[]
block_type=[]
block_sub_type=[]
cur_size=0
temp=""
hex_pointer=0
moov_pointer=0

#Function definitions start from here

def test(n):
  for i in range(n):
    print(data[i],end="")

def initial_chunk():
  initial_size=data[:8]
  block_size_H.append(initial_size)
  initial_size_dec=litEnd(initial_size)
  block_size_D.append(initial_size_dec)
  print(initial_size,"   |  ",initial_size_dec)
  block_count+=1

def dprint(my_dict):
  for attribute,value in my_dict.items():
    print("\'",attribute,"\' : ",value,sep="")


def atom_seeker(pointer):
  #IMPORTANT CODE PART : (incase we need to work on atoms as per which ever is occuring next as per hex file)
  # SEEKING TILL WE FIND A PARTICULAR ATOM

  # Change conventions of cur_pointer and moov_pointer
      print(data[cur_pointer+1])
      tempo=""
      temp=""
      while(temp!="minf"):
        temp=""
        tempo=""
        for k in range(cur_pointer,cur_pointer+8):
          tempo+=data[k]
        print(tempo)
        try:
          temp=hex_to_ascii(tempo)
          print(temp)
        except:
          pass
        cur_pointer+=1   
      print(temp)
      moov_pointer=cur_pointer-1
      # points to 'minf' type starting we need to take it 
      # back to 4 bytes to get its size
      moov_pointer-=8 
      for i in range(0,8):
        print(data[moov_pointer+i])

def ftyp_classifier(pointer,size):
    tempo=""
    for i in range(pointer,pointer+8):
        tempo+=data[i]
    ftyp['Size']=bigEnd(tempo)
    tempo=""
    for i in range(pointer+16,pointer+24):
        tempo+=data[i]
    ftyp['Major_Brand']=hex_to_ascii(tempo)
    tempo=""
    for i in range(pointer+24,pointer+32):
        tempo+=data[i]
    ftyp['Minor_Version']=(tempo)
    pointer+=32
    # print("size is" , size*2)
    count=(size*2-32)/4
    count=int(count/2)
    # these are number of major brands available
    tempo=""
    c_brand=[]
    for j in range(0,count):
      c_brand.append(hex_to_ascii(data[pointer:pointer+8]))
      pointer+=8
    # print(count)
    ftyp['Compatible_Brands']+=c_brand
    return pointer


def free_classifier(pointer,size):
    if(cur_atom == "free"):
        tempo=""
        for i in range(pointer,pointer+8):
            tempo+=data[i]
        free['Size']=bigEnd(tempo)
        pointer+=16
        return pointer


def mdat_classifier(pointer,size):
    if(cur_atom=="mdat"):
        tempo=""
        for i in range(pointer,pointer+8):
            tempo+=data[i]
        mdat['Size']=size
        print(size)
        pointer+=size*2
        return pointer

def moov_classifier(pointer,size):
      if(cur_atom=="moov"):
        moov['Size']=size
        pointer+=size*2
      return pointer

def mvhd_classifier(pointer,size):
        if(cur_atom=="mvhd"):    
            mvhd['Size']=size
            tempo=""
            for j in range(pointer+16,pointer+18):
              tempo+=data[j]
            mvhd['Version']=tempo
            tempo=""
            for j in range(pointer+18,pointer+24):
              tempo+=data[j]
            mvhd['Flags']=tempo
            # print(mvhd['Flags']) 
            tempo=""
            for j in range(pointer+24,pointer+32):
              tempo+=data[j]
            mvhd['Creation_Time']=tempo
            tempo=""
            for j in range(moov_pointer+32,pointer+40):
              tempo+=data[j]
            mvhd['Modification_Time']=tempo 
            tempo=""
            for j in range(pointer+40,pointer+48):
              tempo+=data[j]
            mvhd['Time_Scale']=tempo 
            tempo=""
            for j in range(pointer+48,pointer+56):
              tempo+=data[j]
            mvhd['Duration']=tempo
            tempo=""
            for j in range(pointer+56,pointer+64):
              tempo+=data[j]
            mvhd['Preferred_Rate']=tempo
            tempo=""
            for j in range(pointer+64,pointer+68):
              tempo+=data[j]
            mvhd['Preferred_Volume']=tempo
            tempo=""
            for j in range(pointer+68,pointer+88):
              tempo+=data[j]
            mvhd['Reserved']=tempo
            tempo=""
            for j in range(pointer+88,pointer+160):
              tempo+=data[j]
            mvhd['Matrix']=tempo
            tempo=""
            for j in range(pointer+160,pointer+208):
              tempo+=data[j]
            mvhd['Predefines']=tempo
            tempo=""
            for j in range(pointer+208,pointer+216):
              tempo+=data[j]
            mvhd['Next_Track_ID']=tempo
            pointer=pointer+216
          #updating the moov pointer to the seeked position after parsing the attributes
        return pointer 

def trak_classifier(pointer,size):
    if(cur_atom=="trak"):
        trak['Size']=size
        pointer+=size*2
    return pointer

def tkhd_classifier(pointer,size):
       if(cur_atom=="tkhd"):
          tkhd['Size']=size
          pointer+=16
          tempo=""
          for j in range(pointer,pointer+2):
              tempo+=data[j]
          tkhd['Version']=tempo
          tempo=""
          for j in range(pointer+2,pointer+8):
            tempo+=data[j]
          tkhd['Flags']=tempo
          
          tempo=""
          for j in range(pointer+8,pointer+16):
              tempo+=data[j]
          tkhd['Creation_Time']=tempo
          tempo=""
          for j in range(pointer+16,pointer+24):
              tempo+=data[j]
          tkhd['Modification_Time']=tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
              tempo+=data[j]
          tkhd['Track_ID']=tempo
          tempo=""
          for j in range(pointer+32,pointer+40):
              tempo+=data[j]
          tkhd['Reserved']=tempo
          tempo=""
          for j in range(pointer+40,pointer+48):
              tempo+=data[j]
          tkhd['Duration']=tempo
          tempo=""
          for j in range(pointer+48,pointer+64):
              tempo+=data[j]
          tkhd['Reserved_2']=tempo
          tempo=""
          for j in range(pointer+64,pointer+68):
              tempo+=data[j]
          tkhd['Layer']=tempo
          tempo=""
          for j in range(pointer+68,pointer+72):
              tempo+=data[j]
          tkhd['Alternative_Group']=tempo
          tempo=""
          for j in range(pointer+72,pointer+76):
              tempo+=data[j]
          tkhd['Volume']=tempo
          tempo=""
          for j in range(pointer+76,pointer+80):
              tempo+=data[j]
          tkhd['Reserved_3']=tempo
          tempo=""
          for j in range(pointer+80,pointer+152):
              tempo+=data[j]
          tkhd['Matrix_Structure']=tempo
          tempo=""
          for j in range(pointer+152,pointer+160):
              tempo+=data[j]
          tkhd['Track_Width']=tempo
          tempo=""
          for j in range(pointer+160,pointer+168):
              tempo+=data[j]    
          tkhd['Track_Height']=tempo
          pointer+=168
          return pointer

def mdia_classifier(pointer,size):
    if(cur_atom=="mdia"):
        mdia['Size']=size
        pointer+=size*2
    return pointer

def mdhd_classifier(pointer,size):
      if(cur_atom=="mdhd"):
          mdhd['Size']=size
          pointer+=16
          tempo=""
          for j in range(pointer,pointer+2):
              tempo+=data[j]
          mdhd['Version']=tempo
          tempo=""
          for j in range(pointer+2,pointer+8):
            tempo+=data[j]
          mdhd['Flags']=tempo
          tempo=""
          for j in range(pointer+8,pointer+16):
              tempo+=data[j]
          mdhd['Creation_Time']=tempo
          tempo=""
          for j in range(pointer+16,pointer+24):
              tempo+=data[j]
          mdhd['Modification_Time']=tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
              tempo+=data[j]
          mdhd['Time_Scale']=tempo
          tempo=""
          for j in range(pointer+32,pointer+40):
              tempo+=data[j]
          mdhd['Duration']=tempo
          tempo=""
          for j in range(pointer+40,pointer+44):
              tempo+=data[j]
          mdhd['Language']=tempo
          tempo=""
          for j in range(pointer+44,pointer+48):
              tempo+=data[j]
          mdhd['Predefined']=tempo
          pointer+=48
          return pointer

def hdlr_classifier(pointer,size):
          hdlr['Size']=size
          pointer+=16 
          tempo=""
          for j in range(pointer,pointer+2):
              tempo+=data[j]
          hdlr['Version']=tempo
          tempo=""
          for j in range(pointer+2,pointer+8):
            tempo+=data[j]
          hdlr['Flags']=tempo
          tempo=""
          for j in range(pointer+8,pointer+16):
            tempo+=data[j]
          hdlr['Component_Type']=tempo
          tempo=""
          for j in range(pointer+16,pointer+24):
            tempo+=data[j]
          hdlr['Component_Subtype']=hex_to_ascii(tempo)
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          hdlr['Component_Manufacturer']=tempo
          tempo=""
          for j in range(pointer+32,pointer+40):
            tempo+=data[j]
          hdlr['Component_Flags']=tempo
          tempo=""
          for j in range(pointer+40,pointer+48):
            tempo+=data[j]
          hdlr['Component_Flags_Masks']=tempo
          flag_pointer=pointer+48
          # Strangely the below thing is working
          # moov_pointer+=(hdlr['Size']-16)*2
          pointer=pointer+(hdlr['Size']*2)
         
          #Now moov pointer is pointing to next atom this works because 
          # we can find variable size of parameter by seeking to end of the atom
          tempo=""
          for g in range(flag_pointer,pointer-16):
            tempo+=data[g]
          try:
            hdlr['Component_Name'] = hex_to_ascii(tempo)
            return pointer-16
          except:
            hdlr['Component_Name'] = (tempo)
            return pointer-16

def minf_classifier(pointer,size):
    if(cur_atom=="minf"):
        minf['Size']=size
        pointer+=size*2
    return pointer

def vmhd_classifier(pointer,size):
    if(cur_atom=="vmhd"):
          vmhd['Size']=size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          vmhd['Version'] =tempo
          tempo=""  
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          vmhd['Flags']=tempo 
          tempo="" 
          for j in range(pointer+24,pointer+28):
               tempo+=data[j]
               vmhd['Graphics_Mode']=tempo
          tempo=""
          for j in range(pointer+28,pointer+40):
                tempo+=data[j]
          vmhd['Opcolor']=tempo 
          pointer+=40
          return pointer


def smhd_classifier(pointer,size):
     print("vooo")
     if(cur_atom=="smhd"):
              smhd['Size']=size
              tempo=""
              for j in range(pointer+16,pointer+18):
                tempo+=data[j]
              smhd['Version'] =tempo
              tempo=""  
              for j in range(pointer+18,pointer+24):
                tempo+=data[j]
              smhd['Flags']=tempo    
              tempo=""
              for j in range(pointer+24,pointer+28):
                  tempo+=data[j]
              smhd['Balance'] = tempo
              tempo=""
              for j in range(pointer+28,pointer+32):
                  tempo+=data[j]
              smhd['Reserved'] = tempo 
              pointer+=32
              return pointer

def dinf_classifier(pointer,size):
     if(cur_atom=="dinf"):
        dinf['Size']=size
        pointer+=size*2
     return pointer

def dref_classifier(pointer,size):
    if(cur_atom =="dref"):
          dref['Size']= size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          dref['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          dref['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          dref['Number_of_Entries'] = bigEnd(tempo)
          entry_count=dref['Number_of_Entries']
          pointer+=32
          print("\n","Data Reference Information (dref) Atom Details are:")
          dprint(dref)
          print("Since we have ", entry_count,"Number of entries we are going to have", entry_count, "number of data references like url atom etc")
          count=0
          # Write url atoms individaually to files so that all occurances of data references in the form of url atoms can be stored since lastest url atom is kept at the directionary
          while(count<entry_count):
            print("uoo")
            #cur_atom="url"
            tempo=""
            for j in range(pointer,pointer+8):
                tempo+=data[j]
            print(tempo)
            # break
            url['Size']=bigEnd(tempo)
            tempo=""
            for j in range(pointer+16,pointer+18):
                tempo+=data[j]
            url['Version'] = tempo
            tempo=""
            for j in range(pointer+18,pointer+24):
                tempo+=data[j]
            url['Flags'] = tempo
            pointer+=24
            count+=1
            print("\nURL referenced data items (url) details:")
            dprint(url)
          return pointer

def sample_atom_classifier(atom,pointer,size):
      cur_size=size
      if(atom == 'stsd'):
          cur_atom = "stsd"
          tempo=""
          for j in range(pointer,pointer+8):
            tempo+=data[j]
          stsd['Size']= bigEnd(tempo)
          print(bigEnd(tempo))
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          stsd['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          stsd['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stsd['Number_of_Entries'] = tempo
          tempo=""
          for j in range(pointer+32,pointer+40):
            tempo+=data[j]
          stsd['Sample_Description_Size'] =bigEnd(tempo)
          tempo=""
          for j in range(pointer+40,pointer+48):
            tempo+=data[j]
          stsd['Data_Format'] =hex_to_ascii(tempo)
          tempo=""
          for j in range(pointer+48,pointer+60):
            tempo+=data[j]
          stsd['Reserved1'] = (tempo)
          tempo=""
          for j in range(pointer+60,pointer+68):
            tempo+=data[j]
          stsd['Data_Reference_Index'] = (tempo)
          tempo=""
          for j in range(pointer+68,pointer+80):
            tempo+=data[j]
          stsd['Predefines'] = (tempo)
          tempo=""
          for j in range(pointer+80,pointer+92):
            tempo+=data[j]
          stsd['Reserved2'] = (tempo)
          # Predefines and Reserved are 6 bytes each(moovP:48)
          pointer+=(stsd['Size']*2)
          # here sample description size is size of various format types present 
          # in stsd atoms - in this atom 'mp4a'. Here we have only 1 entry i.e., stsd['Number_of_entries']
          # fo all those entries re-coumputation of constituent elements has to be done
          print("\nSample Table Description(stsd) details:")
          dprint(stsd)
          return pointer
      if(atom == 'stts'):
          cur_atom = "stts"
          stts['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          stts['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          stts['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stts['Number_of_Entries'] = tempo
          tempo=""
          for j in range(pointer+32,pointer+40):
            tempo+=data[j]
          stts['Sample_Duration'] = tempo
          tempo=""
          for j in range(pointer+40,pointer+48):
            tempo+=data[j]
          stts['Sample_Count'] = tempo
          print("\nSample to Time-Table Samples(stts) details:")
          dprint(stts)
          pointer+=48
          return pointer
          # we done with stts
      if(atom == 'stss'):
          cur_atom = "stss"
          stss['Size'] = cur_size
          tempo=""
          cur_pointer = pointer
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          stss['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          stss['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stss['Number_of_Entries'] = tempo
          flag_pointer=pointer+32
          pointer=cur_pointer+(stss['Size']*2)
          #Now moov pointer is pointing to next atom this works because 
          # we can find variable size of parameter by seeking to end of the atom
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          stss['Sync-sample-table'] = tempo
          print("\nSample to Sync Samples(stss) details:")
          dprint(stss)
          # moov_pointer+=40
          return pointer
          # done with stss
      if(atom == 'stsc'):
          cur_atom = 'stsc'
          cur_pointer=pointer
          stsc['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          stsc['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          stsc['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stsc['Number_of_Entries'] = tempo
          flag_pointer = pointer+32
          print(flag_pointer)
          pointer=cur_pointer+(stsc['Size']*2)
          # print("ziggaaaaa")
          # print(moov_pointer)
          # print(stsc['Size'])
          #Now moov pointer is pointing to next atom this works because 
          # we can find variable size of parameter by seeking to end of the atom
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          stsc['Sample-to-Chunk_Table'] = tempo
          #The next attribute is sample to chunk table whose size is variable in nature
          #In order to parse without knowing what its size is, we simply move the moov pointer to end of the atom
          #The un-parsed data must belong to the variable size attribute (from cur_pointer to moov_pointer)
          # tempo=""
          # for i in range(cur_pointer,moov_pointer):
          #   tempo+=data[i]
          # stsc['Sample-to-Chunk_Table'] = tempo
          # moov_pointer=moov_pointer+stsc['Size']
          
          print("\nSample to sample chunk(stsc) atom details:")
          dprint(stsc)
          return pointer
          #stsc atom complete
      if(atom == 'stsz'):
          cur_atom = "stsz"
          cur_pointer=pointer
          stsz['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          stsz['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          stsz['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stsz['Sample_Size'] = tempo
          tempo=""
          for j in range(pointer+32,pointer+40):
            tempo+=data[j]
          stsz['Number_of_Entries'] = tempo
          flag_pointer = pointer+40
          pointer=cur_pointer+(stsz['Size']*2)
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          stsz['Sample-to-Size_Table'] = tempo
          print("\nSample to Size Table(stsz) atom details:")
          dprint(stsz)
          return pointer
          #done with stsz atom
      if(atom == 'stco'):
          cur_atom = "stco"
          cur_pointer=pointer
          stco['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          stco['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          stco['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stco['Number_of_Entries'] = tempo
          flag_pointer = pointer+32
          pointer=cur_pointer+(stco['Size']*2)
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          stco['Chunk_offset_table'] = tempo
          print("\n Chunk offset (stco) atom  details:")
          dprint(stco)
          return pointer
          # done with stco
      if(atom == 'ctts'):
          cur_atom = "ctts"
          cur_pointer=pointer
          ctts['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          ctts['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          ctts['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          ctts['Entry-Count'] = tempo
          flag_pointer = pointer+32
          pointer=cur_pointer+(ctts['Size']*2)
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          ctts['Composition-offset-table'] = tempo
          print("\nComposition offset Table (ctts) details:")
          dprint(ctts)
          return pointer
          
      if(atom == 'sdtp') :
          cur_atom = 'sdtp'
          cur_pointer=pointer
          sdtp['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          sdtp['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          sdtp['Flags'] = tempo
          flag_pointer = pointer+24
          pointer=cur_pointer+(sdtp['Size']*2)
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          sdtp['Sample-Dependency-Flags-Table'] = tempo
          print("\n'Sample Dependency Flag Atom (sdtp) details:")
          dprint(sdtp)
          return pointer
      if(atom=='stps'):
          cur_atom = "stps"
          cur_pointer=pointer
          stps['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          stps['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          stps['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stps['Entry-Count'] = tempo
          flag_pointer = pointer+32
          pointer=cur_pointer+(ctts['Size']*2)
          tempo=""
          for f in range(flag_pointer,pointer):
            tempo+=data[f]
          stps['Partial-Sync-Sample-Table'] = tempo
          print("\nPartial Sync Sample (stps) atom details:")
          dprint(stps)
          return pointer 
      if(atom=='cslg'):
          cur_atom = "stps"
          cur_pointer=pointer
          cslg['Size'] = cur_size
          tempo=""
          for j in range(pointer+16,pointer+18):
            tempo+=data[j]
          cslg['Version'] = tempo
          tempo=""
          for j in range(pointer+18,pointer+24):
            tempo+=data[j]
          cslg['Flags'] = tempo
          tempo=""
          for j in range(pointer+24,pointer+32):
            tempo+=data[j]
          stps['CompositionOffsetToDisplayOffset'] = tempo
          tempo=""
          for j in range(pointer+32,pointer+40):
            tempo+=data[j]
          stps['LeastDisplayOffset'] = tempo
          tempo=""
          for j in range(pointer+40,pointer+48):
            tempo+=data[j]
          stps['DisplayStartTime'] = tempo
          tempo=""
          for j in range(pointer+48,pointer+56):
            tempo+=data[j]
          stps['DispalyEndTime'] = tempo
          print("\ncomposition shift least greatest atom (cslg) atom details:")
          dprint(cslg)
          return pointer
      


try:
        cur_size, cur_atom = integrity_checker(hex_pointer)
        print(cur_size,cur_atom)
  # while(data[hex_pointer]!=''):
        while(cur_atom=="ftyp" or cur_atom=="free" or cur_atom=="mdat"):
              if(cur_atom=="ftyp"):
                 hex_pointer=ftyp_classifier(hex_pointer,cur_size)
                 print("\n","File type(ftyp) Atom Details are:")
                 dprint(ftyp) 
              elif(cur_atom=="free"):
                  hex_pointer=free_classifier(hex_pointer,cur_size)
                  print("\n","Free type(free) Atom Details are:")
                  dprint(free)
              elif(cur_atom=="mdat"):
                  hex_pointer=mdat_classifier(hex_pointer,cur_size)
                  print("\n","Media data(mdat) Atom Details are:")
                  dprint(mdat)
              cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="moov"):  
              origin_pointer=moov_classifier(hex_pointer,cur_size)
              hex_pointer=hex_pointer+16
              print("\n","Movie type(moov) Atom Details are:")
              dprint(moov)
        cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="mvhd"):  
              hex_pointer=mvhd_classifier(hex_pointer,cur_size)
              print("\n","Moovie header(mvhd) Atom Details are:")
              dprint(mvhd)
        cur_size, cur_atom = integrity_checker(hex_pointer)
        while(cur_atom!="trak"):
          hex_pointer+=cur_size*2
          cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="trak"):  
              origin_pointer=trak_classifier(hex_pointer,cur_size)
              print("\n","Track type (trak) Atom Details are:")
              dprint(trak)
              hex_pointer+=16
        cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="tkhd"):  
              hex_pointer=tkhd_classifier(hex_pointer,cur_size)
              print("\n","Track header (tkhd) Atom Details are:")
              dprint(tkhd)
        cur_size, cur_atom = integrity_checker(hex_pointer)
        while(cur_atom!="mdia"):
          hex_pointer+=cur_size*2
          cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="mdia"):       
           origin_pointer=mdia_classifier(hex_pointer,cur_size)
           print("\n","Movie Media (mdia) Atom Details are:")
           dprint(mdia)
           hex_pointer+=16
        cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="mdhd"):       
           hex_pointer=mdhd_classifier(hex_pointer,cur_size)
           print("\n","Movie Media Header(mdhd) Atom Details are:")
           dprint(mdhd)
        cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="hdlr"):       
           hex_pointer=hdlr_classifier(hex_pointer,cur_size)
           print("\n","Handler Description (hdlr) Atom Details are:")
           dprint(hdlr)
        cur_size, cur_atom = integrity_checker(hex_pointer)
        while(cur_atom!="minf"):
          hex_pointer+=cur_size*2
          cur_size, cur_atom = integrity_checker(hex_pointer)
        if(cur_atom=="minf"):
           original_pointer=minf_classifier(hex_pointer,cur_size)
           print("\n","Media Information (minf) Atom Details are:")
           dprint(minf)
           hex_pointer+=16
        cur_size, cur_atom = integrity_checker(hex_pointer)  
        if(cur_atom=="smhd"):
           hex_pointer=smhd_classifier(hex_pointer,cur_size)
           print("\n","Sound Media Header (smhd) Atom Details are:")
           dprint(smhd)
        if(cur_atom=="vmhd"):
           hex_pointer=vmhd_classifier(hex_pointer,cur_size)
           print("\n","Video Media Header (vmhd) Atom Details are:")
           dprint(vmhd)
        cur_size, cur_atom = integrity_checker(hex_pointer)  
        if(cur_atom=="dinf"):
           original_pointer=dinf_classifier(hex_pointer,cur_size)
           hex_pointer+=16
           print("\n","Data information (dinf) Atom Details are:")
           dprint(dinf)
        cur_size, cur_atom = integrity_checker(hex_pointer)  
        if(cur_atom=="dref"):
           hex_pointer=dref_classifier(hex_pointer,cur_size)
           # hex_pointer+=16
           # Dets of dref and url atoms are printed in the classifier due to an issue:
           # The last attribute of dref is data references which is a compilation of URL atoms
        cur_size, cur_atom = integrity_checker(hex_pointer) 
        if(cur_atom=="stbl"):
           tempo=""
           for j in range(hex_pointer,hex_pointer+8):
             tempo+=data[j]
           stbl['Size']=bigEnd(tempo)
           print("\nSample Table (stbl) details:");
           dprint(stbl)
           hex_pointer+=16
        cnt=0
        cur_size,cur_atom=integrity_checker(hex_pointer)
        while(cur_atom == 'stsd' or cur_atom=='stsc' or cur_atom == 'stts' or cur_atom == 'stss' 
              or cur_atom == 'stsz' or cur_atom=='stco' or cur_atom=='ctts' or cur_atom=='sdtp'
              or cur_atom == 'stps' or cur_atom=='cslg'):
             if(cnt>0):
                cur_size,cur_atom=integrity_checker(hex_pointer)
             cnt+=1
             hex_pointer=sample_atom_classifier(cur_atom,hex_pointer,cur_size)

        #  Work on stps atom now    
          # stsd done  
          # stts code diverted to sample atom classifier
          # stss code diverted to sample atom classifier 
          # stsc atom diverted to sample atom classifer
          # stsz atom diverted to sample atom classifer
          # stco atom diverted to sample atom classifer
          # ctts atom done
          # stsd stom done
          # stps atom done
          # cslg atom done

    
          
        #   # The upcoming track should deal with sound track



        #   cur_atom="stco"
        #   count=0
        #   while(cur_atom!='udta'):
        #     tempo=""
        #     for i in range(moov_pointer,moov_pointer+8):
        #       tempo+=data[i]
        #     temp_size=bigEnd(tempo)
        #     # print(temp_size)
        #     tempo=""
        #     for i in range(moov_pointer+8,moov_pointer+16):
        #       tempo+=data[i]
        #     temp_atom=hex_to_ascii(tempo)
        #     cur_atom=temp_atom
        #     # print(cur_atom)
        #     if(cur_atom!='udta'):
        #       moov_pointer+=(temp_size*2)
        #       print("\nAtom Missed!!!!")
        #       print("Atom missed :" , cur_atom,"\n", "Size is : ",temp_size)
          
          # cur_atom = "udta"
          # cur_pointer=moov_pointer
          # udta['Size'] = temp_size
          # tempo=""
          # for j in range(moov_pointer+16,moov_pointer+18):
          #   tempo+=data[j]
          # udta['Version'] = tempo
          # tempo=""
          # for j in range(moov_pointer+18,moov_pointer+24):
          #   tempo+=data[j]
          # udta['Flags'] = tempo
          
          # flag_pointer = moov_pointer+24
          # moov_pointer=cur_pointer+(udta['Size']*2)
          # tempo=""
          # for f in range(flag_pointer,moov_pointer):
          #   tempo+=data[f]
          # udta['User_Data_List'] = tempo
          # print("\n User Data (udta)atom  details:")
          # dprint(udta)
          # #udta atom done

        print("\n(updated size is: " , cur_size, ")\n")
        block_count+=1
        hex_pointer=cur_size*2
except:
  print("\nSize of the file is : " , cur_size , "bytes")
  print("Number of blocks in video :" , block_count , "blocks")
  pass
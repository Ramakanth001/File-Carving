# Atom classification - 1.1
# Implementation using functional programming
# Inclusion of Sample Atoms Classifier
# inclusion of Intergrity checker

from IntegrityChecker import integrity_checker
from SupportFunctions import litEnd, bigEnd, hex_to_ascii, dprint
from HexData import data
from AtomDictionaries import ftyp, free, mdat, moov, mvhd, trak, tkhd, mdia, mdhd, hdlr, minf, smhd, vmhd, dinf, dref, url, stbl, stsd, stts, stss, stsc, stsz, stco, ctts, sdtp, stps, cslg, udta
from Classifiers import ftyp_classifier,free_classifier,mdat_classifier,moov_classifier,mvhd_classifier,trak_classifier,tkhd_classifier,mdia_classifier,mdhd_classifier,hdlr_classifier,minf_classifier,vmhd_classifier,smhd_classifier,dinf_classifier,dref_classifier,sample_atom_classifier

# In FPRINT call DPRINT and write that into file so that data is in the foprm of dictionary in files
myf = open('OutputSamples/output.txt', 'w')
myf.write("FILE CONTENT:\n")
# myf.write(my_file_data)

block_count = 0
file_size = 0
block_size_H = []
block_size_D = []
block_type = []
block_sub_type = []
cur_size = 0
temp = ""
hex_pointer = 0
moov_pointer = 0

def initial_chunk():
    initial_size = data[:8]
    block_size_H.append(initial_size)
    initial_size_dec = litEnd(initial_size)
    block_size_D.append(initial_size_dec)
    print(initial_size, "   |  ", initial_size_dec)
    block_count += 1


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

try:
    cur_size, cur_atom = integrity_checker(hex_pointer)
    print(cur_size, cur_atom)
    # while(data[hex_pointer]!=''):
    while (cur_atom == "ftyp" or cur_atom == "free" or cur_atom == "mdat"):
        if (cur_atom == "ftyp"):
            hex_pointer = ftyp_classifier(hex_pointer, cur_size)
            print("\n", "File type(ftyp) Atom Details are:")
            dprint(ftyp)
        elif (cur_atom == "free"):
            hex_pointer = free_classifier(hex_pointer, cur_size)
            print("\n", "Free type(free) Atom Details are:")
            dprint(free)
        elif (cur_atom == "mdat"):
            hex_pointer = mdat_classifier(hex_pointer, cur_size)
            print("\n", "Media data(mdat) Atom Details are:")
            dprint(mdat)
        cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "moov"):
        origin_pointer = moov_classifier(hex_pointer, cur_size)
        hex_pointer = hex_pointer+16
        print("\n", "Movie type(moov) Atom Details are:")
        dprint(moov)
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "mvhd"):
        hex_pointer = mvhd_classifier(hex_pointer, cur_size)
        print("\n", "Moovie header(mvhd) Atom Details are:")
        dprint(mvhd)
    cur_size, cur_atom = integrity_checker(hex_pointer)
    while (cur_atom != "trak"):
        hex_pointer += cur_size*2
        cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "trak"):
        origin_pointer = trak_classifier(hex_pointer, cur_size)
        print("\n", "Track type (trak) Atom Details are:")
        dprint(trak)
        hex_pointer += 16
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "tkhd"):
        hex_pointer = tkhd_classifier(hex_pointer, cur_size)
        print("\n", "Track header (tkhd) Atom Details are:")
        dprint(tkhd)
    cur_size, cur_atom = integrity_checker(hex_pointer)
    while (cur_atom != "mdia"):
        hex_pointer += cur_size*2
        cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "mdia"):
        origin_pointer = mdia_classifier(hex_pointer, cur_size)
        print("\n", "Movie Media (mdia) Atom Details are:")
        dprint(mdia)
        hex_pointer += 16
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "mdhd"):
        hex_pointer = mdhd_classifier(hex_pointer, cur_size)
        print("\n", "Movie Media Header(mdhd) Atom Details are:")
        dprint(mdhd)
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "hdlr"):
        hex_pointer = hdlr_classifier(hex_pointer, cur_size)
        print("\n", "Handler Description (hdlr) Atom Details are:")
        dprint(hdlr)
    cur_size, cur_atom = integrity_checker(hex_pointer)
    while (cur_atom != "minf"):
        hex_pointer += cur_size*2
        cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "minf"):
        original_pointer = minf_classifier(hex_pointer, cur_size)
        print("\n", "Media Information (minf) Atom Details are:")
        dprint(minf)
        hex_pointer += 16
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "smhd"):
        hex_pointer = smhd_classifier(hex_pointer, cur_size)
        print("\n", "Sound Media Header (smhd) Atom Details are:")
        dprint(smhd)
    if (cur_atom == "vmhd"):
        hex_pointer = vmhd_classifier(hex_pointer, cur_size)
        print("\n", "Video Media Header (vmhd) Atom Details are:")
        dprint(vmhd)
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "dinf"):
        original_pointer = dinf_classifier(hex_pointer, cur_size)
        hex_pointer += 16
        print("\n", "Data information (dinf) Atom Details are:")
        dprint(dinf)
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "dref"):
        hex_pointer = dref_classifier(hex_pointer, cur_size)
        # hex_pointer+=16
        # Dets of dref and url atoms are printed in the classifier due to an issue:
        # The last attribute of dref is data references which is a compilation of URL atoms
    cur_size, cur_atom = integrity_checker(hex_pointer)
    if (cur_atom == "stbl"):
        tempo = ""
        for j in range(hex_pointer, hex_pointer+8):
            tempo += data[j]
        stbl['Size'] = bigEnd(tempo)
        print("\nSample Table (stbl) details:")
        dprint(stbl)
        hex_pointer += 16
    cur_size, cur_atom = integrity_checker(hex_pointer)
    while (cur_atom == 'stsd' or cur_atom == 'stsc' or cur_atom == 'stts' or cur_atom == 'stss'
           or cur_atom == 'stsz' or cur_atom == 'stco' or cur_atom == 'ctts' or cur_atom == 'sdtp'
           or cur_atom == 'stps' or cur_atom == 'cslg'):
            
        hex_pointer = sample_atom_classifier(cur_atom, hex_pointer, cur_size)
        cur_size, cur_atom = integrity_checker(hex_pointer)

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

    print("\n(updated size is: ", cur_size, ")\n")
    block_count += 1
    hex_pointer = cur_size*2
except:
    print("\nSize of the file is : ", cur_size, "bytes")
    print("Number of blocks in video :", block_count, "blocks")
    pass

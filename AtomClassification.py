# Atom classification - 1.1
# Implementation using functional programming
# Inclusion of Sample Atoms Classifier
# inclusion of Intergrity checker

from IntegrityChecker import integrity_checker
from SupportFunctions import litEnd, bigEnd, hex_to_ascii, dprint
from HexData import data
from AtomDictionaries import ftyp, free, mdat, moov, mvhd, trak, tkhd, mdia, mdhd, hdlr, minf, smhd, vmhd, dinf, dref, url, stbl, stsd, stts, stss, stsc, stsz, stco, ctts, sdtp, stps, cslg, udta
from Classifiers import ftyp_classifier,free_classifier,mdat_classifier,moov_classifier,mvhd_classifier,trak_classifier,tkhd_classifier,mdia_classifier,mdhd_classifier,hdlr_classifier,minf_classifier,vmhd_classifier,smhd_classifier,dinf_classifier,dref_classifier,sample_atom_classifier, udta_classifier

hex_pointer=0
block_count=0
try:
    cur_size, cur_atom = integrity_checker(hex_pointer)
    print(cur_size, cur_atom)
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
    
    if(cur_atom=='udta'):
           hex_pointer=udta_classifier(cur_atom,hex_pointer,cur_size)
           print("\n","User Data (udta) Atom Details are:")
           dprint(udta)
           #   # The upcoming track should deal with sound track
    while(cur_atom!="trak"):
        hex_pointer+=cur_size*2
        cur_size, cur_atom = integrity_checker(hex_pointer)
        
    #   # The upcoming track should deal with sound_track or the video_track which ever didn't occur yet
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
    cur_size,cur_atom=integrity_checker(hex_pointer)
    while(cur_atom == 'stsd' or cur_atom=='stsc' or cur_atom == 'stts' or cur_atom == 'stss' 
            or cur_atom == 'stsz' or cur_atom=='stco' or cur_atom=='ctts' or cur_atom=='sdtp'
            or cur_atom == 'stps' or cur_atom=='cslg'): 
            hex_pointer=sample_atom_classifier(cur_atom,hex_pointer,cur_size)
            cur_size,cur_atom=integrity_checker(hex_pointer)
            print(cur_size,cur_atom,hex_pointer)
    print(cur_atom)

    if(cur_atom=='udta'):
           hex_pointer=udta_classifier(cur_atom,hex_pointer,cur_size)
           print("\n","User Data (udta) Atom Details are:")
           dprint(udta)

    print("\n(updated size is: ", cur_size, ")\n")
    block_count += 1
    hex_pointer = cur_size*2
    print(hex)
except:
    print("\nSize of the file is : ", cur_size, "bytes")
    print("Number of blocks in video :", block_count, "blocks")
    pass

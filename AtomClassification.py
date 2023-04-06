# Atom classification - 1.1
# Implementation using functional programming
# Inclusion of Sample Atoms Classifier
# inclusion of Intergrity checker
from BlockClassification import ClassifyBlock
from IntegrityChecker import integrity_checker
from SupportFunctions import bigEnd, dprint
from HexData import data
from AtomDictionaries import ftyp, free, mdat, moov, mvhd, trak, tkhd, mdia, mdhd, hdlr, minf, smhd, vmhd, dinf, dref, url, stbl, stsd, stts, stss, stsc, stsz, stco, ctts, sdtp, stps, cslg, udta, sgpd, sbgp, edts, elst, iods
from Classifiers import ftyp_classifier, udta_classifier, free_classifier, mdat_classifier, moov_classifier, mvhd_classifier, trak_classifier, tkhd_classifier, mdia_classifier, mdhd_classifier, hdlr_classifier, minf_classifier, vmhd_classifier, smhd_classifier, dinf_classifier, dref_classifier, sample_atom_classifier, elst_classifier, iods_classifier
# The above imported classifier functions 

d={'ftyp':ftyp, 'free':free, 'mdat':mdat, 'moov':moov, 'mvhd':mvhd, 'trak':trak, 'tkhd':tkhd, 'mdia':mdia, 'mdhd':mdhd, 'hdlr':hdlr, 'minf':minf, 'smhd':smhd, 'vmhd':vmhd, 'dinf':dinf, 'dref':dref, 'url':url, 'stbl':stbl, 'stsd':stsd, 'stts':stts, 'stss':stss, 'stsc':stsc, 'stsz':stsz, 'stco':stco, 'ctts':ctts, 'sdtp':sdtp, 'stps':stps, 'cslg':cslg, 'udta':udta, 'sgpd':sgpd, 'sbgp' : sbgp, 'elst':elst, 'iods':iods}
MissedAtoms=set()        
try:
    file_size = ClassifyBlock()
    hex_pointer = 0
    origin_pointer = 0
    while (hex_pointer < (file_size*2)):
        cur_size, cur_atom = integrity_checker(hex_pointer)     
        if (cur_atom == "moov" or cur_atom == "trak" or cur_atom == "mdia" or cur_atom=="minf" or cur_atom=="dinf" ):
            origin_pointer = eval(cur_atom+'_classifier')(hex_pointer, cur_size)
            hex_pointer += 16
            print("\n", cur_atom+" Atom Details are:")
            dprint(d[cur_atom])
        elif (cur_atom == "stbl"):
            tempo = ""
            for j in range(hex_pointer, hex_pointer+8):
                tempo += data[j]
            stbl['Size'] = bigEnd(tempo)
            print("\nSample Table (stbl) details:")
            dprint(stbl)
            hex_pointer += 16
        elif (cur_atom == "edts"):
            tempo = ""
            for j in range(hex_pointer, hex_pointer+8):
                tempo += data[j]
            edts['Size'] = bigEnd(tempo)
            print("\n Edit Samples (edts) details:")
            dprint(edts)
            hex_pointer += 16
        elif (cur_atom == 'stsd' or cur_atom == 'stsc' or cur_atom == 'stts' or cur_atom == 'stss'
            or cur_atom == 'stsz' or cur_atom == 'stco' or cur_atom == 'ctts' or cur_atom == 'sdtp'
            or cur_atom == 'stps' or cur_atom == 'cslg' or cur_atom == 'sgpd'or cur_atom == 'sbgp'):
            hex_pointer = sample_atom_classifier(cur_atom, hex_pointer, cur_size)
            print("\n", cur_atom+" Atom Details are:")
            dprint(d[cur_atom])
        elif (cur_atom =='udta' or cur_atom == 'elst' or cur_atom == 'iods'):
            hex_pointer=eval(cur_atom+'_classifier')(cur_atom,hex_pointer, cur_size)
            print("\n", cur_atom+" Atom Details are:")
            dprint(d[cur_atom])
        elif cur_atom in d.keys():
            hex_pointer = eval(cur_atom+'_classifier')(hex_pointer, cur_size)
            print("\n", cur_atom+" Atom Details are:")
            dprint(d[cur_atom])     
        else:
            MissedAtoms.add(cur_atom)
            hex_pointer += cur_size*2
    print("File size: ",file_size*2)
    print("Final hex pointer value ", hex_pointer)
    print("Atoms that are not classified are:",MissedAtoms)
except:
    pass
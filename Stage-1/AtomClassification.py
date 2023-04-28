# Atom classification - 1.1
# Implementation using functional programming
# Inclusion of Sample Atoms Classifier
# Inclusion of Intergrity checker
from IntegrityChecker import integrity_checker
from SupportFunctions import bigEnd, dprint,test,hex_to_ascii,convert_string_to_hex,convert_hex_to_datetime
from HexData import data
import os
from AtomDictionaries import ftyp, free, mdat, moov, mvhd, trak, tkhd, mdia, mdhd, hdlr, minf, smhd, vmhd, dinf, dref, url, stbl, stsd, stts, stss, stsc, stsz, stco, ctts, sdtp, stps, cslg, udta,edts, iods,sgpd,sbgp,elst
from UpdatedClassifiers import ftyp_classifier,iods_classifier, elst_classifier, udta_classifier, free_classifier, mdat_classifier, moov_classifier, mvhd_classifier, trak_classifier, tkhd_classifier, mdia_classifier, mdhd_classifier, hdlr_classifier, minf_classifier, vmhd_classifier, smhd_classifier, dinf_classifier, dref_classifier, sample_atom_classifier,elst_classifier, iods_classifier

d={'ftyp':ftyp, 'free':free, 'mdat':mdat, 'moov':moov, 'mvhd':mvhd, 'trak':trak, 'tkhd':tkhd, 'mdia':mdia, 'mdhd':mdhd, 'hdlr':hdlr, 'minf':minf, 'smhd':smhd, 'vmhd':vmhd, 'dinf':dinf, 'dref':dref, 'url':url, 'stbl':stbl, 'stsd':stsd, 'stts':stts, 'stss':stss, 'stsc':stsc, 'stsz':stsz, 'stco':stco, 'ctts':ctts, 'sdtp':sdtp, 'stps':stps, 'cslg':cslg, 'udta':udta, 'sgpd':sgpd, 'sbgp' : sbgp, 'elst':elst, 'iods':iods}
x = {'ftyp': '(File type)', 'free': 'Free type', 'mdat': 'Media Data', 'moov': 'Movie type', 'mvhd': 'Movie Header type', 'trak': 'Track type', 'tkhd': 'Track Header type ', 'mdia': 'Media type', 'mdhd': 'Media Header', 'hdlr': 'Handler Description', 'minf': 'Media Information', 'smhd': 'Sound Media Header', 'vmhd': 'Video Media Header', 'dinf': 'Data information',
     'dref': 'Data Reference', 'url': 'URL type', 'stbl': 'Sample Atom type', 'stsd': 'Sample Atom type', 'stts': 'Sample Atom type', 'stss': 'Sample Atom type', 'stsc': 'Sample Atom type', 'stsz': 'Sample Atom type', 'stco': 'Sample Atom type', 'ctts': 'Sample Atom type', 'sdtp': 'Sample Atom type', 'stps': 'Sample Atom type', 'cslg': 'Sample Atom type', 'udta': 'User Data','sgpd':'sgpd', 'sbgp' : 'sbgp', 'elst':'elst', 'iods':'iods'}
l=[]
missing_atoms={}
track_counter=1

def WriteToAFile(name="",d={},booll=False,listt=[],missing_atoms={}):
    global track_counter
    myf = open('Stage-1\OutputSamples/output.txt', 'a')
    if booll==False:
        if name=='udta':
            myf.write("\n"+"\nNext Up We Have User Data Atoms:\n")
        if track_counter==2 and name=='trak':
            myf.write("\n"+"\nNext Up We Have Audio Track Atoms: \n")
        if track_counter==1 and name=='trak':
            myf.write("\n"+"\nNext Up We Have Video Track Atoms: \n")
        if name == 'trak':
            track_counter+=1
        myf.write("\n"+"\nClassified Atom is : "+str(name)+"------------------------------\n")
        myf.write('Size : '+str(d['Size'])+"\n")
        for attribute, value in d.items():
            try:
                if len(str(value)) > 1000:
                    myf.write(str(attribute)+" : "+str(value[1050])+"\n")
                else:
                    myf.write(str(attribute)+" : "+str(value)+"\n")
            except:
                pass
    counter=1
    if booll==True:
        myf.write("\n"+"\nList Of Atoms : ------------------------------\n")
        for item in listt:
             myf.write(str(counter)+". "+str(item)+"\n")
             counter+=1
        myf.write("\n"+"\nList Of Missing Atoms : ------------------------------\n")
        if len(missing_atoms)==0:
            myf.write("None")
        for k,v in missing_atoms.items():
            myf.write(str(k)+":"+str(v)+"\n")
    myf.close()

def MainAtomClassification():
    try:
        # file_size=ClassifyBlock()
        # file_size = os.path.getsize(r'Stage-3\\RedundancyPartialFileSamples\\CorruptedPartialFile1.txt')
        file_size = os.path.getsize(r'VideoSamples\Sample-2-HR.mp4')
        hex_pointer = 0
        origin_pointer = 0
        while (hex_pointer < (file_size)):
            cur_size, cur_atom = integrity_checker(hex_pointer,data)
            l.append(cur_atom)
            if (cur_atom == "moov" or cur_atom == "trak" or cur_atom == "mdia" or cur_atom == "minf" or cur_atom == "dinf"):
                origin_pointer,g = eval(
                    cur_atom+'_classifier')(hex_pointer,data,True)
                hex_pointer += 16
                print(cur_atom.upper(
                )+"("+x[cur_atom]+")"+" Atom Details are:-------------------------------------")
                # dprint(d[cur_atom])
                dprint(g)
                WriteToAFile(name=cur_atom,d= d[cur_atom])
            elif (cur_atom == "stbl"):
                tempo = ""
                for j in range(hex_pointer, hex_pointer+8):
                    tempo += data[j]
                stbl['Size'] = bigEnd(tempo)
                print("\nSample Table (stbl) details:-------------------------------------")
                dprint(stbl)
                WriteToAFile(name=cur_atom,d= d[cur_atom])
                hex_pointer += 16
            elif (cur_atom == "edts"):
                tempo = ""
                for j in range(hex_pointer, hex_pointer+8):
                    tempo += data[j]
                edts['Size'] = bigEnd(tempo)
                print("\n Edit Samples (edts) details:-------------------------------------")
                dprint(edts)
                hex_pointer += 16
            elif (cur_atom == 'stsd' or cur_atom == 'stsc' or cur_atom == 'stts' or cur_atom == 'stss'
                or cur_atom == 'stsz' or cur_atom == 'stco' or cur_atom == 'ctts' or cur_atom == 'sdtp'
                or cur_atom == 'stps' or cur_atom == 'cslg' or cur_atom == 'sgpd'or cur_atom == 'sbgp'):
                hex_pointer,g = sample_atom_classifier(
                    cur_atom, hex_pointer, data,True)
                print(cur_atom.upper(
                )+"("+x[cur_atom]+")"+" Atom Details are:-------------------------------------")
                # dprint(d[cur_atom])
                dprint(g)
                WriteToAFile(name=cur_atom,d= d[cur_atom])
            elif cur_atom == 'udta' or cur_atom == 'elst' or cur_atom == 'iods' :
                hex_pointer,g = eval(
                    cur_atom+'_classifier')( hex_pointer, data,True)
                print(cur_atom.upper(
                )+"("+x[cur_atom]+")"+" Atom Details are:-------------------------------------")
                dprint(g)
                WriteToAFile(name=cur_atom,d= d[cur_atom])
            elif cur_atom in d.keys():
                    hex_pointer,g = eval(cur_atom+'_classifier')(hex_pointer,data,True)
                    if cur_atom!='dref':
                        print(cur_atom.upper(
                        )+"("+x[cur_atom]+")"+" Atom Details are:-------------------------------------")
                        dprint(g)
                    WriteToAFile(name=cur_atom,d= d[cur_atom])
            else:
                hex_pointer += cur_size*2
                missing_atoms[cur_atom]=cur_size
        print("File size: ", file_size)
        print("Final hex pointer value: ", hex_pointer//2)
        print("\nAtoms Encountered:")
        print(l)
        WriteToAFile(booll=True,listt=l,missing_atoms=missing_atoms)
        print("\nMissing Atoms:")
        print(missing_atoms)
        print('\nAtom Redundancy:')
        from UpdatedClassifiers import Creation_Time,Modification_Time,Matrix
        print('Creation Time:')
        print(Creation_Time)
        print('Modification Time:')
        print(Modification_Time)
        print('Matrix:')
        print(Matrix)   
        return (Creation_Time,Modification_Time,Matrix) 
    except:
        pass
MainAtomClassification()
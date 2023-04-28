atoms = ['ftyp','edts', 'free', 'mdat', 'moov', 'mvhd', 'trak', 'tkhd', 'mdia', 'mdhd', 'hdlr', 'minf', 'smhd', 'vmhd', 'dinf', 'dref', 'url',
     'stbl', 'stsd', 'stts', 'stss', 'stsc', 'stsz', 'stco', 'ctts', 'sdtp', 'stps', 'cslg', 'udta', 'sgpd', 'sbgp', 'elst', 'iods']
major_brand_list=['isom','iso2','avc1','mp41']
import sys
sys.path.append(r'C:\\Users\Suddala Kavyasree\Desktop\\File Carving\\Stage-1\\')
from UpdatedClassifiers import ftyp_classifier,stbl_classifier, edts_classifier, udta_classifier, free_classifier, mdat_classifier, moov_classifier, mvhd_classifier, trak_classifier, tkhd_classifier, mdia_classifier, mdhd_classifier, hdlr_classifier, minf_classifier, vmhd_classifier, smhd_classifier, dinf_classifier, dref_classifier, sample_atom_classifier, elst_classifier, iods_classifier

import os
directory_path = r"C:\\Users\Suddala Kavyasree\Desktop\\File Carving\\Stage-3\\FileSamples"
file_list = os.listdir(directory_path)
# print(file_list)

def Recover(hex_string):
    ascii_string = bytes.fromhex(hex_string).decode('latin-1')
    print('\nAscii String is: '+ascii_string)
    ss=ascii_string
    atoms_present=[]
    partial_atoms_present=[]
    for atom in atoms:
        if atom in ascii_string:
            atoms_present.append(atom)
            ss=ss.replace(atom,'')
    print('\nFull Atoms present in the given fragment are: ',atoms_present)
    for atom in atoms:
        if atom not in atoms_present:
            l=[atom[i:i+2] for i in range(len(atom)-1)]
            for i in l:
                if i in ss:
                    if atom not in partial_atoms_present:
                        partial_atoms_present.append(atom)
    if len(partial_atoms_present)>0:
        print('\nAtoms(Possibility) present in the given fragment are: ',partial_atoms_present)
        
    if 'ftyp' in ascii_string:
        print('\nFTYP atom found!! Size of ftyp atom is 32 bytes and recovered fragment is '+('00000020'+hex_string))
    
    if 'free' in ascii_string:
        print('\nFREE atom found!! Size of free atom is 8 bytes and recovered fragment is '+('00000008'+hex_string))
    
    for i in major_brand_list:
        if i in ascii_string and 'ftyp' not in atoms_present and 'ftyp' not in partial_atoms_present:
            print('\nThere is a possibility of occurence of ftyp as we encountered '+i)
            break
    found=False
    for atom in partial_atoms_present+atoms_present:
        if atom == ascii_string[-4:]:
            found=True
            print('\nThere is a possibility of occurence of atom '+atom.upper()+' after all atoms in current file fragment\n')
            break
    if found==False:
        for atom in partial_atoms_present+atoms_present:  
            l=[atom[i:i+2] for i in range(len(atom)-1)]
            for i in l:
                if i in ascii_string[-4:]:
                    print('\nThere is a possibility of occurence of atom '+atom.upper()+' after all atoms in current file fragment\n')

    for cur_atom in atoms_present:
        if cur_atom=='url':
            continue
        atom_pos = ascii_string.find(str(cur_atom))
        if (cur_atom == 'stsd' or cur_atom == 'stsc' or cur_atom == 'stts' or cur_atom == 'stss'
                or cur_atom == 'stsz' or cur_atom == 'stco' or cur_atom == 'ctts' or cur_atom == 'sdtp'
                or cur_atom == 'stps' or cur_atom == 'cslg' or cur_atom == 'sgpd'or cur_atom == 'sbgp'):
            pointerr,dictt = sample_atom_classifier(cur_atom,0,hex_string[(atom_pos*2)+8:], False)
        else:
            pointerr,dictt = eval(str(cur_atom)+'_classifier')(0,hex_string[(atom_pos*2)+8:], False)
        print('\nAttributes of atom '+cur_atom.upper()+":\n")
        for k,v in dictt.items():
            if v is not None and len(str(v))!=0:
                print(k+': '+str(v))
        
s=input('Enter filename:')
with open(r'C:\\Users\Suddala Kavyasree\Desktop\\File Carving\\Stage-3\\FileSamples\\'+s+'.txt','r') as f:
    data=str((f.read()))
    hex_string=data.replace(' ','').replace('\n','')
    print('\nConsidered File fragment ('+s+'): '+hex_string)
    Recover(hex_string)
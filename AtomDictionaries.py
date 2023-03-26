ftyp = {
     'Size':None, 
     'Type':'ftyp',
     'Major_Brand':None,
     'Minor_Version' : None,
     'Compatible_Brands' : []
}
    
free = {
    'Size':None,
     'Type':'free',
    'Free Space' :None
}
mdat = {
    'Size':None,
     'Type':'mdat'
}
moov = {
    'Size':None,
     'Type':'moov'
}
mvhd = {
     'Size':None,
     'Type':'mvhd',
     'Version':None, 
     'Flags':None,
     'Creation_Time':None,
     'Modification_Time':None,
     'Time_Scale':None,
     'Duration':None,
     'Preferred_Rate':None,
     'Preferred_Volume':None,
     'Reserved':None,
     'Matrix':None,
     'Predefines':None,
     'Next_Track_ID':None
}
trak= {
    'Size':None,
     'Type':'trak'
}
tkhd = {
     'Size':None,
     'Type':'tkhd',
     'Version':None, 
     'Flags':None,
     'Creation_Time':None,
     'Modification_Time':None,
     'Track_ID' : None, 
     'Reserved': None,
     'Duration': None,
     'Reserved_2': None,
     'Layer':None,
     'Alternative_Group': None,
     'Volume': None,
     'Reserved_3': None,
     'Matrix_Structure': None,
     'Track_Width': None,
     'Track_Height': None
}
mdia= {
    'Size':None,
     'Type':'mdia'
}

mdhd = {
     'Size':None,
     'Type':'mdhd',
     'Version':None, 
     'Flags':None,
     'Creation_Time':None, 
     'Modification_Time':None,
     'Time_Scale':None,
     'Duration':None,
     'Language':None,
     'Predefined':None
}
hdlr = {
     'Size':None,
     'Type':'hdlr',
     'Version':None, 
     'Flags':None,
     'Component_Type':None,
     'Component_Subtype':None,
     'Component_Manufacturer':None,
     'Component_Flags':None,
     'Component_Flags_Masks': None,
     'Component_Name':None,
} 
minf = {
    'Size':None,
     'Type':'minf'
}
smhd = {
    'Size':None,
     'Type':'smhd',
     'Version':None, 
     'Flags':None,
     'Balance':None,
     'Reserved':None
}
vmhd = {
    'Size':None,
     'Type':'vmhd',
     'Version':None, 
     'Flags':None,
     'Graphics_Mode':None,
     'Opcolor':None
}
dinf = {
    'Size':None,
     'Type':'dinf'
}
dref = {
    'Size':None,
     'Type':'dref',
     'Version' : None,
     'Flags' : None,
     'Number_of_Entries' : None,
     'Data_References' : None
}
url = {
     'Size':None,
     'Type':'url ',
     'Version' : None,
     'Flags' : None
}
stbl = {
    'Size':None,
     'Type':'stbl'
}
stsd = {
    'Size':None,
     'Type':'stsd',
     'Version':None, 
     'Flags':None,
     'Number_of_Entries' : None,
     'Sample_Description_Size':None,
     'Data_Format':None,
     'Reserved1':None,
     'Data_Reference_Index':None,
     'Predefines':None,
     'Reserved2':None,
     'Media_Width':None,
     'Media_Height':None,
     'Horizontal_Resolution':None,
     'Vertical_Resolution':None,
     'Reserved3':None,
     'Frame_Count':None

}
stts= {
    'Size':None,
     'Type':'stts',
     'Version':None, 
     'Flags':None,
     'Number_of_Entries' : None,
     'Sample_Duration' : None,
     'Sample_Count' : None
}
stss = {
    'Size':None,
     'Type':'stss',
     'Version':None, 
     'Flags':None,
     'Number_of_Entries' : None,
     'Sync-sample-table' : None # stated wrong in cirramon systems
}
stsc = {
    'Size':None,
     'Type':'stsc',
     'Version':None, 
     'Flags':None,
     'Number_of_Entries' : None,
     'Sample-to-Chunk_Table': None
}
stsz = {
    'Size':None,
     'Type':'stsz',
     'Version':None, 
     'Flags':None,
     'Sample_Size':None,
     'Number_of_Entries' : None,
     'Sample-to-Size_Table': None
     
}
stco={
     'Size':None,
     'Type':'stco',
     'Version':None, 
     'Flags':None,
     'Number_of_Entries' : None,
     'Chunk_offset_table' : None
}
ctts = {
    'Size':None,
     'Type':'ctts',
     'Version':None, 
     'Flags':None,
     'Entry-Count' : None,
     'Composition-offset-table': None
}
sdtp = {
     'Size':None,
     'Type':'sdtp',
     'Version':None, 
     'Flags':None,
     'Sample-Dependency-Flags-Table': None
}

stps = {
    'Size':None,
     'Type':'stps',
     'Version':None, 
     'Flags':None,
     'Entry-Count' : None,
     'Partial-Sync-Sample-Table': None
}
cslg = {
    'Size':None,
     'Type':'stps',
     'Version':None, 
     'Flags':None,
     'CompositionOffsetToDisplayOffset': None,
     'LeastDisplayOffset':None,
     'DisplayStartTime':None,
     'DispalyEndTime':None
}
udta={
    'Size':None,
     'Type':'udta',
     'Version':None, 
     'Flags':None,
     'User_Data_List' : None
}
# Below are atom dicts
ftyp = {
     'Size':None, # 4-bytes
     'Type':'ftyp', # 4-bytes
     'Major_Brand':None, # 4-bytes
     'Minor_Version' : None, # 4-bytes
     'Compatible_Brands' : [], # Variable size
}
    
free = {
    'Size':None, # 4-bytes
     'Type':'free', # 4-bytes
}
mdat = {
    'Size':None, # 4-bytes
     'Type':'mdat' # 4-bytes
}
moov = {
    'Size':None, # 4-bytes
     'Type':'moov' # 4-bytes
}
mvhd = {
     'Size':None, # 4-bytes 
     'Type':'mvhd',# 4-bytes
     'Version':None,  # 1-byte
     'Flags':None, # 3-bytes
     'Creation_Time':None, # 4-bytes
     'Modification_Time':None, # 4-bytes
     'Time_Scale':None,# 4-bytes
     'Duration':None,# 4-bytes
     'Preferred_Rate':None, # 4-bytes
     'Preferred_Volume':None, # 2-bytes
     'Reserved':None, # 10-bytes
     'Matrix':None, # 36-bytes  
     'Preview_Time':None, # 4-bytes
     'Preview_Duration':None, # 4-bytes
     'Poster_Time':None, # 4-bytes
     'Selection_Time':None, # 4-bytes
     'Selection_Duration':None, # 4-bytes
     'Current_Time':None, # 4-bytes
     'Next_Track_ID':None # 4-bytes,
}
trak= {
    'Size':None, # 4-bytes
     'Type':'trak'# 4-bytes
}
tkhd = {
     'Size':None,# 4-bytes
     'Type':'tkhd',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None,# 3-bytes
     'Creation_Time':None, # 4-bytes
     'Modification_Time':None,# 4-bytes
     'Track_ID' : None, # 4-bytes
     'Reserved': None,# 4-bytes
     'Duration': None, # 4-bytes
     'Reserved_2': None,# 8-bytes
     'Layer':None, # 2-bytes
     'Alternative_Group': None, # 2-bytes
     'Volume': None, # 2-bytes
     'Reserved_3': None, # 2-bytes
     'Matrix_Structure': None, # 36-bytes
     'Track_Width': None, # 4-bytes
     'Track_Height': None # 4-bytes
}
mdia= {
    'Size':None, # 4-bytes
     'Type':'mdia' # 4-bytes
}

mdhd = {
     'Size':None, # 4-bytes
     'Type':'mdhd', # 4-bytes
     'Version':None,  # 1-byte
     'Flags':None,# 3-bytes
     'Creation_Time':None,  # 4-bytes
     'Modification_Time':None, # 4-bytes
     'Time_Scale':None, # 4-bytes
     'Duration':None, # 4-bytes
     'Language':None, # 2-bytes
     'Predefined':None # 2-bytes
}
hdlr = {
     'Size':None,# 4-bytes
     'Type':'hdlr',# 4-bytes
     'Version':None, # 1-byte 
     'Flags':None, # 3-bytes
     'Component_Type':None, # 4-bytes
     'Component_Subtype':None, # 4-bytes
     'Component_Manufacturer':None,# 4-bytes
     'Component_Flags':None,# 4-bytes
     'Component_Flags_Masks': None,# 4-bytes
     'Component_Name':None, #variable
} 
minf = {
    'Size':None, # 4-bytes
     'Type':'minf' # 4-bytes
}
smhd = {
    'Size':None, # 4-bytes
     'Type':'smhd', # 4-bytes
     'Version':None, # 1-byte 
     'Flags':None,# 3-bytes
     'Balance':None, # 2-bytes
     'Reserved':None # 2-bytes 
}
vmhd = {
    'Size':None, # 4-bytes
     'Type':'vmhd',# 4-bytes
     'Version':None, # 1-byte 
     'Flags':None,# 3-bytes
     'Graphics_Mode':None,# 2-bytes
     'Opcolor':None # 6-bytes
}
dinf = {
    'Size':None,# 4-bytes
     'Type':'dinf'# 4-bytes
}
dref = {
    'Size':None,# 4-bytes
     'Type':'dref',# 4-bytes
     'Version' : None,# 1-byte
     'Flags' : None,# 3-bytes
     'Number_of_Entries' : None,# 4-bytes
     'Data_References' : None # variable - url atoms
}
url = {
     'Size':None,# 4-bytes
     'Type':'url ',# 4-bytes
     'Version' : None,# 1-byte
     'Flags' : None # 3-bytes
}
stbl = {
    'Size':None,# 4-bytes
     'Type':'stbl'# 4-bytes
}
stsdd = {
    'Size':None,# 4-bytes
     'Type':'stsd',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Number_of_Entries' : None,# 4-bytes
     'Sample_Description_Size':None,# 4-bytes
     'Data_Format':None, # 4-bytes
     'Reserved1':None, # 6-bytes
     'Data_Reference_Index':None,# 4-bytes
     'Predefines':None, # 6-bytes
     'Reserved2':None, # 6-bytes
     'Media_Width':None, #2-bytes
     'Media_Height':None, #2-bytes
     'Horizontal_Resolution':None, #4-bytes
     'Vertical_Resolution':None, #4-bytes
     'Reserved3':None, #6-bytes
     'Frame_Count':None #2-bytes

}
stsd = {
    'Size':None,# 4-bytes
     'Type':'stsd',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Number_of_Entries' : None,# 4-bytes 1 or 2 or 3
     'Sample_Description_Size':None,# 4-bytes
     'Data_Format':None, # 4-bytes
     'version':None, #2-bytes
     'Revision_Level':None, #2-bytes
     'Vendor':None, #4-bytes
     'Temporal_Quality':None,#4-bytes
     'Spatial_Quality':None,#4-bytes
     'Media_Width':None, #2-bytes
     'Media_Height':None, #2-bytes
     'Horizontal_Resolution':None, #4-bytes
     'Vertical_Resolution':None, #4-bytes
     'DataSize':None,#4-bytes
     'Frame_Count':None, #2-bytes
     'compressorname':None, #varying n char-n bytes+1
     'bits_per_sample':None,#2-bytes
     'channelcount':None,#2-bytes
     'samplesize':None,#2-bytes
     'samplerate':None,#4-bytes
     'format_specific_data':None     
}
stts= {
    'Size':None,# 4-bytes
     'Type':'stts',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Number_of_Entries' : None,# 4-bytes
     'Sample_Duration' : None,# 4-bytes
     'Sample_Count' : None# 4-bytes
}
stss = {
    'Size':None,# 4-bytes
     'Type':'stss',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Number_of_Entries' : None,# 4-bytes
     'Sync-sample-table' : None # Variable-size # stated wrong in cirramon systems
}
stsc = {
    'Size':None,# 4-bytes
     'Type':'stsc',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Number_of_Entries' : None,# 4-bytes
     'Sample-to-Chunk_Table': None # Variable-size
}
stsz = {
    'Size':None,# 4-bytes
     'Type':'stsz',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Sample_Size':None,# 4-bytes
     'Number_of_Entries' : None,# 4-bytes
     'Sample-to-Size_Table': None # Variable-size
     
}
stco={
     'Size':None,# 4-bytes
     'Type':'stco',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Number_of_Entries' : None,# 4-bytes
     'Chunk_offset_table' : None# Variable-size
}
ctts = {
    'Size':None,# 4-bytes
     'Type':'ctts',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Entry-Count' : None,# 4-bytes
     'Composition-offset-table': None # Variable-size
}
sdtp = {
     'Size':None,# 4-bytes
     'Type':'sdtp',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Sample-Dependency-Flags-Table': None # Variable-size
}

stps = {
    'Size':None,# 4-bytes
     'Type':'stps',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'Entry-Count' : None, # 4-bytes
     'Partial-Sync-Sample-Table': None # Variable-size
}
cslg = {
    'Size':None,# 4-bytes
     'Type':'cslg',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None,# 3-bytes
     'CompositionOffsetToDisplayOffset': None,# 4-bytes
     'LeastDisplayOffset':None, # 4-bytes
     'DisplayStartTime':None, # 4-bytes
     'DispalyEndTime':None # 4-bytes
}
udta={
    'Size':None,# 4-bytes
     'Type':'udta',# 4-bytes
     'Version':None, # 1-byte
     'Flags':None,# 3-bytes
     'UserDataList' : None # 4-bytes
}
sgpd =  {
    'Size':None, # 4-bytes
     'Type':'sgpd', # 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'GroupingType':'roll', # 4-bytes - Generally set to 'roll'
     'DefaultLength':None, # 4-bytes
     'EntryCount':None, # 4-bytes
     'PayloadData':None #Variable
}
sbgp = {
    'Size':None, # 4-bytes
     'Type':'sbgp', # 4-bytes
     'Version':None, # 1-byte
     'Flags':None, # 3-bytes
     'GroupingType':'roll', # 4-bytes - Generally set to 'roll'
     'EntryCount':None, # 4-bytes
     'TableData':None # Variable  - Consists of SampleCount and GroupDescriptionIndex

}
iods= {
    'Size': None, # 4-bytes
     'Type': 'iods', # 4-bytes
     'Version': None, # 1-byte
     'Flags': None, # 3-bytes
     'OtherData' : None # Variable - Doesnt exists really we are just terminating this ways
}

edts = {
     'Size': None, # 4-bytes
     'Type': 'edts', # 4-bytes
}
#edts can contain elst
elst = {
     'Size': None, # 4-bytes
     'Type': 'elst', # 4-bytes
     'Version': None, # 1-byte
     'Flags': None, # 3-bytes
     'EntryCount': None, # 4-bytes
     'EditDuration' : None,  # 4-bytes( in global timescale units)
     'EditMediaTime' : None, # 4-bytes (in trak timescale units)
     'PlaybackSpeed' : None # 4-bytes
}

# Video File-Carving
Video file carving is a technique used in digital forensics to recover deleted or damaged video files from a storage deice like a disk. It involves analyzing the file system and/or the raw data on the storage device to locate fragments or whole blocks of data that may belong to a video file. The carved data is then reconstructed and extracted into a playable video file. It cane be a can be a useful technique in digital forensics, data recovery, and criminal investigations, as it can help to recover important evidence that might otherwise be lost. However, it can also be a time-consuming and complex process that requires specialized tools and expertise to perform accurately. The process of video file carving requires specialized software tools and a deep understanding of file system structures and data recovery techniques. Our project is an attempt to build a forensic tool that aids in video file carving. <br />
**The project is divided into _3 stages_:**

## STAGE-1 : 
> **Atom-Classification**

First stage attempts to identify the structure of the video file and attempts to classify the atom boxes in the video file as attributes of individual atoms and their values. Atoms are the lowesst structural units of a video file. We have a dictionary of atoms for classification and the video file will be parsed against it. When a video file is given as input, the video file is converted into hex, and that hex data consists of structural data, video meta data, and frame level data. We just classify the atoms, attributes in them and their values in this stage.<br />
**The below atoms can be classified by our tool:**

```
1. ftyp
2. free
3. mdat
4. moov
5. mvhd
6. trak
7. tkhd 
8. mdia
9. mdhd
10. hdlr
11. minf
12. smhd
13. vmhd
14. dinf
15. dref
16. url
17. stsd
18. stss
19. stts
20. stsc
21. stsz
22. stco
23. ctts
24. sdtp
25. stps
26. cslg
27. udta
28. sgpd
29. sbgp
30. iods
31. edts
32. elst
33. stbl
```

## STAGE-2 : 
> **Frame-Classification**

Stage-2 deals with identification and classification of frames. In video, a frame is a single still image that is displayed on the screen for a specific period of time before being replaced by the next frame. Each frame in a video contains information about the color and brightness values of each pixel in the image, as well as any other metadata that might be associated with the frame, such as the timecode or frame number. If we have enough information, we can identify and extract frames from the hex content we have. <br /> 
**Below techniques are used to extract key frames:**
```
1. *Frame-Interval Method (FIM)
2. *Blob Detection using a set of Detection Parameters (BDM)
3. *Absolute Mean Difference Method (AMD)
4. *Root Mean Square Method (RMS)
5. *Background Frame Subtraction Method (BFSM)
6. *Custom Frame Detection Method (CFDM)
7. *Optical Flow Frame Detection Method (OFFDM) -> *Horn-Schunck Algorithm is used*
 ```
 **NOTE: _(CFDM is adviced for a naive user)_**

## STAGE-3 : 
> **Partial-File-Carving**

Stage-3 deals with the redundant attributes present in the atoms classified and tracks them down with their corresponding values. If there is a corruption or missing values of the redundant attributes, then the most probable choice value (max count) is considered to be the final value and is assigned to the attributes in all atoms where the redundancy is found and a new corruption-free fragment is generated.It will also consider the structure-based evidence in order to come up with certain conclusions related to the considered partial file fragment. <br />
**Below ideas are used for partial file carving:**
```
1. Attribute Redundancy
2. Intergity Checker
3. Structural Evidences
```

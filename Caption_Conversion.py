# This file holds functions that convert a SRT file into a G-cloud compatible file with break statements

# For example the following in SRT:
# 1
# 00:00:02,100 --> 00:00:02,790
# Hello there.

# 2
# 00:00:02,800 --> 00:00:07,190
# My name is audio jack on the vice president of
# Is converted to:
# <speak> Hello there. <break time="10ms"/> My name is audio jack on the vice president of

def SRT_to_API(in_file):
    #params: in_file is the SRT file to convert
    #output: API string

    #Extract the files from the SRT file
    lines = extract_lines(in_file)
    #
    line = subtitle_split[0]
    # start with num\n start (space)-->(space) end time\n txt
    line = line.split(sep='\n') # [num,start (space)-->(space) end time,txt]
    x = line[1].split(sep=' --> ')
    line[0] = x[0]
    line[1] = x[1] #[start,end,txt]

print(line)

def extract_lines(in_file):
    #params: in_file (SRT)
    #output: list of strings, each string is one of the lines

    # line = 
    # 1
    # 00:00:02,100 --> 00:00:02,790
    # Hello there.
    SRT = open(in_file,'r')
    raw_subtitle = SRT.read()
    SRT.close() # get raw content
    subtitle_split = raw_subtitle.split(sep='\n\n')
    subtitle_split[0] = subtitle_split[0].replace('\ufeff','') # remove \ufeff from first line
    return subtitle_split


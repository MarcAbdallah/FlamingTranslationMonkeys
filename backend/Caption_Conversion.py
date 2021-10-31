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

def time_to_ms(time):
    layers = time.split(':')
    # print(layers)
    layers[2] = layers[2].replace(",", ".")  # ['xx' hours, 'xx' minutes, 'xx.xxx' seconds]
    ms = int((int(layers[0]) * 3600000) + (int(layers[1]) * 60000) + (float(layers[2]) * 1000))
    return ms

# TODO: Why is this only returning the first subtitle
def SRT_to_API(in_file):
    #params: in_file is the SRT file to convert
    #output: API string
    API_string = "" #"<speak> "
    #Extract the files from the SRT file
    subtitle_split = extract_lines(in_file)
    #[begin,endtime,txt]
    
    previous_end = 0
    for line in subtitle_split:
        # start with num\n start (space)-->(space) end time\n txt
        line = line.split(sep='\n')  # [num,start (space)-->(space) end time,txt]
        x = line[1].split(sep=' --> ')
        line[0] = x[0]
        line[1] = x[1] #[start,end,txt]
        line[0] = time_to_ms(line[0])
        line[1] = time_to_ms(line[1])
        API_string += "<break time=\"" + str(line[0] - previous_end) + "ms\"/> " + line[2] + " "
        previous_end = line[1]
    endtime = line[1]
    # API_string += "</speak>"
    return API_string,endtime


def extract_lines(in_file):
    #params: in_file (SRT)
    #output: list of strings, each string is one of the lines

    # line =
    # 1
    # 00:00:02,100 --> 00:00:02,790
    # Hello there.
    # this is a byte stream, so decode
    raw_subtitle = in_file.read().decode("utf-8")
    subtitle_split = raw_subtitle.split(sep='\r\n\r\n')
    subtitle_split[0] = subtitle_split[0].replace('\ufeff','') # remove \ufeff from first line
    return subtitle_split

def main():
    print(SRT_to_API("Adi.srt"))

if __name__ == "__main__":
    main()
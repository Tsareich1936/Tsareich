import glob
import os
import re
fist_num = 970
files = glob.glob("history/states/*.txt")
name_list = [os.path.basename(file) for file in files]
for i in name_list:
    
    name = i
    spilit_name = name.split("-")
    
    spilit_name[0] = int(spilit_name[0])
    if spilit_name[0] >= fist_num:
        print(i)
        print(spilit_name[0])
        future_num = spilit_name[0] + 35
        with open("history/states/"+i,mode="r")as f:
            data_lines = f.read()
        data_lines = data_lines.replace("\tid={}".format(str(spilit_name[0]-35)), "\tid={}".format(spilit_name[0]))
        data_lines = data_lines.replace("\tid = {}".format(str(spilit_name[0]-35)), "\tid={}".format(spilit_name[0]))
        data_lines = data_lines.replace("\tname=\"STATE_{}\"".format(str(spilit_name[0]-35)), "\tname=\"STATE_{}\"".format(spilit_name[0]))
        data_lines = data_lines.replace("\tname = \"STATE_{}\"".format(str(spilit_name[0]-35)), "\tname = \"STATE_{}\"".format(spilit_name[0]))
        print(data_lines)
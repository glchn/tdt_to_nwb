import sys
import numpy as np

from datetime import datetime
from dateutil.tz import tzlocal
from os import getcwd, path, listdir

from nwb_handler import *
from tdt import read_block

# global variables! change these as needed.
data_block = r'/mnt/c/Users/scsc7/Documents/Github/tdt_to_nwb/test'

# converts tdt files to nwb file
# params: string block_path is path to tdt folder
#         string nwb_file_name is name of nwb file you will write to
def convert():
    data = read_block(data_block)
    # print("\ndata:\n" + str(data))
    # print("\ninfo:\n"+ str(data.info))
    # print ('\nall stream stores: \n' + str(data.streams))
    nwb_handler.new_nwb(data)
    # print('\nChannel data in', data.info.blockname)
    # for channel in data.streams.keys():
    #     print(channel, data.streams[channel])
    # print(store, data.streams[store].data[:])
    # print('\nSampling rates in', data.info.blockname)
    # for store in data.streams.keys():
    #     print(store, '{:.4f} Hz'.format(data.streams[store].fs))
    # plt.plot(_405A_time[0:t], data.streams._405A.data[0:t], color='cornflowerblue')

convert()
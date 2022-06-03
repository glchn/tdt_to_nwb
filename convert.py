from tdt import read_block, read_sev, epoc_filter
import numpy as np
import matplotlib.pyplot as plt

from qtpy.QtWidgets import QFileDialog, QApplication
from os import getcwd, path, listdir
import sys
from datetime import datetime
from dateutil.tz import tzlocal
import numpy as np
import re

from pynwb import NWBFile, NWBHDF5IO, ProcessingModule, file
from pynwb.ecephys import ElectricalSeries, FilteredEphys, SpikeEventSeries, EventWaveform
from pynwb.behavior import BehavioralTimeSeries, EyeTracking, PupilTracking
from pynwb.misc import AbstractFeatureSeries

# global variables! change these as needed.
data_block = r'/mnt/c/Users/scsc7/Documents/Github/tdt_to_nwb/test'
nwb_name = 'test.nwb'

def new_nwb(tdt_data):
    nwb_io = []
    nwb_io = NWBHDF5IO(nwb_name, mode='w')
    nwb_file = NWBFile(session_description ="place holder",
                        identifier = "place holder",
                        subject = None,
                        session_id ="place holder",
                        session_start_time=tdt_data.info.start_date,
                        file_create_date=datetime.now(tzlocal()),
                        experimenter="placeholder",
                        lab="placeholder",
                        institution="placeholder",
                        source_script='convert.py',
                        source_script_file_name='convert.py',
                        notes="")
    nwb_io.write(nwb_file)
    nwb_io.close()

# converts tdt files to nwb file
# params: string block_path is path to tdt folder
#         string nwb_file_name is name of nwb file you will write to
def convert():
    data = read_block(data_block)
    print("\ndata:\n" + str(data))
    print("\ninfo:\n"+ str(data.info))
    print ('\nall stream stores: \n' + str(data.streams))
    new_nwb(data)
    print('\nChannel data in', data.info.blockname)
    for channel in data.streams.keys():
        print(channel, data.streams[channel])
    # print(store, data.streams[store].data[:])
    print('\nSampling rates in', data.info.blockname)
    for store in data.streams.keys():
        print(store, '{:.4f} Hz'.format(data.streams[store].fs))
convert()

# def convert(block_path):
#     # Explore Stream events
#     print('channel 1:', data.streams._405A.data[:])
#     print('Sampling rates in', data.info.blockname)
#     for store in data.streams.keys():
#         print(store, '{:.4f} Hz'.format(data.streams[store].fs))

#     num_samples = len(data.streams._405A.data)
#     print('number of samples:', num_samples)

#     _405A_time = np.linspace(1, num_samples, num_samples) / data.streams._405A.fs

#     t = int(2 * data.streams._405A.fs) # int rounds it to the nearest integer

# gettdt(data_block)

# this does something! i don't know what.
# def xt(arr, fs, axis=0):
#     retval = np.arange(0, (arr.shape[axis])/fs, 1/fs)
#     print("length of retval: " + str(len(retval)) + "\nretval is: " + str(retval))
#     return retval

# def get_fiber_data(data_block):
#     reader = tdt.TDTbin2py
#     data = reader.read_block(data_block)
#     print("\ndata is: " + str(data))

#     t = xt(data.streams._465A.data, data.streams._465A.fs)
#     # plotsimple(t, t/1)
#     led_on = data.epocs.TIG_.onset[1]
#     led_off = data.epocs.TIG_.offset[1]
#     t_on = np.argmin(np.abs(t-led_on))
#     t_off = np.argmin(np.abs(t-led_off))

#     # create file and write
#     f = open("test465_tdt.txt", "w")
#     f.write("data.streams._465A.data: " + str(data.streams._465A.data) + "\n" +
#             "data.streams._405A.data: " + str(data.streams._405A.data) + "\n" +
#             "data.streams._465A.fs: " + str(data.streams._465A.fs) + "\n" + 
#             "t_on: " + str(t_on) + "\n" +
#             "t_off: " + str(t_off) + "\n")
#     f.close()

#     return data.streams._465A.data,  data.streams._405A.data, data.streams._465A.fs, t_on, t_off

# data465, data405, fs, t_on, t_off = get_fiber_data(data_block)

# #   File "./convert.py", line 12, in get_fiber_data
# #     t = xt(data.streams._466A.data, data.streams._466A.fs)
# # AttributeError: 'StructType' object has no attribute '_466A'
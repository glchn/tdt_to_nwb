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

from pynwb import NWBFile, NWBHDF5IO, ProcessingModule, file, TimeSeries
from pynwb.epoch import TimeIntervals
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
    new_time_series(nwb_file, tdt_data)
    nwb_io.write(nwb_file)
    nwb_io.close()

# iterative time series data for each stream
def new_time_series(nwb_file, tdt_data):
    for store in tdt_data.streams.keys():
        # print("\ntimeseries" + str(store))
        # print(tdt_data.streams[store].data[:])
        # print(tdt_data.streams[store].fs)
        time_series_with_rate = TimeSeries(
            name = ("timeseries" + str(store)),
            data = tdt_data.streams[store].data[:],
            unit = "volts",
            starting_time = 0.0,
            rate = tdt_data.streams[store].fs
            )
        nwb_file.add_acquisition(time_series_with_rate)

# converts tdt files to nwb file
# params: string block_path is path to tdt folder
#         string nwb_file_name is name of nwb file you will write to
def convert():
    data = read_block(data_block)
    # print("\ndata:\n" + str(data))
    # print("\ninfo:\n"+ str(data.info))
    # print ('\nall stream stores: \n' + str(data.streams))
    new_nwb(data)
    # print('\nChannel data in', data.info.blockname)
    # for channel in data.streams.keys():
    #     print(channel, data.streams[channel])
    # print(store, data.streams[store].data[:])
    # print('\nSampling rates in', data.info.blockname)
    # for store in data.streams.keys():
    #     print(store, '{:.4f} Hz'.format(data.streams[store].fs))
convert()
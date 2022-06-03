from os import getcwd, path, listdir
import sys
from datetime import datetime
from dateutil.tz import tzlocal
import re

from tdt import read_block
import numpy as np

from pynwb import NWBFile, NWBHDF5IO, ProcessingModule, file, TimeSeries
from pynwb.ecephys import ElectricalSeries, FilteredEphys, SpikeEventSeries, EventWaveform
from pynwb.behavior import BehavioralTimeSeries, EyeTracking, PupilTracking
from pynwb.misc import AbstractFeatureSeries
from pynwb.file import Subject
import convert

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
    create_subject(tdt_data, nwb_file)
    nwb_io.write(nwb_file)
    nwb_io.close()
    print(nwb_file.session_description)

def create_subject(tdt_data, nwb_file):
    nwb_file.subject = Subject(
    subject_id="placeholder",
    age="placeholder",
    description="placeholder",
    species="placeholder",
    sex="placeholder",
    )

    # def add_spike_series(tdt_data, nwb_file):
    #     nwb_file.
    #     for channel in data.streams.keys():
    #         print(channel, data.streams[channel].time[0:t])
    #     time_series_with_rate = TimeSeries(
    #     name="test_timeseries",
    #     data=data,
    #     unit="m",
    #     starting_time=0.0,
    #     rate=1.0,
    # )
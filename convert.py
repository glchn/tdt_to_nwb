from tdt import read_block
import numpy as np
import matplotlib.pyplot as plt
import os
from os import getcwd, path, listdir, remove
from datetime import datetime
from dateutil.tz import tzlocal
import numpy as np
from pynwb import NWBFile, NWBHDF5IO, TimeSeries

data_block = r'/mnt/c/Users/scsc7/Documents/Github/tdt_to_nwb/test'
working_dir = r'/mnt/c/Users/scsc7/Documents/Github/tdt_to_nwb/'

# plot time series data of a nwb file
# param: nwb_in stream reader for nwb file we're plotting, store being plotted
def testplot(nwb_in, store):
    store_timeseries_entry = nwb_in.acquisition["timeseries"+str(store)]
    num_points = len(store_timeseries_entry.data[:])
    nwb_sampling_rate = store_timeseries_entry.rate
    time = np.linspace(1, num_points, num_points) / nwb_sampling_rate
    t = int(num_points * nwb_sampling_rate) # int rounds it to the nearest integer
    plt.plot(time[0:t], store_timeseries_entry.data[0:t], color='cornflowerblue') # plot the line using slices
    plt.title("NWB " + str([store]) + " Data", fontsize=16) # create title, axis labels
    plt.xlabel('Seconds', fontsize=14)
    plt.ylabel('Volts', fontsize=14)
    plt.autoscale(tight=True)
    plt.savefig("nwb" + str([store]) + ".jpg")
    plt.close()
    print("done plotting iteration" + str([store]) + "\n") # debug statement

# use to check if nwb file was correctly written. prints acquisition info and timeseries data. plots data.
# params: name of nwb file you'll be reading, tdt data used to grab the store info.
def checkwrite(nwb_name, tdt_data):
    nwb_io = NWBHDF5IO(nwb_name, 'r')
    nwb_in = nwb_io.read()
    print(nwb_in.acquisition)
    for store in tdt_data.streams.keys():
        print(nwb_in.acquisition["timeseries" + str(store)].data[:])
        testplot(nwb_in, store)

# creates new nwb file with basic properties
# param: tdt file from which data is retrieved, name of nwb file to create and write to
# TODO: add params for basic properties. not sure if these come from tdt file
def new_nwb(tdt_data, nwb_name):
    nwb_io = []
    if path.isfile(working_dir + nwb_name): # if file already exists, delete it
        os.remove(working_dir + nwb_name) # nwb doesn't like it when you re-write the metadata
        # print("file removed\n") # debug statement
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
    new_time_series(nwb_file, tdt_data) # add time series from tdt data
    nwb_io.write(nwb_file)
    nwb_io.close()

# creates a time series for each store
# params: nwb_file to be written to, tdt_data from which timeseries is extracted
def new_time_series(nwb_file, tdt_data):
    for store in tdt_data.streams.keys():
        time_series_with_rate = TimeSeries(
            name = ("timeseries" + str(store)),
            data = tdt_data.streams[store].data[:],
            unit = "volts",
            starting_time = 0.0,
            rate = tdt_data.streams[store].fs
            )
        nwb_file.add_acquisition(time_series_with_rate)

# converts tdt files to nwb file
# params: string nwb_file_name is name of nwb file you will write to
def convert(nwb_name):
    data = read_block(data_block)
    new_nwb(data, nwb_name)

convert('test.nwb') # write tdt data to nwb data
checkwrite('test.nwb', read_block(data_block)) # test read to check if data was successfully written
#TODO: stuck on Fi2r and Fi1r... why?
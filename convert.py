import tdt
from pynwb import NWBHDF5IO
import numpy as np

def xt(arr, fs, axis=0):
    return np.arange(0, (arr.shape[axis])/fs, 1/fs)

def get_fiber_data(data_block):
    reader = tdt.TDTbin2py
    data = reader.read_block(data_block)

    t = xt(data.streams._465A.data, data.streams._465A.fs)
    led_on = data.epocs.TIG_.onset[1]
    led_off = data.epocs.TIG_.offset[1]
    t_on = np.argmin(np.abs(t-led_on))
    t_off = np.argmin(np.abs(t-led_off))

    # create file and write
    f = open("test465_tdt.txt", "w")
    f.write("data.streams._465A.data: " + str(data.streams._465A.data) + "\n" +
            "data.streams._405A.data: " + str(data.streams._405A.data) + "\n" +
            "data.streams._465A.fs: " + str(data.streams._465A.fs) + "\n" + 
            "t_on: " + str(t_on) + "\n" +
            "t_off: " + str(t_off) + "\n")
    f.close()

    return data.streams._465A.data,  data.streams._405A.data, data.streams._465A.fs, t_on, t_off

data_block = r'/mnt/c/Users/scsc7/Documents/Github/tdt_to_nwb/test'
data465, data405, fs, t_on, t_off = get_fiber_data(data_block)

#   File "./convert.py", line 12, in get_fiber_data
#     t = xt(data.streams._466A.data, data.streams._466A.fs)
# AttributeError: 'StructType' object has no attribute '_466A'

# print("\nCONVERTING from tdt to nwb\n")

# with NWBHDF5IO("FibPhoTest-220218-125509_test-220523-190029.nwb", "r") as io:
#     read_nwbfile = io.read()
#     print("\nPRINTING nwb file contents\n")
#     print(read_nwbfile)
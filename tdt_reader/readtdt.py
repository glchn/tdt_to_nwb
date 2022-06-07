from tkinter import N
import matplotlib.pyplot as plt  # standard Python plotting library
import numpy as np  # fundamental package for scientific computing, handles arrays and maths
from tdt import read_block

block_path = r'/mnt/c/Users/scsc7/Documents/Github/tdt_to_nwb/test'

# produce plot for each stream
# param: path of tdt data
def plot_streams(block_path):
    data = read_block(block_path)
    # print ('\nall stream stores: \n' + str(data.streams)) # debugging print statements
    # print('\nChannel data in', data.info.blockname)
    # for channel in data.streams.keys():
    #     print(channel, data.streams[channel])

    for store in data.streams.keys(): # for each signal and panel
        num_points = len(data.streams[store].data[:]) # get the number of data points
        print('number of samples:', num_points) # print statement for debugging
        time = np.linspace(1, num_points, num_points) / data.streams[store].fs
        t = int(num_points * data.streams[store].fs) # int rounds it to the nearest integer
        fig1 = plt.subplots(figsize=(10, 6)) # declare figure size
        plt.plot(time[0:t], data.streams[store].data[0:t], color='cornflowerblue') # plot the line using slices
        plt.title("TDT " + str([store]) + " Data", fontsize=16) # create title, axis labels
        plt.xlabel('Seconds', fontsize=14)
        plt.ylabel('Volts', fontsize=14)
        plt.autoscale(tight=True)
        plt.savefig("tdt" + str([store]) + ".jpg")
        print("done iteration" + str([store]) + "\n") # print statement for debugging. getting stuck on Fi2r and Fi1r
        #TODO: stuck on Fi2r and Fi1r... why?

plot_streams(block_path)
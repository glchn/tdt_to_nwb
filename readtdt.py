import matplotlib.pyplot as plt  # standard Python plotting library
import numpy as np  # fundamental package for scientific computing, handles arrays and maths
# import the primary functions from the tdt library only
from tdt import read_block, read_sev, epoc_filter

#variables
block_path = r'/mnt/c/Users/scsc7/Documents/Github/tdt_to_nwb/test'

#fns
data = read_block(block_path)
print("\ndata:\n" + str(data))
print("\ninfo:\n"+ str(data.info))
print("\nstreams:\n"+ str(data.streams))
data.streams._405A.fs # dot syntax

# Explore Stream events
print('all stream stores')
print(data.streams)
print('channel 1:', data.streams._405A.data[:])
print('Sampling rates in', data.info.blockname)
for store in data.streams.keys():
    print(store, '{:.4f} Hz'.format(data.streams[store].fs))

num_samples = len(data.streams._405A.data)
print('number of samples:', num_samples)

_405A_time = np.linspace(1, num_samples, num_samples) / data.streams._405A.fs

t = int(2 * data.streams._405A.fs) # int rounds it to the nearest integer

# declare the figure size
fig1 = plt.subplots(figsize=(10, 6))

channel = 1 

# plot the line using slices
plt.plot(_405A_time[0:t], data.streams._405A.data[0:t], color='cornflowerblue')

# Some matplotlib stuff
# add an annotation mark to the figure
plt.annotate('Point Here',
             xy=(0.8,0.002),
             xytext=(.88,.003),
             arrowprops=dict(arrowstyle='->', color='k')
            )

# create title, axis labels, and legend
plt.title('_405A Data', fontsize=16)
plt.xlabel('Seconds', fontsize=14)
plt.ylabel('Volts', fontsize=14)
plt.legend(('Channel {}'.format(channel),),
           loc='lower right', 
           bbox_to_anchor=(1.0,1.01)
          )
plt.autoscale(tight=True)
plt.savefig("readtdt.jpg")
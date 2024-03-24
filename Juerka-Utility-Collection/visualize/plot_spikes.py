#!/usr/bin/env python3
# coding: utf-8

"""This is the plot generator script.
"""

import matplotlib.pyplot as plot
import numpy as np

def raster_plot(arguments):
    dirname = arguments.dirname
    network_index = arguments.logfile_index

    dir_separator = '/'
    logfile_name_prefix = 'JUNLOG_'
    logfile_name_suffix = '.txt'

    path = dirname + dir_separator + logfile_name_prefix + network_index + logfile_name_suffix
    
    Nx = 1000
    Ny = 1000

    fig, axs = plot.subplots(2, 1, figsize=[10,6])

    raw_data = []

    with open(path) as f:
        for s_line in f:
            raw_data.append([int(i) for i in s_line.split()])

    spike_array= np.zeros((Nx, Ny));
    spike_value = 1

    #print(raw_data)

    for x, y in raw_data:
        spike_array[y][x] = spike_value

    for trial in range(Ny):
        spike_times = [i for i, x in enumerate(spike_array[trial]) if x == spike_value]
        axs[0].vlines(spike_times, trial - 0.5, trial + 0.5)

    axs[0].set_xlim([0, Nx])

    axs[0].set_ylim([0, Ny])
    axs[0].set_ylabel('Neuron Number')

    axs[0].set_title('Neuronal Spike Times')

    #print(spike_array)
    axs[1].bar(range(spike_array.shape[1]),
               np.sum(spike_array, 0))

    axs[1].set_xlim([0, Nx])

    axs[1].set_title('Spike Histogram (SH)')
    axs[1].set_xlabel('Time (ms)')
    axs[1].set_ylabel('Spike Count')

    #plot.savefig('raster_plot_' + network_index + '.png', format='png', dpi=300)

    plot.show()


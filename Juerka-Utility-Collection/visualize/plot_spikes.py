#!/usr/bin/env python3
# coding: utf-8

"""This is the plot generator script.
"""
#from distutils.util import strtobool
import setuptools
import matplotlib.pyplot as plot
import numpy as np

def raster_plot(arguments):
    dirname = arguments.dirname
    network_index = arguments.logfile_index
    start_time = arguments.start_time
    silent = arguments.silent

    dir_separator = '/'
    logfile_name_prefix = 'JUNLOG_'
    logfile_name_suffix = '.txt'

    path = dirname + dir_separator + logfile_name_prefix + network_index + logfile_name_suffix
    
    Nx = 2000
    Ny = 2000

    ResponseYmin = 0
    ResponseYmax = 1599

    fig, axs = plot.subplots(3, 1, figsize=[10,6])
    
    raw_data = []

    int_start_time = 0+int(start_time)
    int_end_time = Nx+int(start_time)
    
    with open(path) as f:
        for s_line in f:
            sub_array = [int(i) for i in s_line.split()]
            #print(sub_array[0])
            if int_start_time <= sub_array[0] < int_end_time:
                sub_array[0] -= int_start_time
                raw_data.append(sub_array)
            if sub_array[0] >= int_end_time:
                break

    spike_array= np.zeros((Nx, Ny));
    spike_value = 1

    #print(raw_data)

    for x, y in raw_data:
        spike_array[y][x] = spike_value

    for trial in range(Ny):
        spike_times = [(int(i)+int_start_time) for i, x in enumerate(spike_array[trial]) if x == spike_value]
        axs[0].vlines(spike_times, trial - 0.5, trial + 0.5)

    axs[0].set_xlim([int_start_time, int_end_time])

    axs[0].set_ylim([0, Ny])
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Neuron Number')

    axs[0].set_title('Neuronal Spike Times')

    #print(spike_array)
    axs[1].bar([x+int_start_time for x in range(spike_array.shape[1])],
               np.sum(spike_array, 0))

    axs[1].set_xlim([int_start_time, int_end_time])
#    axs[1].set_ylim([0, Ny])
    axs[1].set_ylim([0, 1000])

    axs[1].set_title('Spike Histogram')
    axs[1].set_xlabel('Time (ms)')
    axs[1].set_ylabel('Spike Count')
    axs[1].grid()

    response_spike_array= np.zeros((Nx, Ny));

    for x, y in raw_data:
        if (y >= ResponseYmin) and (y <= ResponseYmax):
            response_spike_array[y][x] = spike_value

    axs[2].bar([x+int_start_time for x in range(response_spike_array.shape[1])],
            np.sum(response_spike_array, 0))

    axs[2].set_xlim([int_start_time, int_end_time])
#    axs[2].set_ylim([0, ResponseYmax+1-ResponseYmin])
    axs[2].set_ylim([0, 1000])

    axs[2].set_title('Spike Histogram for excitatory neurons')
    axs[2].set_xlabel('Time (ms)')
    axs[2].set_ylabel('Spike Count')
    axs[2].grid()

    plot.tight_layout()

    plot.savefig('raster_plot_' + network_index + '.png', format='png', dpi=600)

    if not bool(setuptools.distutils.util.strtobool(silent)):
        plot.show()

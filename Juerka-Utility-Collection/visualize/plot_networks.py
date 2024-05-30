#!/usr/bin/env python3
# coding: utf-8

"""This is the network plot generator script.
"""

#import networkit as nk
#import networkit as nx
#import networkit.vizbridges as nkv
#import matplotlib.pyplot as plt
import math
import os
import re
import numpy as np
from scipy import sparse
from sknetwork.visualization.graphs import svg_graph

def network_structure_plot(arguments):

    dirname = arguments.dirname
    network_index = arguments.logfile_index

    dir_separator = '/'
    logfile_name_prefix = 'JUNWEIGHTLOG_'
    logfile_name_suffix = '.txt'

    path = dirname + dir_separator + logfile_name_prefix + network_index + logfile_name_suffix

    pattern_added = '(\d+) added.*'
    pattern_deleted = '(\d+) deleted.*'

    current_time = 0

    read_mode = ""
    row = [];
    column = [];
    line_ind = 0;

    Nx = 1000
    Ny = 1000

    width = 1920
    height = 1080
    
    plot_ratio = 0.8

    a = width * plot_ratio
    b = height * plot_ratio

    new_dir_path = 'svg_log'
    os.makedirs(new_dir_path, exist_ok=True)
    
    t = np.linspace(0, 2 * math.pi, Nx)   
    position = np.zeros((t.shape[0], 2))

    names = [];
    for i in range(Nx):
        if i % 10 == 0:
            names.append(str(i))
        else:
            names.append('')
    names = np.array(names)

    for i in range(t.shape[0]):
        position[i][0] = a * (math.cos(t[i]))
        position[i][1] = b * (math.sin(t[i]))
    
    with open(path) as f:
        lines = f.readlines()
        
        while line_ind < len(lines):
            m1 = re.match(pattern_added, lines[line_ind])
#            if m1:
#                print("m1 matched.")
            m2 = re.match(pattern_deleted, lines[line_ind])
#            if m2:
#                print("m2 matched.")
            if m1:
                read_mode = 'ADDITION'
                line_ind += 1
                current_time = int(m1.group(1))
                print(current_time)
            elif m2:
                read_mode = 'DELETION'
                line_ind += 1
                current_time = int(m2.group(1))
                print(current_time)
            else:
                raw_arr_row = lines[line_ind].split()
                raw_arr_column = lines[line_ind+1].split()
                int_arr_row = [int(s) for s in raw_arr_row]
                int_arr_column = [int(s) for s in raw_arr_column]

                if read_mode == 'ADDITION':
                    print(int_arr_row)
                    print(int_arr_column)
                    if int_arr_row:
                        row.extend(int_arr_row)
                        column.extend(int_arr_column)
                if read_mode == 'DELETION':
                    delete_row_candidate = [i for i, x in enumerate(row) if x in int_arr_row]
                    delete_column_candidate = [i for i, x in enumerate(column) if x in int_arr_column]
                    matched_set = set(delete_row_candidate) & set(delete_column_candidate)

                    print(row)
                    print(column)
                    print(int_arr_row)
                    print(int_arr_column)
                    print(delete_row_candidate)
                    print(delete_column_candidate)
                    print(matched_set)
                    print(len(matched_set))
                    
                    for item in matched_set:
                        print('pop: ' + str(item))
                        row.pop(item)
                        column.pop(item)
                        
                    if any(row):                        
                        target_graph = np.zeros((Nx,Ny));
                        assert(len(row) == len(column))

                        for target_row, target_column in zip(row, column):
                            target_graph[target_row, target_column] = 1

                        adjacency = sparse.csr_matrix(target_graph)
                        n_nodes, _ = adjacency.shape
                        #names = np.arange(n_nodes)
                        node_weights = np.array([i for i in adjacency.getnnz(0)])
                        
                        filename = new_dir_path + dir_separator + str(current_time)
                        
                        svg_graph(adjacency,
                                  position = position,
                                  names = names,
                                  directed = True,
                                  width = width,
                                  height = height,
                                  edge_color='rgb(255, 212, 222)',
                                  scale = 0.5,
                                  display_node_weight=True,
                                  node_weights=node_weights,
                                  filename=filename)
                
                line_ind+=2

    '''
    adjacency = np.array([[0, 0, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]])
    adjacency = sparse.csr_matrix(adjacency)
    n_nodes, _ = adjacency.shape
    names = np.arange(n_nodes)
    svg_text = svg_graph(adjacency, names=names, directed=True)
    '''


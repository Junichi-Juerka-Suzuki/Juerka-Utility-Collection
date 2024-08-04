#!/bin/bash

for i in `seq 0 1000 9000`
do
	python3 Juerka-Utility-Collection/Juerka_Utility_Collection.py visualize_spikes -dirname 20240602100005 -logfile_index 0 -start_time $i -silent True
    mv raster_plot_0.png raster_plot_${i}_test4.png
done


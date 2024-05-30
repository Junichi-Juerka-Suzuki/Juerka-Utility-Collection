# Juerka-Utility-Collection
## Overview
### What is this?
This is the collection of utility scripts for ![Juerka](https://github.com/Junichi-Juerka-Suzuki/Juerka).

### The purpose of this?
It's simple. These utility scripts are intended for better understanding of spiking neural network activities.
In other words, you can visualize or analyze spiking neural network activities with these utility scripts.

### Who contributes to this?
Myself.

### About sponsors
If you like it, please donate!

Thank you!.
ありがとうございます。

## plot_spikes.py
### Introduction
This simple python script visualizes spike activities as a raster plot.

For example:

![raster_plot_0](https://github.com/Junichi-Juerka-Suzuki/Juerka-Utility-Collection/assets/163645026/b90c91f5-1ec3-4be9-b36c-b2081b79c017)

### How to use it
#### Linux environment
You can run the script like using the below command.

```sh
$ python3 ./Juerka_utilities.py visualize -dirname 20240322112453 -logfile_index=0
```
#### Windows environment
I would like to write down this content later.

### Technical details
Input file should contain the lines of \"spike_timing\" and \"neuron_number\".

For example:

```
0 10 <- spike_timing: 0[ms] & neuron_number: 10
2 986
...
999 564
```

### Limitations
Currently this script only supports the range of \[0,1000\) for both spike_timing and neuron_number.

## plot_networks.py
### dependencies

Please pip install below packages.
- scikit-network

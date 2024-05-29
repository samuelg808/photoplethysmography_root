# Photoplethysmography

2Ba Industrial Sciences Vrije Universiteit Brussel, Engineering Programming task
## Table of Contents


- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [ToDo](#todo)

## Introduction

This project was made for the Engineering Programming course at the Vrije Universiteit Brussels. The goal for this project was to create a Python program that calculates the BPM of a video taken of your fingertip with the flashlight on. I added a GUI for ease of use, the instructions are explained below. This task is based on the results of Jonathan and Leahy's (2010) research paper investigating a smartphone imaging unit for photoplethysmography.

## Features

- Calculate the average BPM of the whole video: A single window can be used to calculate the average BPM of the entire video (different fps and resolution are compatible).
- Calculate BPM over 5 windows: Using five windows, the BPM can be calculated and plotted over time. It is recommended to use a video of +30 seconds to ensure enough data is collected per window.
- Determine percentile ranking based on this [dataset](/data/dataset-72971.csv): Percentile ranking can be determined from a data set (not in GUI).

## Installation

To run this project, you will need to have the following Python libraries installed:

- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html) 
- [sys](https://docs.python.org/3/library/sys.html)

You can install these libraries using pip, Python's package manager. Open your terminal or command prompt and issue the following command

```bash
pip install matplotlib numpy pandas
```

## Usage

Calculate the average BPM over the entire video:

1. Enter the full path of the .mp4 file in the GUI
2. Select the number of windows, in this case 1
3. Look at the Power Spectral Density graph and determine it's Lowcut and Highcut, enter them in the input box and click Next.
4. The plotted graphs are the second iteration ones, click on OK.
5. The average BPM over the whole video is given.

To calculate the BPM over 5 windows
1. Enter the full .mp4 file path in the GUI
2. Select the number of windows, in this case 5
3. Look at all the Power Spectral Density graphs and determine their lowcuts and highcuts, fill in all the input boxes and click Next.
4. The plotted graphs are the second iteration ones, click on OK.
5. The BPM over 5 windows is now plotted over the duration of the entire video.

## Documentation

For a more detailed analysis of the project, including its background, methodology and results, please refer to my [report](reportEP.pdf). 

## ToDo

- Add GUI compatibility for different screen resolutions

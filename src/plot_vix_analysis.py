#!/usr/bin/env pythonT

# Written by Sophia Wang
# Date： 2017-12-07
# Plot vix autocorrelation chart

# libraries/packages used
import os
import csv
import numpy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import argparse
import pylab

# define argument
parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('dst')
args = parser.parse_args()

# main function
# plot vix autocorrelation
def main():
    src = args.src
    dst = args.dst
    interval = []
    corrcoef = []
    # input file
    with open (src) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            interval.append(row[0])
            corrcoef.append(row[1])
    interval = numpy.array([float(i) for i in interval[1:]])
    corrcoef = numpy.array([float(c) for c in corrcoef[1:]])
    # output png file
    fig = plt.figure()
    plt.bar(interval, corrcoef, width=0.5,color="blue")
    plt.axes()
    ax = fig.add_subplot(1, 1, 1)
    plt.yticks(numpy.arange(-0.25,0,0.05))
    plt.xticks(numpy.arange(1,21,1))
    ax.xaxis.set_ticks_position("top")
    plt.ylabel("VIX Autocorrelation Coefficient")
    plt.xlabel("Time Interval")
    plt.title('VIX Prediction',y=1.08,fontweight="bold")
    pylab.savefig(dst + '.png')


# call main function
if __name__ == "__main__":
    main()

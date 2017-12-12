#!/usr/bin/env python
import os
import csv
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import argparse
import pylab

parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('dst')
args = parser.parse_args()

#main function
def main():
    src = args.src
    dst = args.dst
    interval = []
    corrcoef = []
    with open(os.path.join(src)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            interval.append(row[0])
            corrcoef.append(row[1])
    interval = numpy.array([float(i) for i in interval[1:]])
    corrcoef = numpy.array([float(c) for c in corrcoef[1:]])

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
    pylab.savefig(os.path.join(dst) + '.png')


# call main function
if __name__ == "__main__":
    main()

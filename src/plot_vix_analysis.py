#!/usr/bin/env python
import os
import csv
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import argparse
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
    with open(os.path.join(os.pardir, src)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            interval.append(row[0])
            corrcoef.append(row[1])
    interval = numpy.array([float(i) for i in interval[1:]])
    corrcoef = numpy.array([float(c) for c in corrcoef[1:]])

    fig = plt.figure()
    plt.plot(interval, corrcoef, 'ro')
    pp = PdfPages(os.path.join(os.pardir, dst) + '.pdf')
    pp.savefig(fig)
    pp.close()

# call main function
if __name__ == "__main__":
    main()

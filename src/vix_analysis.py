#!/usr/bin/env python

import os
import csv
import numpy
import datetime
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('dst')
args = parser.parse_args()

#main function
def main():
    src = args.src
    dst = args.dst
    vix_close = []
    dte = []
    with open(os.path.join(os.pardir, src)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            vix_close.append(row[4])
            dte.append(row[0])

    vix_close = vix_close[1:]
    vix_close = numpy.array([float(v) for v in vix_close])
    dte = dte[1:]
    dte = [d.split('/') for d in dte]
    dte = numpy.array([datetime.date(int(d[2]), int(d[0]), int(d[1])) for d in dte])
    min_dte = datetime.date(2007, 1, 1)
    max_dte = datetime.date(2017, 1, 1)
    vix_close = vix_close[numpy.logical_and(dte<max_dte, dte>=min_dte)]

    interval_list = []
    corrcoef_list = []
    for i in range(20):
        interval = i + 1
        tmp_vix_close_0 = vix_close[:-2*interval]
        tmp_vix_close_1 = vix_close[interval:-interval]
        tmp_vix_close_2 = vix_close[2*interval:]
        tmp_vix_diff_0 = tmp_vix_close_1 - tmp_vix_close_0
        tmp_vix_diff_1 = tmp_vix_close_2 - tmp_vix_close_1
        corrcoef = numpy.corrcoef(tmp_vix_diff_0, tmp_vix_diff_1)[0][1]
        interval_list.append(interval)
        corrcoef_list.append(corrcoef)

    with open(os.path.join(os.pardir, dst), 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['VIX diff interval', 'T and T-1 diff correlation coefficient'])
        for i in range(len(interval_list)):
            csvwriter.writerow([interval_list[i], corrcoef_list[i]])

# call main function
if __name__ == "__main__":
    main()

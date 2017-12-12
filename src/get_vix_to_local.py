#!/usr/bin/env python

# Written by Sophia Wang
# Date： 2017-12-07
# Get data from CBOE VIX csv file to data directory
# http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv

# libraries/packages used
import urllib.request
import os
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument('url')
parser.add_argument('dst')
args = parser.parse_args()

#main function
def main():
    #url = args.url
    dst = args.dst

    #input file
    response = urllib.request.urlopen("http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv")
    data = response.read().decode('UTF-8')
    data = '\n'.join(data.split('\n')[1:])

    #output file
    output_file_directory = os.path.join(dst)
    with open(output_file_directory,'w') as output:
        output.write(data)

# call main function
if __name__ == "__main__":
    main()

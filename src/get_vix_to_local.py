#!/usr/bin/env python

# Get data from CBOE VIX csv file to data directory
# http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv

# libraries/packages used
import urllib.request
import os
import sys

url = sys.argv[1]
dst = sys.argv[2]

#main function
#url = 'http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv'
response = urllib.request.urlopen(url)
data = response.read().decode('UTF-8')
data = '\n'.join(data.split('\n')[1:])

#output file
output_file_directory = os.path.join(os.pardir, dst)
with open(output_file_directory,'w') as output:
    output.write(data)

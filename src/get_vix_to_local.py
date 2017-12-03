#!/usr/bin/env python

# Get data from CBOE VIX csv file to data directory
# http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv

# libraries/packages used
import urllib.request
import os

#main function
url = 'http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv'
response = urllib.request.urlopen(url)
data = response.read()

#output file
output_file_directory = os.path.join(os.pardir, 'data', 'vix_data.csv')
print(output_file_directory)
with open(output_file_directory,'wb') as output:
    output.write(data)

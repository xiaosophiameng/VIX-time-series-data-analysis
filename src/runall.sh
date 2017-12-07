#!/bin/sh
python get_vix_to_local.py http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv data/vix_data.csv
python vix_analysis.py data/vix_data.csv results/vix_analysis.csv
python plot_vix_analysis.py results/vix_analysis.csv results/vix_analysis_plot

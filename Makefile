# Driver script
# Xiaomeng(Sophia) Wang, Dec 2017

# Usage: run all the scripts together and make all the associated output

# make all the following files with running this makefile
# using "make all"
all: doc/vix_report.md
#all: data/vix_data.csv results/vix_analysis.csv results/vix_analysis_plot.png

# create vix_data.csv
# download data from website by running the get_vix_to_local.py script in src
# save the downloaded csv file in the data folder named as vix_data.csv
data/vix_data.csv: src/get_vix_to_local.py
	python src/get_vix_to_local.py data/vix_data.csv

# create vix_analysis.csv
# Conduct the analysis by running vix_analysis.py script in src folder
# with the input data file vix_data.csv in the data folder
# save output analysis result in the results folders named vix_analysis.csv
results/vix_analysis.csv: src/vix_analysis.py data/vix_data.csv
	python src/vix_analysis.py data/vix_data.csv results/vix_analysis.csv

# vix_analysis_plot
# Make plot by running plot_vix_analysis.py script in src folder
# based on the analysis result saved in results folders named vix_analysis.csv
# save the output plot in the results folder named vix_analysis_plot
results/vix_analysis_plot.png: src/plot_vix_analysis.py results/vix_analysis.csv
	python src/plot_vix_analysis.py results/vix_analysis.csv results/vix_analysis_plot

# create final report
doc/vix_report.md: src/vix_report.rmd data/vix_data.csv results/vix_analysis.csv results/vix_analysis_plot.png
		Rscript -e "ezknitr::ezknit('src/vix_report.rmd', out_dir = 'doc')"
# clean up intermediate files
# clean:
# 	rm -f data/vix_data.csv
# 	rm -f results/vix_analysis.csv
# 	rm -f results/vix_analysis_plot.png
# 	rm -f doc/vix_report.md doc/vix_report.html

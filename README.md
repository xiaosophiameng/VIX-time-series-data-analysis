Title: VIX Analysis

Author: Xiaomeng Wang (Sophia)

Date: December 10, 2017

Project: Milestone 3

---



## Summary of the project

VIX is an index which shows the market's expectation of 30-day volatility for the Chicago Board Options Exchange (CBOE). The project aims to find out whether the trend of vix index is predictable. 

To see whether the vix index is predictable by itself, I based on the 10 years' vix index (from January 1st, 2007 to January 1st, 2017) and calculated the auto-correlation coefficients between time T and time T+1, where T ranges from 1-day period to 20-day period. According to the derived results, for the 10-year time horizon, all the autocorrelation coefficients are negative from 1-day period to 20-day period. Thus, we can conclude that the trend of vix index is predictable by itself and the value of the vix index is negatively correlated with its short term return.



## Usage

#### How to use makefile

To run the full analysis and run the `makefile`, open the command line/terminal/Git bash and follow the steps below:

1. Use command `cd` to change the current directory to the project root directory
2. Use command `atom Makefile` to access the make file
3. Use command `make all` to run all the scripts
	- If you need to re-run the makefile for any purpose, use command `make clean` first to delete all the output files; then use command `make all` to finish re-running

#### How to use dockerfile

To use the `makefile`, open the command line/terminal/Git bash and follow the steps below:

1. Use command `docker pull xiaosophiameng/vix-time-series-data-analysis-final` to download the docker container to your local drive
2. Use command `docker build -t docker-vix-analysis .`to build docker
3. Use command `docker run -v /Users/xiaomengwang/documents/522_milestone/VIX-time-series-data-analysis:/docker-vix-analysis docker-vix-analysis make all` to run build environment, install all related packages and run all the scripts
 - Note: On the left hand side of the : is the path on your own computer. On the right hand side of the : is the path on the container. This should almost always start with /home/rstudio/.
4. In case you want to clean up your make file, use command `docker run -v /Users/xiaomengwang/documents/522_milestone/VIX-time-series-data-analysis:/docker-vix-analysis docker-vix-analysis clean`


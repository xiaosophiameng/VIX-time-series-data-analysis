---
Author: Xiaomeng Wang (Sophia)

Date: Decmber 10, 2017

Project: Milestone 2

---



## Summry of the project

VIX is an index which shows the market's expectation of 30-day volatility for the Chicago Board Options Exchange (CBOE). The project aims to find out whether the trend of vix index is preditable. 

To see whether the vix index is predictable by itself, I based on the 10 years' vix index (from January 1st, 2007 to January 1st, 2017) and calculated the auto-correlation coefficients between time T and time T+1, where T ranges from 1-day period to 20-day period. According to the derived results, for the 10-year time horizon, all the auto-correlation coefficients are negative from 1-day period to 20-day period. Thus, we can conclude that the trend of vix index is preditable by itself and the value of the vix index is negatively correlated with its short term return.

## How to run my data analysis

#### Order scripts are run in

Here is the order to run my scripts:

- 1. get_vix_to_local.py
- 2. vix_analysis.py
- 3. plot_vix_analysis.py

#### Expected inputs for each script

- Inputs for script `get_vix_to_local.py`: 
	- http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv 
	- data/vix_data.csv
- Inputs for script vix_analysis.py: 
	- data/vix_data.csv 
	- results/vix_analysis.csv
- Inputs for script plot_vix_analysis.py: 
	- results/vix_analysis.csv 
	- results/vix_analysis_plot

Note: A runall.sh file is included in the directory for users to run all my scripts together
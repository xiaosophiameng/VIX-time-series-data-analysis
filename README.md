---
Author: Xiaomeng Wang (Sophia)

Date: Decmber 3, 2017

Project: Milestone 1

---



## Choose a Data Set

[VIX Data since 2004](http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv)

Explanation of VIX: VIX is an index which shows the market's expectation of 30-day volatility for the Chicago Board Options Exchange (CBOE)

Users can run the file `git_vix_to_local.py` in the `src` folder to get the vix index from the public website and output it as a csv file into your local `data` folder. 


## Identify a Question

Question: Whether the trend of vix index is preditable 

## Generate a Hypothesis

Hypothesis: The value of the vix index is negatively correlated with its short term return; that is, if the current vix is high, we expect a negative vix, and vice versa  


## Analysis and Data Visualization

#### Analysis 

I plan to calculte the correlation coefficients of the current vix index with its future return in the terms of t, where t ranges from 1 day to 30 days. If most of the correlation coefficients are significantly negative, my hypothesis can be concluded as acceptable. If most of the the correlation coefficients are positive, my hypothesis should be rejected.

#### Data Visualization 

Thus far, I plan to make the following plots:

- plot the histogram for the entire sample vix data to display the range of the index and how it is distributed
- plot the correlation coefficients of the vix index with its future return in the term of t, where t equals to 1 day to 30 days to view the entire trend   

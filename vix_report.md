Vix Analysis Report
================
Sophia Wang
2017-12-09

Introduction
------------

VIX is an index which shows the market's expectation of 30-day volatility for the Chicago Board Options Exchange (CBOE). The project aims to find out whether the trend of vix index is preditable by itself. That is, are there any associations between the value of vix for a certain time period and its return over the next time period?

Data Resource
-------------

The data resource of vix index is from the website <http://www.cboe.com/>. The first few rows of the data resource are shown in the table as below. There are five columns: Date, VIX.Open, VIX.High, VIX.Low, VIX.Close. From the data column, we can see the vix data is summarised on a daily basis from Monday to Friday. VIX.Open and VIX.Close show the starting vix and ending vix for a given business day, respectively. VIX.High and VIX.Low display the highest vix and lowest vix for a given business day, respectively.

| Date     |  VIX.Open|  VIX.High|  VIX.Low|  VIX.Close|
|:---------|---------:|---------:|--------:|----------:|
| 1/2/2004 |     17.96|     18.68|    17.54|      18.22|
| 1/5/2004 |     18.45|     18.49|    17.44|      17.49|
| 1/6/2004 |     17.66|     17.67|    16.19|      16.73|
| 1/7/2004 |     16.72|     16.75|    15.50|      15.50|
| 1/8/2004 |     15.42|     15.68|    15.32|      15.61|
| 1/9/2004 |     16.15|     16.88|    15.57|      16.75|

Data Analysis and Visualization
-------------------------------

To see whether the vix index is predictable by itself, I based on the 10 years' vix index (from January 1st, 2007 to January 1st, 2017) and calculated the auto-correlation coefficients between time T and time T+1, where T ranges from 1-day period to 20-day period. The first column in the table below shows the time intervals and the second column provides the corresponding correlation coefficient. According to the result, for a 10-year time horizon, all the auto-correlation coefficients are negative from 1-day period to 20-day period. Thus, we can conclude that vix index is negatively self-correlated in the short term. The plot below demonstrates the auto-correlation coefficients range from roughly −0.08 to −0.25.

|  VIX.diff.interval|  correlation.coefficient|
|------------------:|------------------------:|
|                  1|               -0.1297951|
|                  2|               -0.1664354|
|                  3|               -0.2082684|
|                  4|               -0.2400652|
|                  5|               -0.2408114|
|                  6|               -0.1982981|
|                  7|               -0.1854868|
|                  8|               -0.1602489|
|                  9|               -0.1256151|
|                 10|               -0.1023419|
|                 11|               -0.1043480|
|                 12|               -0.1140703|
|                 13|               -0.1084521|
|                 14|               -0.0973736|
|                 15|               -0.0917499|
|                 16|               -0.0792844|
|                 17|               -0.0792394|
|                 18|               -0.0986280|
|                 19|               -0.1020681|
|                 20|               -0.1009557|

<img src="./results/vix_analysis_plot.png" width="100%" />

Conclusion
----------

To sum up, the trend of vix index is preditable by itself and the value of the vix index is negatively correlated with its short term return.

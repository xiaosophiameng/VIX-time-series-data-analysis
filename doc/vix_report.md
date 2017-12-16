---
title: "Vix Analysis Report"
author: "Sophia Wang"
date: '2017-12-09'
output: pdf_document
---



## Introduction

VIX is an index which shows the market's expectation of 30-day volatility for the Chicago Board Options Exchange (CBOE). The project aims to find out whether the trend of vix index is predictable by itself. That is, are there any associations between the value of vix for a certain time period and its return over the next time period?


## Data Resource

The data resource of vix index is from the website http://www.cboe.com/. The first few rows of the data resource are shown in the table as below. There are five columns: Date, VIX.Open, VIX.High, VIX.Low, VIX.Close. From the data column, we can see the vix data is summarised on a daily basis from Monday to Friday. VIX.Open and VIX.Close show the starting vix and ending vix for a given business day, respectively. VIX.High and VIX.Low display the highest vix and lowest vix for a given business day, respectively. 


```
## Warning in file(file, "rt"): cannot open file '../data/vix_data.csv': No
## such file or directory
```

```
## Error in file(file, "rt"): cannot open the connection
```

```
## Error in head(vix_data): object 'vix_data' not found
```

## Data Analysis and Visualization

To see whether the vix index is predictable by itself, I based on the 10 years' vix index (from January 1st, 2007 to January 1st, 2017) and calculated the auto-correlation coefficients between time T and time T+1, where T ranges from 1-day period to 20-day period. The first column in the table below shows the time intervals and the second column provides the corresponding correlation coefficient. According to the result, for a 10-year time horizon, all the autocorrelation coefficients are negative from 1-day period to 20-day period. Thus, we can conclude that vix index is negatively self-correlated in the short term. The plot below demonstrates the auto-correlation coefficients range from roughly $-0.08$ to $-0.25$.


```
## Warning in file(file, "rt"): cannot open file '../results/
## vix_analysis.csv': No such file or directory
```

```
## Error in file(file, "rt"): cannot open the connection
```

```
## Error in eval(expr, envir, enclos): object 'vix_data' not found
```

[vix_analysis_plot.png](../results/vix_analysis_plot.png)


## Conclusion

To sum up, the trend of vix index is predictable by itself and the value of the vix index is negatively correlated with its short term return.

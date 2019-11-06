# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:37:34 2019

@author: Arthur
"""

import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Setting Start and Stop points from collecting data
start=dt.datetime(2019,1,1)
end=dt.datetime(2019,10,4)

# Prices from Apple, changing to % and getting the last price
prices=web.DataReader('AAPL','yahoo',start,end)['Close']
returns=prices.pct_change()
last_price=prices.iloc[-1]

# Defining how many simulations and how many days we are gonna try to predict
num_trials=1000
num_days=30
simulations=pd.DataFrame()

# Running Simulations
for i in range(num_trials):
    count=0
    daily_vol=returns.std()
    
    price_series=[]
    price_series.append(last_price+(1+np.random.normal(0,daily_vol)))
    
    for j in range(num_days):
        if count==num_days-1:
            break
        price_series.append(last_price+(1+np.random.normal(0,daily_vol)))
        count+=1
    simulations[i]=price_series
    
# Creating plot with real prices and simulated prices
dates=pd.date_range(end,dt.datetime(2019,11,2)).tolist()
simulations.index=dates
plt.figure(figsize=(16,8))
plt.title('Forecasting AAPL Closed Prices with Monte Carlo Simulations')
plt.ylabel('Price')
plt.plot(prices)
plt.plot(simulations,linestyle='--')
plt.savefig('Forecasted.png')
plt.show()

# Zoomed plot
plt.figure(figsize=(16,8))
plt.title('Zoomed Forecasting AAPL Closed Prices with Monte Carlo Simulation')
plt.ylabel('Price')
plt.plot(simulations)
plt.savefig('Zoomed Forecasted.png')
plt.show()
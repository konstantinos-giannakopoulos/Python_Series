import numpy as np
from pandas_datareader import data as web
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

start = dt.datetime(2016,1,1)
end = dt.datetime(2019,1,1)

apple = web.DataReader('AAPL', 'yahoo', start, end)
data = apple['Adj Close']

x = data.index.map(mdates.date2num)

fit = np.polyfit(x, data.values, 1)
fit1d  = np.poly1d(fit)

plt.grid()
plt.plot(data.index, data.values, 'b')
plt.plot(data.index, fit1d(x), 'r')
plt.show()

# Setting the time frame
rstart = dt.datetime(2018,7,1)
rend = dt.datetime(2019,1,1)

fit_data = data.reset_index()
pos1 = fit_data[fit_data.Date >= rstart].index[0]
pos2 = fit_data[fit_data.Date <= rend].index[-1]

fit_data = fit_data.iloc[pos1:pos2]

dates = fit_data.Date.map(mdates.date2num)

fit = np.polyfit(dates, fit_data['Adj Close'], 1)
fit1d = np.poly1d(fit)

plt.grid()
plt.plot(data.index, data.values, 'b')
plt.plot(fit_data.Date, fit1d(dates), 'r')
plt.show()

import pandas_datareader
from pandas_datareader import data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


df = pd.read_csv("apple.csv")

# 1) Plotting Diagrams
df['Adj Close'].plot()
plt.show()

style.use('ggplot')
plt.ylabel('Adjusted Close')
plt.title('AAPL Share Price')
df['Adj Close'].plot()
plt.show()

# comparing stocks
style.use('ggplot')

start = dt.datetime(2017,1,1)
end = dt.datetime(2022,7,31)

apple = web.DataReader('AAPL', 'yahoo', start, end)
facebook = web.DataReader('FB', 'yahoo', start, end)
amazon = web.DataReader('AMZN', 'yahoo', start, end)

apple['Adj Close'].plot(label="AAPL")
facebook['Adj Close'].plot(label="FB")
amazon['Adj Close'].plot(label="AMZN")
plt.ylabel('Adjusted Close')
plt.title('Share Price Comparison')
plt.legend(loc='upper left')
plt.show()

#

plt.subplot(211)
apple['Adj Close'].plot(color="blue")
plt.ylabel('Adjusted Close')
plt.title('AAPL Share Price.')

plt.subplot(212)
amazon['Adj Close'].plot(color="yellow")
plt.ylabel('Adjusted Close')
plt.title('AMZN Share Price')

plt.tight_layout()
plt.show()

# 2) Candlestick Charts
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

start = dt.datetime(2017,1,1)
end = dt.datetime(2022,7,31)

apple = apple[['Open', 'High', 'Low', 'Close']]

apple.reset_index(inplace=True)
apple['Date']=apple['Date'].map(mdates.date2num)

ax = plt.subplot()
candlestick_ohlc(ax, apple.values, width=5, colordown='r', colorup='g')
ax.grid()
ax.xaxis_date()
plt.show()

# Plotting multiple days
apple = web.DataReader('AAPL', 'yahoo', start, end)
apple_ohlc = apple['Adj Close'].resample('10D').ohlc()
apple_ohlc.reset_index(inplace=True)
apple_ohlc['Date'] = apple_ohlc['Date'].map(mdates.date2num)
apple_volume = apple['Volume'].resample('10D').sum()

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=4, colspan=1)
ax2 = plt.subplot2grid((6,1),(4,0),rowspan=4, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, apple_ohlc.values, width=5, colorup='g', colordown='r')
ax2.fill_between(apple_volume.index.map(mdates.date2num),apple_volume.values)
plt.tight_layout()
plt.show()

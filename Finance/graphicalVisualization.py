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

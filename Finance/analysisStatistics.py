import matplotlib.pyplot as plt
import pandas as pd

apple = pd.read_csv("apple.csv")

# 100-day moving average
# create a new column, and fill it with the mean values of every 100 entries
apple['100d_ma'] = apple['Adj Close'].rolling(window = 100, min_periods = 0).mean()

# drop NaN-Values
apple.dropna(inplace=True)

print(apple.head())

# visualization
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=4, colspan=1)
ax2 = plt.subplot2grid((6,1),(4,0),rowspan=4, colspan=1, sharex=ax1)

ax1.plot(apple.index, apple['Adj Close'])
ax1.plot(apple.index, apple['100d_ma'])
ax2.fill_between(apple.index, apple['Volume'])
plt.tight_layout()
plt.show()

# percentage change
apple['PCT_Change'] = ( apple['Close'] - apple['Open'] ) / apple['Open']

# high-low percentage
apple['HL_PCT'] = ( apple['High'] - apple['Low'] ) / apple['Close']

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=4, colspan=1)
ax2 = plt.subplot2grid((6,1),(4,0),rowspan=4, colspan=1, sharex=ax1)

ax1.plot(apple.index, apple['PCT_Change'])
#ax2.plot(apple.index, apple['HL_PCT'])
ax2.fill_between(apple.index, apple['HL_PCT'])
plt.tight_layout()
plt.show()

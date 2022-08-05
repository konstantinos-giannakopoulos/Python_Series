import bs4 as bs
import requests
import pickle


# 1) Webscraping
def load_sp500_tickers():
    # html requests
    link = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(link)

    # BeautifulSoup
    soup = bs.BeautifulSoup(response.text, 'html5lib') # 'lxml'

    table = soup.find('table', {'class':'wikitable sortable'})

    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text[:-1]
        tickers.append(ticker)

    return tickers
    
tickers = load_sp500_tickers()
#print(tickers)

# Serializing Tickers
with open("sp500tickers.pickle",  'wb') as f:
    pickle.dump(tickers, f)


# 2) Loading Share Prices
import os
import datetime as dt
import pandas_datareader as web

def load_prices(reload_tickers=False):
    if reload_tickers:
        tickers = load_sp500_tickers()
    else:
        if os.path.exists('sp500tickers.pickle'):
            with open('sp500tickers.pickle','rb') as f:
                tickers = pickle.load(f)

if not os.path.exists('companies'):
    os.makedirs('companies')

start = dt.datetime(2017,1,1)
end = dt.datetime(2019,1,1)

for ticker in tickers:
    if not os.path.exists('companies/{}.csv'.format(ticker)):
        print("{} is loading...".format(ticker))
        try:
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('companies/{}.csv'.format(ticker))
        except:
            print("Error in: ", ticker)
    else:
        print('{} already downloaded!'.format(ticker))

# 3) Compiling Data
with open('sp500tickers.pickle','rb') as f:
    tickers = pickle.load(f)
main_df = pd.DataFrame()

print("Compiling data... ")
# 4) Visualizing Data
# 5) Correlations



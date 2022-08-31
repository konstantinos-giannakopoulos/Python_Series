import pandas_datareader
from pandas_datareader import data as web
import datetime as dt
import xml.sax
import pandas as pd

'''
Goal:
Processing financial data from the Yahoo Finance API
'''
# 1) Loading Data

# specify time frames 
start = dt.datetime(2017,1,1)
end = dt.datetime(2019,1,1)
#end = dt.datetime.now()

# define a dataframe to load the financial data into it
df = web.DataReader('AAPL', 'yahoo', start, end) # Apple
print(df.head(5))

# reading individual values
print(df['Close'])
print(df['Close']['2017-02-14'])
print(df['Close'][5])


# Saving to CSV and loading from CSV, Excel, HTML, JSON
#for xml
#handler = xml.sax.ContentHandler()
#parser = xml.sax.make_parser()
#parser.setContentHandler(handler)
#parser.parse()

df.to_csv('apple.csv')
df.to_excel('apple.xlsx')
df.to_html('apple.html')
df.to_json('apple.json')

df = pd.read_csv("apple.csv")
print("CSV file read")
df = pd.read_excel("apple.xlsx")
print("Excel file read")
df = pd.read_html("apple.html",flavor='html5lib')
print("HTML file read")
df = pd.read_json("apple.json")
print("JSON file read")

#regression stock prices
import config
quandl.ApiConfig.api_key = config.api_key

import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
#High - low percent, the percent volatiltiy. 
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#Percent change is (new-old)/old

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]


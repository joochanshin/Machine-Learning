#regression stock prices
import config
import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key = config.api_key
df = quandl.get('WIKI/GOOGL', rows=5)
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
#High - low percent, the percent volatiltiy. 
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#Percent change is (new-old)/old

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = "Adj. Close"
df.fillna(-99999, inplace=True) #na=not available. You cant use NaN in ML or sacrifice data

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head)
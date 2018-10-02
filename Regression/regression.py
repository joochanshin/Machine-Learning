#regression stock prices
import config
import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, model_selection, svm #support vector machine
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = config.api_key
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
#High - low percent, the percent volatiltiy. 
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#Percent change is (new-old)/old

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = "Adj. Close"
df.fillna(-99999, inplace=True) #na=not available. You cant use NaN in ML or sacrifice data

forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])

x = preprocessing.scale(x)

#x = x[:-forecast_out+1]
y = np.array(df['label'])

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1) #classifier
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)  

print(accuracy)
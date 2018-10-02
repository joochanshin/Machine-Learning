#regression stock prices
import config
import pandas as pd
import quandl, math, datetime
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

x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)
x_lately = x[-forecast_out:]
x = x[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])
y = y[:-forecast_out]
y = np.array(df['label'])




x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1) #classifier
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)  

forecast_set = clf.predict(x_lately)

print(forecast_set, accuracy, forecast_out)
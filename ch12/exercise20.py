# pp 211

import yfinance as yf
tkr = yf.Ticker('AAPL')
hist = tkr.history(period="1y")
import pandas_datareader.data as pdr
from datetime import date, timedelta
end = date.today()
start = end - timedelta(days=365)
index_data = pdr.get_data_stooq('^SPX', start, end)  
df = hist.join(index_data, rsuffix = '_idx')
df = df[['Close','Volume','Close_idx','Volume_idx']]
import numpy as np
df['priceRise'] = np.log(df['Close'] / df['Close'].shift(1))
df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))
df['priceRise_idx'] = np.log(df['Close_idx'] / df['Close_idx'].shift(1))
df['volumeRise_idx'] = np.log(df['Volume_idx'] / df['Volume_idx'].shift(1))
df = df.dropna()
df = df[['priceRise','volumeRise','priceRise_idx','volumeRise_idx']]
conditions = [
(df['priceRise'].shift(-1) > 0.01),
(df['priceRise'].shift(-1)< -0.01)
]
choices = [1, -1]
df['Pred'] = np.select(conditions, choices, default=0)

features = df[['priceRise','volumeRise','priceRise_idx','volumeRise_idx']].to_numpy()
features = np.around(features, decimals=2)
target = df['Pred'].to_numpy()

from sklearn.model_selection import train_test_split
rows_train, rows_test, y_train, y_test = train_test_split(features, target, test_size=0.2)
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(rows_train, y_train)

print(clf.score(rows_test, y_test))

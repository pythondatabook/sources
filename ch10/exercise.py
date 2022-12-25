# pp 172 - 173  

import yfinance as yf
import numpy as np
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='1mo')
df = df[['Close','Volume']].rename(columns={'Close': 'Price'})
df['priceRise'] = np.log(df['Price'] / df['Price'].shift(1))
df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))
df['volumeSum'] = df['Volume'].shift(1).rolling(2).sum().fillna(0).astype(int)
print(df[abs(df['priceRise']) > .05].replace(0, np.nan).dropna())
df['nextVolume'] = df['Volume'].shift(-1).fillna(0).astype(int)
print(df[abs(df['priceRise']) > .05].replace(0, np.nan).dropna())  

import yfinance as yf
import numpy as np
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='5d')
print(pd.concat([df['Close'], df['Close'].shift(2)], axis=1, keys= ['Close', '2DaysShift']))
df['2daysRise'] = np.log(df['Close'] / df['Close'].shift(2))
print(df[['Close','2daysRise']])

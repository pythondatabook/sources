# pp 83  

import yfinance as yf
data = []
tickers = ['TSLA', 'FB', 'ORCL','AMZN']
for ticker in tickers:
 tkr = yf.Ticker(ticker)
 hist = tkr.history(period='5d').reset_index()
 records = hist[['Date','Close']].to_records(index=False)
 records = list(records)
 d = records
 records = [(ticker, str(elem[0])[:10], elem[1]) for elem in records]
 data = data + records 
print(data)

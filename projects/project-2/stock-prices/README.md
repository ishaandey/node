
Use stock api to get stock data indexed by time

```python
# In case packages doesn't work
# !pip install pandas-datareader

# Imports
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web
import pandas as pd

start_dt = '2020-01-01'
end_dt =  '2020-10-10'

# For individual stock
stock = 'TSLA'
tsla_data = web.DataReader(stock, data_source = 'yahoo', start = start_dt, end = end_dt)
tsla_data.head()

# For portfolio of stocks
stocks = ['FB', 'AAPL',  'AMZN', 'NFLX', 'GOOGL']
data = pd.DataFrame()
for symbol in stocks:
  data[symbol] = web.DataReader(symbol, data_source = 'yahoo', start = start_dt, end = end_dt)['Adj Close']
data.head()  
```
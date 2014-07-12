import pandas.io.data as web
from datetime import datetime
start = datetime(2014, 6, 1)
end = datetime(2014, 6, 13)
f=web.DataReader("IBM", 'yahoo', start, end)
print f
print f["Open"][0], f["Close"][-1]

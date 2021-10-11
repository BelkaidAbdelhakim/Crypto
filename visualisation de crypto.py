
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

crypto='BTC'
currency='EUR'
start=dt.datetime(2021,7,1)
end=dt.datetime.now()
btc=web.DataReader('BTC-EUR','yahoo',start,end)
eth=web.DataReader('ETH-EUR','yahoo',start,end)
#print(data)
mpf.plot(eth,type='candle',volume=True,style='yahoo')
mpf.plot(btc,type='candle',volume=True,style='yahoo')

plt.plot(eth['Close'],label='Etherium')
plt.plot(btc['Close'],label='Bitcoin')
plt.legend()
plt.xticks(rotation=45)
plt.show()
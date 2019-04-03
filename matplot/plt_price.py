'''

'''
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab 
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker 
from datetime import date
from matplotlib.pylab import date2num
from datetime import datetime
import quandl
import os

myticker = 'IBM'
begdate = date(2017, 1, 1)  
enddate = date(2017, 12, 31)
price = quandl.get('WIKI/'+myticker, stat_date=begdate, end_date=enddate)
path = os.path.split(os.path.realpath(__file__))[0]
path += '/%s.csv' % myticker
price.to_csv(path)

price = pd.read_csv(path)
price_date = [
            date2num(datetime.strptime(x,'%Y-%m-%d')) for x in price['Date']
        ]
price_adj_close = price["Adj. Close"]
# print(price)

ax = plt.subplots()
plt.plot(price_date[-30:], price_adj_close[-30:], 'o-')
plt.title('IBM')
# plt.show()

ind = np.arange(len(price_date[-30:]))

def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, len(price_date[-30:])-1)
    return price_date[-30:][thisind].strftime('%Y-%m-%d')

fig, ax = plt.subplots()
plt.plot(ind, price_adj_close[-30:], 'o-')
plt.xlabel('Every Monday shown')
ax.set_title('IBM')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()
plt.show()
'''
历史回报率的均值估计期望收益，历史回报率的标准差估计收益的风险
分布的峰值位于右侧的股票具有较高的预期收益 
分布的分散度表示风险水平，分布越广意味着风险越高
'''

import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.mlab as mlab
import quandl
from datetime import date

ticker = 'IBM'
begdate = date(2017,1,1)
enddate = date(2017,12,31)
price = quandl.get('WIKI/IBM', start_date=begdate, end_date=enddate)
price = np.array(price.Close)
# print(price)
ret = (price[1:] - price[:-1]) / price[1:]
# print(ret)
n, bins, patches = plt.hist(ret, 100)

mu = np.mean(ret)    # average historical rate of return
print(mu)
sigma = np.std(ret)    # std historical rate of return/ risk of return
x = mlab.normpdf(bins, mu ,sigma)
plt.plot(bins, x, color='red', lw=2)
plt.title('IBM return distribution')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.show()
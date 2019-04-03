'''
做多股票，做空期权的组合／股票多头和看涨期权空头的组合
'''

# A股票100股，每股$10，同时卖出一个看涨期权，每一个合同对应的股票100股，
# 看涨期权的价格$2，执行价格$15

import numpy as np 
import matplotlib.pyplot as plt 

s_t = np.arange(0, 40, 5)
k = 15     # 期权执行价格
s_0 = 10   # 每股价格 
c = 2      # 期权价格

y_0 = np.zeros(len(s_t))
y_1 = s_t - s_0    # 股票
y_2 = (abs(s_t - k) + s_t - k) / 2 - c    # 看涨期权
y_3 = y_1 - y_2    # 投资组合 y1 buy   y2 sell

plt.ylim(-10, 30)
plt.plot(s_t, y_1)
plt.plot(s_t, y_2)
plt.plot(s_t, y_3, 'r')
plt.plot(s_t, y_0, 'b-.')
plt.plot([k, k], [-10, 10], 'k')

plt.title('covered call (long one share and short one call)')
plt.xlabel('stock price')
plt.ylabel('profit (loss)')

plt.annotate(
    'stock only (long one share)', xy=(24, 15), xytext=(15, 20),
    arrowprops=dict(facecolor='blue', shrink=0.01)
)
plt.annotate(
    'long one share, short a call', xy=(10, 4), xytext=(9, 25),
    arrowprops=dict(facecolor="red", shrink=0.01)
)
plt.annotate(
    'exercise price = ' + str(k), xy=(k+0.2, -10+0.5)
)
plt.show()
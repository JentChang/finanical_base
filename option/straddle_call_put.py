'''
straddle - buy a call and a put with the same exercise prices
跨式期权组合－具有相同价格执行价格额看涨期权和看跌期权
'''
# 背景
# 某个企业在下一个月将发生重大事件＿不能确定事件结果的方向
# 同时买进执行价格相同的一个看涨和一个看跌期权＿无论上涨或是下跌，都可以获利
# 假设 exercise price is $30

import numpy as np 
import matplotlib.pyplot as plt 

sT = np.arange(30, 80, 5)
x = 50   # exercise price
c = 2    # call option price
p = 1    # put option price

y_call = (abs(sT - x) + sT - x) /2 - c
y_put = (abs(x - sT) + x - sT) /2 - p
straddle = y_call + y_put
y_0 = np.zeros(len(sT))

plt.ylim(-6, 20)
plt.xlim(40, 70)
plt.plot(sT, y_0)
plt.plot(sT, straddle, 'r')
plt.plot([x, x], [-6, 4], 'g-.')
plt.plot([40, x], [-p-c, -p-c], 'b-.')
plt.title('profit-loss for a straddle')
plt.xlabel('stock price')
plt.ylabel('profit(loss)')

plt.annotate(
    'point_1=' + str(x-c-p), xy=(x-p-c, 0), xytext=(x-p-c, 10),
    arrowprops=dict(facecolor='red', shrink=0.01)
)
plt.annotate(
    'point_2=' + str(x+c+p), xy=(x+p+c, 0), xytext=(x+p+c, 13),
    arrowprops=dict(facecolor='blue', shrink=0.01)
)
plt.annotate('exercise price', xy=(x+1, -5))
plt.annotate('max loss '+str(p+c), xy=(40.5, -p-c+0.5))
plt.annotate(
    'buy a call and buy a put with the same exercise price', xy=(45, 16)
)
plt.show()
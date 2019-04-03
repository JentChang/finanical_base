'''
期权的收益和利润／损失函数
S_t stock price at the maturity date(t)
X the exercise price
c option price
'''

import scipy as sp
import matplotlib.pyplot as plt   

x = 45 # 执行价格20
c = 2.5 # 期权价格
p = 2
s = sp.arange(30, 70, 5) # 到期日股票价格
profit_call = (abs(s - x) + s - x) / 2 - c # 收益函数
profit_put = (abs(x - s) + x -s) / 2 - p
y = sp.zeros(len(s))
y2 = [-30, 10]
x2 = [x, x]

fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 20))
ax1.set_title('profit/loss function for call option')
ax1.plot(s, profit_call, 'b')
ax1.plot(s, y, 'g-.')
ax1.plot(s, -profit_call, 'r')
ax1.plot(x2, y2, 'g--')
ax1.annotate(
    'call option buyer', xy=(55, 15), xytext=(35, 30),
    arrowprops=dict(facecolor='blue', shrink=0.01)
)
ax1.annotate(
    'call option seller', xy=(55, -10), xytext=(35, -20),
    arrowprops=dict(facecolor='red', shrink=0.01)
)

ax2.set_title('profit/loss function for call option')
ax2.plot(s, profit_put, 'b')
ax2.plot(s, y, 'g-.')
ax2.plot(s, -profit_put, 'r')
ax2.plot(x2, y2, 'g--')
ax2.annotate(
    'put option buyer', xy=(35, 18), xytext=(45, 30),
    arrowprops=dict(facecolor='blue', shrink=0.01)
)
ax2.annotate(
    'put option seller', xy=(35, -15), xytext=(45, -25),
    arrowprops=dict(facecolor='red', shrink=0.01)
)

plt.xlabel('stock price')
plt.ylabel('profit/loss')
ax1.set_ylim(-30, 50)
ax2.set_ylim(-30, 50)
plt.show()
'''
a calendar spread
日历套现组合
involves two call option with the 
same exercise price
but different maturities(where T1 < T2)
'''

# 卖出较短的看涨期权，并购买较长期限的看涨期权．
# 看涨期权的价格与有效期呈正相关positively，需要付出现金initial cash来购买日历套利组合
# 希望当第一个看涨期权到期时，标的股票的价格接近行权价格exercise price

import numpy as np 
import matplotlib.pyplot as plt 


def bs_call(S,X,T,r,sigma):
    ''''期权定价

    args:
    s 当前价格
    x 执行价格
    r 复利无风险利率
    T 期权有效期
    sigma 股票波动率
    '''
    from scipy import log,exp,sqrt,stats
    d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)


sT = np.arange(20, 70, 10)
s = 40
x = 40
T1 = 0.5
T2 = 1
sigma = 0.3
r = 0.05

payoff = (abs(sT - x) + sT - x) / 2
call_short = bs_call(s, x, T1, r, sigma)
call_long = bs_call(s, x, T2, r, sigma)
profit_short = payoff - call_short
call_cycle = bs_call(sT, x, (T2 - T1), r, sigma)
calendar_spread = call_cycle - payoff + call_short - call_long

y0 = np.zeros(len(sT))
plt.ylim(-20, 20)
plt.xlim(20, 60)
plt.plot(sT, call_cycle, 'b-.')
plt.plot(sT, call_long-call_short-payoff, 'b-.')
plt.plot(sT, calendar_spread, 'r')
plt.plot([x, x], [-20, -15])
plt.title('calendar spread with calls')
plt.xlabel('stock price at maturity (sT)')
plt.ylabel('profit (loss)')

plt.annotate(
    'buy a call with T1 and sell a call with T2', xy=(25, 16)
)
plt.annotate(
    'where T1 < T2', xy=(25, 14)
)
plt.annotate(
    'calendar spread', xy=(25, -3), xytext=(22, -15),
    arrowprops=dict(facecolor='red', shrink=0.01)
)
plt.annotate(
    'value of the call (T2) at maturity', xy=(45, 7), xytext=(25,10),
    arrowprops=dict(facecolor='blue', shrink=0.01)
)
plt.annotate(
    'profit/loss with call_long only', xy=(50, -10), xytext=(30, -10),
    arrowprops=dict(facecolor='blue', shrink=0.01)
)
plt.show()  
from datetime import date
import tushare as ts
import matplotlib.pyplot as plt 
import numpy as np 


def fun(myticker,start,end):
    '''获取收盘价'''
    price = ts.get_k_data(myticker, start=start, end=end)
    price = np.array(price['close'][-30:])
    # 返回回报率
    return (
        (price[1:] - price[:-1]) / price[1:]
    )

myticker = '600466'
start = '20171001'
end = '20181212'
ret_LGFZ = fun(myticker, start, end)
print(ret_LGFZ)
ret_SZ = fun('000001', start=start, end=end)
print(ret_SZ)

n = min(len(ret_LGFZ), len(ret_SZ))
s = np.ones(n)*2
t = range(n)
line = np.zeros(n)

plt.plot(t, ret_LGFZ[0:n], 'ro', s)
plt.plot(t, ret_SZ[0:n], 'bd', s)
plt.plot(t, line, 'b', s)
plt.figtext(0.4, 0.8, 'Red for LGFZ.SH, Blue for 1A0001.SH')
plt.xlim(1, n)
plt.ylim(-0.04, 0.07)
plt.title('Comparions between stock and market returns')
plt.xlabel('Day')
plt.ylabel('Returns')
plt.show()

'''
投资组合

years    stock_A     stock_B
2009       0.102      0.1062
2010       -0.02        0.23
2011       0.213       0.045
2012        0.12       0.234
2013        0.13       0.113
'''
import numpy as np 
import matplotlib.pyplot as plt 

year = [2009, 2010, 2011, 2012, 2013]
ret_a = np.array([0.102, -0.02, 0.213, 0.12, 0.13])
ret_b = np.array([0.1062, 0.23, 0.045, 0.234, 0.113])
port_EW = (ret_a + ret_b) / 2
print(round(np.mean(ret_a),3), round(np.mean(ret_b),3), round(np.mean(port_EW),3))
print(round(np.std(ret_a),3), round(np.std(ret_b),3), round(np.std(port_EW),3))

plt.figtext(0.2, 0.65, 'Stock_A')
plt.figtext(0.15, 0.4, 'Stock_B')
plt.xlabel('year')
plt.ylabel('Returns')
plt.plot(year, ret_a, lw=2)
plt.plot(year, ret_b, lw=2)
plt.plot(year, port_EW, lw=2)
plt.title('Indiviudal stocks vs. an equal-weighted 2-stock portflio')
plt.annotate('Equal-weighted Portfolio', xy=(2010, 0.1), 
             xytext=(2011, 0), arrowprops=dict(facecolor='black', shrink=0.5))
plt.ylim(-0.1, 0.3)
plt.show()
'''
现金的时间价值
'''

import matplotlib.pyplot as plt 

fig1 = plt.figure(facecolor='white')
ax1 = plt.axes(frameon=False)
ax1.set_frame_on(False)
ax1.axes.get_yaxis().set_visible(False)

x = range(0, 11, 2)
x1 = range(len(x), 0, -1)
y = [0]*len(x)

v0 = "Today's value of $100 received today"
v2 = "Today's value of $100 received in years"
v6 = "received in 6 yearss"
v10 = 'received in 10 years'
c = "black"

plt.annotate(
    v0, xy=(0, 0), xytext=(2, 0.1), arrowprops=dict(facecolor=c, shrink=0.02)
)
plt.annotate(
    v2, xy=(2, 0.005), xytext=(3.5, 0.08), arrowprops=dict(facecolor=c, shrink=0.02)
)
plt.annotate(
    v6, xy=(4, 0.00005), xytext=(5.3, 0.06), arrowprops=dict(facecolor=c, shrink=0.02)
)
plt.annotate(
    v10, xy=(10, -0.00005), xytext=(4, -0.06), arrowprops=dict(facecolor=c, shrink=0.02)
)
s = [50*2.5**n for n in x1]
plt.title('Time value of money')
plt.xlabel('Time (number of years)')
plt.scatter(x, y, s=s)
plt.show()
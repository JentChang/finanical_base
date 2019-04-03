'''
正态分布
1/sqr(2*pi*pow(\sigma,2))exp(-pow((x-\mu),2)/(2pow(\sigma)))
stats.norm.pdf()
'''
from scipy import exp, sqrt, stats
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.mathtext as mathtext


def f(t):
    return stats.norm.pdf(t)     #默认标准正态分布　＼mu=0 \sigma=1


z = 0.2
x = np.arange(-3, 3, 0.1)
y = f(x)

fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 8))
ax1.set_ylim(0, 0.45)
ax1.plot(x, y)     # 绘制标准正态分布

x2 = np.arange(-4, z, 1/40.)
sum = 0
delta = 0.001
s = np.arange(-10, z, delta)

for i in s:
    sum += f(i) * delta     # 累积

ax1.annotate(
    'area is ' + str(round(sum, 4)), xy=(-1, 0.25), xytext=(-3.8, 0.4),
    arrowprops=dict(facecolor='red', shrink=0.01)
)
ax1.annotate(
    'z = ' + str(z), xy=(z, 0.01)
)
ax1.fill_between(x2, f(x2))    # 填充


def f2(x):
    return stats.norm.cdf(x)     # 计算标准正态分布累积


y1 = f2(x)
y2 = np.ones(len(x)) * 0.5
x3 = [0, 0]
y3 = [0, 1]

ax2.plot(x, y1, 'r')
ax2.plot(x, y2, 'b-')
ax2.plot(x3, y3)
ax2.scatter([z, z], [f2(z), 0], c='b', marker='o')
    
ax2.annotate(
    'f(z)=f(' + str(z) + ') is ' + str(np.round(f2(z), 4)),
    xy=(z, f2(z)), xytext=(z-3, f2(z)), arrowprops=dict(facecolor='red', shrink=0.01)
)
ax2.annotate(
    'z is ' + str(z), xy=(z, 0), xytext=(1.5, 0.3),
    arrowprops=dict(facecolor='blue', shrink=0.01)
)
ax2.set_xlim(-3, 3)
ax2.set_ylim(0, 1)

m = r'$\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$'
parser = mathtext.MathTextParser('Bitmap')
r, depth = parser.to_rgba(m, color='k', fontsize=12, dpi=120)
fig.figimage(r.astype(float)/255., 450, 580)
plt.show()
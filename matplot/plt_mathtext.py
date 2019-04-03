'''
数学公式在matplotlib上的显示
'''

import numpy as np 
import matplotlib.mathtext as mathtext
import matplotlib.pyplot as plt 
import matplotlib

m1 = r'$c=S_ON(d_1)-Ke^{-rT}N(d_2)$'
m2 = r'$d_2=\frac{len(S_0/K)+(r-\sigma^2/2)T}{\sigma\sqrt{T}}=d_1-\sigma\sqrt{T}$'
m3 = r'$d_1=\frac{len(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt{T}}$'

matplotlib.rc('image', origin='upper')
parser = mathtext.MathTextParser('Bitmap')
r1, depth1 = parser.to_rgba(m1, color='red', fontsize=12, dpi=200)
r2, depth2 = parser.to_rgba(m2, color='blue', fontsize=12, dpi=200)
r3, depth3 = parser.to_rgba(m3, color='blue', fontsize=14, dpi=200)

image = plt.imread('latex.pngs')

fig = plt.figure()
fig.figimage(r1.astype(float)/255., 100, 100)
fig.figimage(r2.astype(float)/255., 100, 200)
fig.figimage(r3.astype(float)/255., 100, 300)
ax = plt.imshow(image,alpha=0.05)
plt.axis('off')
plt.show()

'''
EPS 每股收益
'''
import matplotlib.pyplot as plt 
import numpy as np 

a_eps = (5.02, 4.54, 4.18, 3.73)
b_eps = (1.35, 1.88, 1.35, 0.73)

ind = np.arange(len(a_eps))    # the x location for the groups
width = 0.40    # the width of the bars
fig, ax = plt.subplots()
a_std = b_std = (0.5,0.5,0.5,0.5)
rects1 = ax.bar(ind, a_eps, width, color='r', yerr=a_std)
rects2 = ax.bar(ind+width, b_eps, width, color='y', yerr=b_std)
ax.set_ylabel('EPS')
ax.set_xlabel("Year")
ax.set_title("Diluted EPS Excluding Extraordinary Items")
ax.set_xticks(ind+width)
ax.set_xticklabels(('2012', '2011', '2010', '2009'))
ax.legend((rects1[0], rects2[0]), ('W-Mart', 'DELL'))
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height,
        '%d'%int(height), ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.show()
print((rects1[0], rects2[0]))
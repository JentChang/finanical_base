'''
port_sigma protfolio-std of annual revenue投资组合的年收益的标准差 
i_sigma indiviudal stock-std of annual revenue单只股票的标准方差
n stock_num   port_sigma    port_sigma/i_sigma
          1       49.236                  1.00
          2       37.358                  0.76
          4       29.687                  0.60
          6       26.643                  0.54
          8       24.983                  0.51
        ...          ...                   ...
        800       19.233                  0.39
        900       19.217                  0.39
       1000       19.211                  0.39
         >>       19.158                  0.39
'''

import matplotlib.pyplot as plt 

n = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 75, 100,
     200, 300, 400, 500, 600, 700, 800, 900, 1000]
port_sigma = [
   0.49236, 0.37358, 0.29687, 0.26643, 0.24983, 0.23932, 0.23204, 0.22670, 
   0.22261, 0.21939, 0.21677, 0.21196, 0.20870, 0.20634, 0.20456, 0.20316, 
   0.20203, 0.19860, 0.19686, 0.19432, 0.19336, 0.19292, 0.19265, 0.19347,
   0.19233, 0.19224, 0.19217, 0.19211, 0.19158
]

plt.xlim(0, 50)
plt.ylim(0.1, 0.4)
plt.hlines(0.19217, 0, 50, colors='r', linestyles='dashed')
plt.annotate('', xy=(5, 0.19), xycoords="data", xytext=(5, 0.28),
             textcoords='data',arrowprops={'arrowstyle':'<->'})
plt.annotate('', xy=(30, 0.19), xycoords='data', xytext=(30, 0.1),
             textcoords='data', arrowprops={'arrowstyle':'<->'})
plt.annotate('Total portfolio risk', xy=(5, 0.3), xytext=(25, 0.35),
             arrowprops=dict(facecolor='black', shrink=0.02))
plt.figtext(0.15, 0.4, 'Diversiable risk')
plt.figtext(0.65, 0.25, 'Nondiversifiable risk')
plt.plot(n, port_sigma[0:28])

plt.title('Relationship between n and portfolio risk')
plt.xlabel('Nujmber of stocks in a portfolio')
plt.ylabel('Ratio of Portfolio std to std of one stock')
plt.show()
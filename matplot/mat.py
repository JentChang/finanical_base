"""matplotlib绘图的基本操作"""


import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.cos(2*x)

# 创建figure对象，生成画板  # 参数依次是图名，大小，dpi，背景色，边缘色
plt.figure(num='正余弦函数图', figsize=(10, 6), dpi=120, facecolor='y', edgecolor='g')
    # 在绘制时设置lable, 逗号是必须的
l1 = plt.plot(x, y1, color='red', linestyle='-', linewidth=0.5, label='$sin(x)$')
l2 = plt.plot(x, y2, 'b', label='$cos(x)$')
    # plt.plot(x, y1, 'r--', x, y2, 'b-.', x, y3, 'g') 叠加图 在一个图画出多条不同格式的线
    # 设置坐标轴的取值范围
plt.axis((-6.5, 6.5, -1.1, 1.1))
    # plt.xlim((-6.5, 6.5))
    # plt.ylim((-1.1, 1.1))


# 设置坐标轴的lable
plt.xlabel('X axis')
plt.ylabel('Y axis')
# 设置x坐标轴刻度, 原来为0.25, 修改后为0.5 # plt.xticks(np.linspace(-2*np.pi, 2*np.pi, 9))
# 第一个参数是位置，第二个参数是标签lable，$使字体倾斜，\ 输出空格，\alpha_i输出数学符号α1也可直接alpha
plt.xticks((-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi),
           ('$-2π$', '$-3π/2$', '$-π$', '$-π/2$', r'$0\ \alpha_i$', 'π/2', 'π', '3π/2', '2π'))
plt.yticks((-1, 0, 1))

# 设置、显示legend
plt.legend(loc='best')  # loc参数设置图例显示的位置


# 设置图表的标题
plt.title('cos&sin')
plt.text(-np.pi, 1, '任意位置添加文字',fontdict={'size': 10, 'color': 'y'})  # text在图中任意位置添加文字，前两个参数是左下角的位置坐标
plt.annotate('max', xy=(0, 1), xytext=(1, 1.05), arrowprops=dict(facecolor='k', shrink=1))  # 注释的地方xy(x,y)和插入文本的地方xytext(x1,y1)


# 移动坐标轴，spines为脊梁，即4个边框
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')  # 设置右‘脊梁’为无色
ax.spines['top'].set_color('none')  # 设置上‘脊梁’为无色
ax.xaxis.set_ticks_position('bottom')  # 底部‘脊梁’设置为X轴
ax.spines['bottom'].set_position(('data', 0))  # 底部‘脊梁’移动位置，y的data
ax.yaxis.set_ticks_position('left')  # 左部‘脊梁’设置为Y轴
ax.spines['left'].set_position(('data', 0))  # 左部‘脊梁’移动位置，x的data


# 给特殊点做注释，在2π/3的位置给两条函数曲线加一个注释
plt.plot([2*np.pi/3, 2*np.pi/3], [0, np.sin(2*np.pi/3)], 'r--')  # xy是基于xycoords的data
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(2*np.pi/3, np.sin(2*np.pi/3)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle="->",
             connectionstyle="arc3,rad=.2"))  # +10，+30表示基于xy加10，加30，textcoords='offset points'代表基于xy
plt.scatter([2*np.pi/3], [np.sin(2*np.pi/3)], 40, 'r')  # 绘制点x,y,大小，颜色
plt.plot([2*np.pi/3, 2*np.pi/3], [0, np.cos(2*np.pi/3)], 'b--')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$', xy=(2*np.pi/3, np.cos(2*np.pi/3)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle="->",
             connectionstyle="arc3,rad=.2"))  # arrowprops设置指示线的格式,connectionstyle设置线的角度，弧度
plt.scatter([2*np.pi/3], [np.cos(2*np.pi/3)], 40, 'b')
plt.show()
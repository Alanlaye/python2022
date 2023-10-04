#15.2.3 使用scatter()绘制散点图
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40) 
#生成y值的列表解析，它遍历x值,计算其平方值
#使用实参s设置了绘制图形时使用的点的尺寸
#将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

#函数axis()指定了每个坐标轴的取值范围
#函数axis()要求提供四个值：x和y坐标轴的最小值和最大值
plt.axis([0,1100,0,1100000])

plt.savefig('squares_plot.png',bbox_inches='tight')

plt.show()
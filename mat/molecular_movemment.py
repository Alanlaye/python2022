import matplotlib.pyplot as plt
from random_walk import RandomWalk
# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk(3000) 
rw.fill_walk()
plt.plot(rw.x_values,rw.y_values,linewidth=1)
plt.scatter(0,0,c='green',edgecolors='none',s=10)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)
plt.show()



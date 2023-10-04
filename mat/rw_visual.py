import matplotlib.pyplot as plt
from random_walk import RandomWalk
# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置绘图窗口分辨率和尺寸
    plt.figure(dpi=128,figsize=(10,8))

    point_numbers = list(range(rw.num_points))
    #使用了range()生成了一个数字列表,其中包含的数字个数与漫步包含的点数相同
    
    #关闭坐标
    #plt.axes()方法使用时，必须将他赋值给一个变量，然后调用他才可以正常使用
    #也可以直接使用plt.axes('off')
    current_axes = plt.axes()
    current_axes.get_xaxis().set_visible(False)
    current_axes.get_yaxis().set_visible(False)

     #关闭刻度
    plt.xticks([])
    plt.yticks([])

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
         cmap=plt.cm.spring, edgecolors='none', s=1)
    
    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=10)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)
    
    plt.show()
    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n':
        break
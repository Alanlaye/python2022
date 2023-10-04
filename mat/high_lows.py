import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = r"C:\Users\零落\Desktop\python_work\《Python编程》源代码文件\chapter_16\sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #读取第一行
    for index,column_header in enumerate(header_row):
        print(index,column_header)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    #遍历余下各行，并将每行的row[1]存储到列表highs中
    #int将字符串转换成数字
    print(highs)

#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')
#设置图形格式

plt.title("Daily high temperatures, July 2014", fontsize=24) 
plt.xlabel('', fontsize=16) 
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#关闭刻度
plt.xticks([])

plt.show()

#读取表示日期的字符串
first_date = datetime.strptime('2014-7-1','%Y-%m-%d')
print(first_date)
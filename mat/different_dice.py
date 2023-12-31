from die import Die
import pygal
# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die() 

# 掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(500000):
    result = die_1.roll()*die_2.roll()
    results.append(result)
# 分析结果
frequencies = []
max_value = die_1.num_sides*die_2.num_sides
frequencies = [results.count(value) for value in range(1,max_value+1)]


# 可视化结果

hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times." 
hist.x_labels = [str(value) for value in range(1,max_value+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D10', frequencies)
hist.render_to_file('different_visual.svg')



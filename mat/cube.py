import matplotlib.pyplot as plt

x_values = list(range(1,101))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.spring, edgecolors='none', s=40)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("cube", fontsize=14)

plt.tick_params(axis='both',labelsize=14)
plt.axis([0,100,0,1000000])

plt.show()

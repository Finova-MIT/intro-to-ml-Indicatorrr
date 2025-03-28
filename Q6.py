import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 8, 12, 16, 20]


plt.plot(x, y, color='b', marker='o', linestyle='-', linewidth=2, markersize=6)
plt.title("Simple Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()


plt.scatter(x, y, color='r', marker='x', s=100)  # s sets marker size
plt.title("Simple Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()

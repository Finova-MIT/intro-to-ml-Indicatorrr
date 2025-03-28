import seaborn as sns
import matplotlib.pyplot as plt

data = [12, 15, 14, 13, 19, 18, 21]

sns.boxplot(data=data, color='skyblue')
plt.title("Box Plot")
plt.show()

sns.histplot(data, bins=5, kde=False, color='purple') 
plt.title("Histogram")
plt.show()

sns.kdeplot(data, fill=True, color='red') 
plt.title("Density Plot")
plt.show()
import numpy as np
import matplotlib.pyplot as plt

marks = [85, 90, 78, 92, 88]

print("Marks:", np.mean(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))

plt.hist(marks, bins=5, edgecolor='black', color='skyblue')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
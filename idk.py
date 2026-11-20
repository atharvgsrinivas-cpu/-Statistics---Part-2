import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.DataFrame({
    "runtime": [120, 150, 200, 180, 220, 160, 190, 210],
    "imdb_rating": [7.5, 8.0, 6.5, 7.0, 8.5, 7.2, 6.8, 7.9]
})

print(data.head(5 ))

print(data.isnull().sum())

plt.hist(data['runtime'])
plt.xlabel("runtime")
plt.ylabel("Frequency")
plt.title("Distribution of Runtime")
plt.show()

bins_time = np.arange(120, 230, 10)
plt.hist(data['runtime'], bins=bins_time, edgecolor='black', color='lightgreen')
plt.xlabel("Runtime")
plt.ylabel("Frequency")
plt.title("Distribution of Runtime")
plt.show()

bins_rating = np.arange(6.0, 9.0, 0.5)
plt.hist(data['imdb_rating'], bins=bins_rating, edgecolor='black', color='lightcoral')
plt.xlabel("IMDB Rating")
plt.ylabel("Frequency")
plt.xticks(bins_rating)
plt.title("Distribution of IMDB Ratings")
plt.show()
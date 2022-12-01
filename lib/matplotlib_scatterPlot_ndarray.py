import matplotlib.pyplot as plt
from pandas_SeriesValuesToNdarray import features

plt.scatter(features[:50, 0], features[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(features[50:100, 0], features[50:100, 1], color='blue', marker='x', label='versicolor')
plt.show()
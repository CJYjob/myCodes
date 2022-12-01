from sklearn.model_selection import train_test_split
from numpy_manufactureNdarrayValues import label
from pandas_SeriesValuesToNdarray import features

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)

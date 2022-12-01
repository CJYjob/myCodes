from tensorflow_compileNeuralNetworkModel import model
from sklearn_splitDataToTestTrain import X_train, X_test, y_train, y_test

model.fit(X_train, y_train, epochs=30)
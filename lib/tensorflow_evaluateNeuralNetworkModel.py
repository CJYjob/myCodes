from tensorflow_trainingNeuralNetworkModel import model
from sklearn_splitDataToTestTrain import X_train, X_test, y_train, y_test

model.evaluate(X_test, y_test, verbose=2)
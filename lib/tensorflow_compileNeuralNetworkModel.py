from tensorflow_buildNeuralNetworkModel import model

# 신경망에서 사용할
#   옵티마이저(optimizer)
#   손실함수(loss)
#   지표(metrics)
# 설정
model.compile(optimizer='sgd',
    loss = 'binary_crossentropy',
    metrics=['accuracy'])
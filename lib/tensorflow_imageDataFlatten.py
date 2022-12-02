# https://opentutorials.org/module/5268/29787
# 2차원 형태로 표현된 이미지를 
# 모델 내에서 1차원 형태로 변환해주는 역할.
# 입력층에서 1차원 형태로 이미지를 받아들이기 때문에 사용

import tensorflow_buildNeuralNetworkModel
from tensorflow.keras.layers import Flatten

model.add(Flatten(input_shape=(x, y)))

# 다른 표현
'''
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(64,
          kernel_regularizer=regularizers.l2(0.01),
          activity_regularizer=regularizers.l1(0.01)),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
'''
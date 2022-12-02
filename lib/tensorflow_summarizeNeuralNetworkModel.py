import numpy as np
from tensorflow_compileNeuralNetworkModel import model

# 모델에 input을 줘서, build.
model(np.random.rand(20,30)) 

# build되지 않으면, 입력층 노드 수가 불명확함으로, summary 출력 불가.
model.summary()
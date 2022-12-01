import tensorflow as tf

# 단일 출력층으로만 구성된 모델.
#   출력층 노드 수 : 1개
#   출력층 활성화 함수 : sigmoid
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Dense(1, activation='sigmoid')
    ]
)

# 위의 모델과 동일하나, 다른 표현
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

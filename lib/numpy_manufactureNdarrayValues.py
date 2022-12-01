import numpy as np
import pandas as pd
from pandas_readDataFrame import df

# ndarray 생성
label = df.iloc[0:100, 4].values

# ndarray의 value를 지정된 조건에 맞으면 1, 아니면 0 으로 변경
label = np.where(label == 'Iris-setosa', 0, 1)

# ndarray의 value 데이터 타입 지정
label.astype(object)
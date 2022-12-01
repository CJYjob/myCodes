from pandas_readDataFrame import df

# 시리즈의 값들을 ndarray 형태로 가져옴
print(df.iloc[0:100, 4].values)
print(type(df.iloc[0:100, 4].values))
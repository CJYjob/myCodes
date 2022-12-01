import pandas as pd
from pandas_readDataFrame import df

# index 사용
print(df.iloc[0:100, 2:4]) # df.iloc[row_start:row_end, column_start:column_end]
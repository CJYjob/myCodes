import pandas as pd

def exploreData(df) :
    print('df shape : \n', df.shape) 
    print('df.head(3) : \n ', df.head(3))
    print('df.info() : \n ', df.info())
    print('df.describe() : \n', df.describe())

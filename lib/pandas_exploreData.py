import pandas as pd

def exploreData(df) :
    print('df shape : \n')
    df.shape
    print('\n df.head(3) : \n ', df.head(3))
    print('\n df.info() : \n ', df.info())
    print('\n df.describe() : \n', df.describe())

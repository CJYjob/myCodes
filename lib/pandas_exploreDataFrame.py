import pandas as pd

def exploreDataFrame(df) :
    print(df.shape, '\n')
    print(df.head(3), '\n')
    prnit(df.info(), '\n')
    print(df.describe(), '\n')
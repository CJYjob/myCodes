import pandas as pd

def exploreDataFrame(df) :

    print(df.shape, '\n')

    print(df.head(3), '\n')
    print('\n')

    print(df.info(), '\n')
    print('\n')

    print(df.describe(), '\n')
    print('\n')
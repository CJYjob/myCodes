import pandas as pd

def exploreData(df) :
    print(df.shape, '\n')
    print(df.head(3), '\n')
    print(df.info(), '\n')
    print(df.describe(), '\n')
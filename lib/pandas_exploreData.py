import pandas as pd

def exploreData(df) :
    print(df.shape, df.head(3), df.info(), df.describe())

import pandas as pd
import lib.debug_log

def exploreData(df) :
    print(df.shape, '\n')
    debug('df.shape', __name__)
    print(df.head(3), '\n')
    print('\n')
    print(df.info(), '\n')
    print('\n')
    print(df.describe(), '\n')
    print('\n')
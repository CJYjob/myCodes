import pandas as pd

# DataFrame 기본 탐색 진행
#   파라미터
#       df : 탐색할 DataFrame
#   처리
#       df의 shape, head(3), info, describe 출력
#   반환
#       없음
def exploreDataFrame(df) :
    print(df.shape, '\n')
    print(df.head(3), '\n')
    print(df.info(), '\n')
    print(df.describe(), '\n')
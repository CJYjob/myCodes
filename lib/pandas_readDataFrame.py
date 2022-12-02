import pandas as pd

# csv 파일 읽어오기
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

# excel 파일 읽어오기
df2 = pd.read_excel('https://ds-lecture-data.s3.ap-northeast-2.amazonaws.com/MouseProtein/mouse_protein_X.xls', header=None)
df2_label = pd.read_excel('https://ds-lecture-data.s3.ap-northeast-2.amazonaws.com/MouseProtein/mouse_protein_label.xls', header=None)

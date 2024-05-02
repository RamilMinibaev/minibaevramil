import pandas as pd
data = pd.read_csv ("nba.csv")
col = data.head (3)
col
clm = list (col)
for i in clm:
    print(col[i][2])
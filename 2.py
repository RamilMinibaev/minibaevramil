import pandas as pd
data = pd.read_csv ("nba.csv")
for i, j in data.iterrows():
    print (i, j)
    print ()

import pandas as pd
data = pd.read_csv ("nba.csv")
for key, value in data.iteritems():
    print(key, value)
    print()
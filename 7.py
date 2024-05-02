import pandas as pd
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}
df = pd. DataFrame (dict)
print(df)
colums = list (df)
for i in colums:
    print(df[i][2])
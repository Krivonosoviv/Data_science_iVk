import pandas as pd
ratings = pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/movies/ratings1.csv', sep=',')
+pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/movies/ratings2.csv', sep=',')
dates=pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/movies/dates.csv', sep=',')
movies=pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/movies/movies.csv', sep=',')
dates['date']=pd.to_datetime (dates['date'],dayfirst=True)
max=dates['date'].dt.year
print(max.mode())
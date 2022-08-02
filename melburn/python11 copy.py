import pandas as pd
data = pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/citibike-tripdata.csv', sep=',')
def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
    else:
        return 'else'
data['time_of_day'] = data['starttime'].dt.hour.apply(get_time_of_day)
a = data[data['time_of_day'] == 'day'].shape[0]
b = data[data['time_of_day'] == 'night'].shape[0]
print(round(a / b))

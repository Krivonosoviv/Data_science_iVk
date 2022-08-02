from turtle import title
import pandas as pd
joined = pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/movies/ratings_movies.csv', sep=',')
import re 
def get_year_release(joined):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', 'title') 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
joined['date'] = pd.to_datetime(joined['date'])
joined['year_rating'] = joined['date'].dt.year
pivot = joined.pivot_table(
    index='year_rating',
    columns='genres',
    values='rating',
    aggfunc='mean'
)
print(pivot)
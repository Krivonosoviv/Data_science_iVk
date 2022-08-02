import pandas as pd
student_data = pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/SKILLFACTORY/Melburn/data/students_performance.csv', sep=',')
a = student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()
b = student_data[student_data['race/ethnicity'] == 'group C']['writing score'].mean()
print(round(abs(a - b)))
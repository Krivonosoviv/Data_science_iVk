import pandas as pd
melb_df = pd.read_csv('/Users/igorkrivonosov/Desktop/IDE/game.py/melb_data_fe.csv', sep=',')
pivot = melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='mean',
)
max_unit_price = pivot['unit'].max()
print(pivot[pivot['unit'] == max_unit_price].index[0])

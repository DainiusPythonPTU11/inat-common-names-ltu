from os import getcwd
from glob import glob
import pandas as pd

dir_path = f'{getcwd()}\\Files\\Results'

csv_files_list = glob(f'{dir_path}\\observations-*.csv')

df_old = pd.read_csv(csv_files_list[0], encoding='UTF-8')
df_new = pd.read_csv(csv_files_list[1], encoding='UTF-8')

df_old = df_old.convert_dtypes()
df_new = df_new.convert_dtypes()

df_old['catena'] = df_old['scientific_name'].astype(str) + df_old['common_name'].astype(str)
df_new['catena'] = df_new['scientific_name'].astype(str) + df_new['common_name'].astype(str)

df_old = df_old.iloc[:, [27, 0, 1, 2, 3]]
df_new = df_new.iloc[:, [27, 0, 1, 2, 3]]

df_old.to_csv(f'{dir_path}\\Old.csv')
df_new.to_csv(f'{dir_path}\\New.csv')

df = pd.merge(df_old, df_new, how='outer', on='catena')
print(df.head())

df.to_csv(f'{dir_path}\\Catena.csv')

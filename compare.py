from os import getcwd
from glob import glob
import pandas as pd

dir_path = f'{getcwd()}\\Files\\Results'

csv_files_list = glob(f'{dir_path}\\observations-*.csv')

old = pd.read_csv(csv_files_list[0], encoding='UTF-8').convert_dtypes()
new = pd.read_csv(csv_files_list[1], encoding='UTF-8').convert_dtypes()

old['catena'] = old['scientific_name'].astype(str) + old['common_name'].astype(str)
new['catena'] = new['scientific_name'].astype(str) + new['common_name'].astype(str)

old = old.iloc[:, [27, 0, 1, 2, 3]]
new = new.iloc[:, [27, 0, 1, 2, 3]]

df = pd.merge(old, new, how='outer', on='catena', suffixes=('_old', '_new'))

old_filename = csv_files_list[0][csv_files_list[0].find('observations-') + 13:csv_files_list[0].find('.csv')-24]
new_filename = csv_files_list[1][csv_files_list[1].find('observations-') + 13:csv_files_list[1].find('.csv')-24]

df.to_csv(f'{dir_path}\\Pakeitimai {old_filename}-{new_filename}.csv')

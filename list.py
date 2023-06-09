from os import getcwd
from glob import glob
from zipfile import ZipFile
import pandas as pd

# Du .zip failus iš aplanko Duomenys pasibandymui nukopijuokite į aplanką Files. Rezultatą rasite aplanke Results.

dir_path = f'{getcwd()}\\Files'

i = ''

for i in glob(f'{dir_path}\\*.zip'):
    ZipFile(i).extractall(dir_path)

latest_file = i[i.find('observations-') + 13:i.find('.csv')]

df = pd.DataFrame()

for i in glob(f'{dir_path}\\observations-*.csv'):
    df = pd.concat([df, pd.read_csv(i, encoding='UTF-8', low_memory=False).drop(columns=['species_guess'])])

df = df.convert_dtypes().reset_index(drop=True)

# print(df.info())

df['created_at'] = pd.to_datetime(df['created_at'], utc=True)

print('\n', '       Paskutinio stebėjimo laikas:', pd.to_datetime(max(df['created_at'])))
ignore_datetime = input('Neįtraukti duomenų nuo (YYYY-MM-DD): ') + ' 00:00:00+00:00'

df = df[df.created_at < ignore_datetime]

latest_datetime = str(pd.to_datetime(max(df['created_at'])))[:19].replace(':', '_') + ' UTC'

df = df.drop(columns=['created_at'])

taxon_id_count = df.value_counts('taxon_id').to_frame()

df = df.drop_duplicates()

df['common_name'] = df['common_name'].str.capitalize()

taxon_id_count.join(df.set_index('taxon_id'), on='taxon_id').sort_values(by='scientific_name').to_csv(
    f'{dir_path}\\Results\\observations-{latest_file} {latest_datetime}.csv')

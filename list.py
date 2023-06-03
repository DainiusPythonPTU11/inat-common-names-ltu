import os, glob, zipfile, pandas

dir_path = f'{os.getcwd()}\\Files'

for i in glob.glob(f'{dir_path}\\*.zip'): zipfile.ZipFile(i).extractall(dir_path)

df = pandas.DataFrame()

for i in glob.glob(f'{dir_path}\\observations-*.csv'): df = pandas.concat([df, pandas.read_csv(i, encoding='UTF-8')])

df = df.convert_dtypes().reset_index(drop=True)

df.sort_values(by='created_at').to_csv(f'{dir_path}\\df.csv') # Čia
print('\n', '                             Paskutinio stebėjimo laikas:', max(df['created_at']))
data = input('Nuo kurios dienos nereikia įtraukti duomenų? (YYYY-MM-DD): ')+' 00:00:00+0000'
print('                            Nebus įtraukiami duomenys nuo:', data)

df['created_at'] = pandas.to_datetime(df['created_at'], utc=True)

df = df[df.created_at < data]

df.to_csv(f'{dir_path}\\dfaltered.csv')

df = df.drop(columns=['created_at', 'species_guess'])

uv = df.value_counts('taxon_id').to_frame()

df = df.drop_duplicates()

df['common_name'] = df['common_name'].str.capitalize()

uv.join(df.set_index('taxon_id'), on='taxon_id').sort_values(by='scientific_name').to_csv(f'{dir_path}\\apjungtas.csv')
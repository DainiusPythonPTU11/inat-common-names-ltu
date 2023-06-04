import os, glob, zipfile, pandas

dir_path = f'{os.getcwd()}\\Files'
df = pandas.DataFrame()

for i in glob.glob(f'{dir_path}\\*.zip'):
    zipfile.ZipFile(i).extractall(dir_path)
    latest_file = i[i.find('observations-') + 13:i.find('.csv')]

for i in glob.glob(f'{dir_path}\\observations-*.csv'):
    df = pandas.concat([df, pandas.read_csv(i, encoding='UTF-8', low_memory=False).drop(columns=['species_guess'])])

df = df.convert_dtypes().reset_index(drop=True)

print('\n', '       Paskutinio stebėjimo laikas:', pandas.to_datetime(max(df['created_at']), utc=True))
data = input('Neįtraukti duomenų nuo (YYYY-MM-DD): ') + ' 00:00:00+00:00'

df['created_at'] = pandas.to_datetime(df['created_at'], utc=True)
df = df[df.created_at < data]

latest_datetime = str(pandas.to_datetime(max(df['created_at']), utc=True))[:19].replace(':', '_') + ' UTC'

df = df.drop(columns=['created_at'])

taxon_count = df.value_counts('taxon_id').to_frame()

df = df.drop_duplicates()
df['common_name'] = df['common_name'].str.capitalize()

taxon_count.join(df.set_index('taxon_id'), on='taxon_id').sort_values(by='scientific_name').to_excel(
    f'{dir_path}\\Results\\observations-{latest_file} {latest_datetime}.xlsx', sheet_name=f'iNaturalist{latest_file}')

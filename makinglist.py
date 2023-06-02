import glob, zipfile, pandas

dir_path = 'C:\\Users\CodeAcademy\Desktop\inat-common-names-ltu\Files'

df = pandas.DataFrame()

for i in glob.glob((f'{dir_path}\*.zip')): zipfile.ZipFile(i).extractall(dir_path)

for i in glob.glob((f'{dir_path}\observations-*.csv')): df = pandas.concat([df, pandas.read_csv(i, encoding='UTF-8')])

df = df.convert_dtypes()
df = df.drop(['species_guess'], axis=1)
df = df.drop(['created_at'], axis=1)
df = df.reset_index(drop=True)
unikalus = df.value_counts('taxon_id').to_frame()
df = df.drop_duplicates()
df.to_csv(f'{dir_path}\\df.csv')

# df1 = pandas.DataFrame(df.taxon_id.unique())
# unikalus = df.value_counts('taxon_id').to_frame()
unikalus = unikalus.reset_index()
unikalus.to_csv(f'{dir_path}\\unikalus.csv')
# sujungta = pandas.merge(unikalus, df, on='taxon_id', how='left')
apjungtas = unikalus.join(df.set_index('taxon_id'), on='taxon_id')
apjungtas = apjungtas.sort_values(by='count', ascending=False)
apjungtas.to_csv(f'{dir_path}\\apjungtas.csv')
# apjungtas.to_excel(f'{dir_path}\\apjungtas.xlsx')
print(apjungtas.info())

# , dtype={'taxon_id': 'Int64'}
# dtype={'scientific_name': str, 'taxon_id': 'Int64', 'taxon_genushybrid_name': str, 'taxon_form_name': str})])
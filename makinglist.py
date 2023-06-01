import glob, zipfile, pandas

dir_path = 'D:\Python\PycharmProjects\inat-common-names-ltu\Files'

df = pandas.DataFrame()

for i in glob.glob((f'{dir_path}\*.zip')): zipfile.ZipFile(i).extractall(dir_path)

for i in glob.glob((f'{dir_path}\observations-*.csv')): df = pandas.concat([df, pandas.read_csv(i, encoding='UTF-8')])

df = df.convert_dtypes()
print(df.dtypes)
print(df.head())

unikalus = df.value_counts('taxon_id').to_frame()
unikalus.reset_index()
print(unikalus.head())

sujungta = pandas.merge(unikalus, df, on='taxon_id', how='left')
# joined = unikalus.join(df, on='taxon_id', how='left')
# unikalus.to_csv(f'{dir_path}\\unikalus.csv')
# joined.to_csv(f'{dir_path}\joined.csv')
sujungta.to_csv(f'{dir_path}\sujungta.csv')
# print(joined.info())
print(sujungta.info())

# , dtype={'taxon_id': 'Int64'}
# dtype={'scientific_name': str, 'taxon_id': 'Int64', 'taxon_genushybrid_name': str, 'taxon_form_name': str})])
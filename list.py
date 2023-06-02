import glob, zipfile, pandas

# dir_path = 'C:\\Users\CodeAcademy\Desktop\inat-common-names-ltu\Files'
dir_path = 'D:\\Python\PycharmProjects\inat-common-names-ltu\Files'

for i in glob.glob((f'{dir_path}\\*.zip')): zipfile.ZipFile(i).extractall(dir_path)

df = pandas.DataFrame()

for i in glob.glob((f'{dir_path}\\observations-*.csv')): df = pandas.concat([df, pandas.read_csv(i, encoding='UTF-8')])

df = df.convert_dtypes().reset_index(drop=True)

# Pasidaryti nukirpimą pagal datą ir laiką

df = df.drop(columns=['created_at', 'species_guess'])

tc = df.value_counts('taxon_id').to_frame()

df = df.drop_duplicates()

df['common_name'] = df['common_name'].str.capitalize()

tc.join(df.set_index('taxon_id'), on='taxon_id').sort_values(by='scientific_name').to_csv(f'{dir_path}\\apjungtas.csv')

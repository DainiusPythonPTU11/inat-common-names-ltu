from os import getcwd
from glob import glob
import pandas as pd

dir_path = f'{getcwd()}\\Files\\Results'

for i in glob(f'{dir_path}\\observations-*.csv'):
    pass
# scientific_name + zzz + common_name iš failo1
# scientific_name + zzz + common_name iš failo2
# Yra faile1, nėra faile2 -> prapuolė
# Yra faile2, nėra faile1 -> atsirado
from zipfile import ZipFile
import pandas as pd

with ZipFile('NewsAggregatorDataset.zip', 'r') as f:
    # print(f.namelist())
    f.extractall('data/')
with open('./data/readme.txt', 'r', encoding='utf-8') as f:
    print(f.read())

df = pd.read_csv('./data/newsCorpora.csv',
                 encoding='utf-8', sep='¥t', header=None)
print(df)

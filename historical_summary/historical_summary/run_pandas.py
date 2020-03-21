import pandas as pd
import scrapy

dataset = pd.read_csv(r'./db.csv', sep=',')
size_dataset = (len(dataset))
database_csv = dataset.head(size_dataset)
print (database_csv)
print('---------------Resumo de 5 Anos---------------')
dataset_5_anos = dataset.loc[dataset['periodo']=='5 Anos']
ascending_dataset = dataset_5_anos.sort_values(by='variacao', ascending=False)
print (ascending_dataset)

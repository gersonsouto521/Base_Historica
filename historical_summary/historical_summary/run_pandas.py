import pandas as pd
import scrapy

dataset = pd.read_csv(r'./db.csv', sep=',')
size_dataset = (len(dataset))
database_csv = dataset.head(size_dataset)
print (database_csv)



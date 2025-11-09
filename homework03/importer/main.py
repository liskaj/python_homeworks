from datetime import datetime, timedelta
from pathlib import Path
import os
import pandas as pd
from pymongo import MongoClient

mongo_uri = os.environ['MONGO_URI']
csv_path = '/data/pwr_consumption.csv'

client = MongoClient(mongo_uri)
collection = client['energy']['power_consumption']

df = pd.read_csv(csv_path)
df.rename(columns={
    'Datum': 'timestamp',
    'VT [kW]': 'load_high',
    'NT [kW]': 'load_low'}, inplace=True)
documents = []
for index, row in df.iterrows():
    value = row['timestamp']
    if value.endswith('24:00:00'):
        day_part = value.split(' ')[0]
        dt = datetime.strptime(day_part, '%d.%m.%Y') + timedelta(days=1)
        dt = dt.replace(hour=0, minute=0, second=0)
    else:
        dt = datetime.strptime(value, '%d.%m.%Y %H:%M:%S')
    document = {
        'timestamp': dt.timestamp(),
        'load_high': row['load_high'],
        'load_low': row['load_low']
    }
    documents.append(document)
collection.insert_many(documents)
print(f'Import completed:  {len(documents)} documents')
import csv
import requests
import random

DATA_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey=17POZWY30SQZNMJI'

response = requests.get(DATA_URL)
data_json = response.json()
data = data_json['Time Series (Daily)']

csv_file = open('./data.csv', 'w')
writer = csv.writer(csv_file)

sample_item = key, val = random.choice(list(data.items()))
# print(sample_item)
header_list = list(sample_item[1].keys())
header = [i[3:].upper() for i in header_list]
header.insert(0, 'DATE')
# print(header_list)
writer.writerow(header)

for date in data:
    # print(date)
    row = list(data[date].values())
    row.insert(0, date)
    writer.writerow(row)
    
    # for item in data[date]:
        # print(item, date[item])


csv_file.close()

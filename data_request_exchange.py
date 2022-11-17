import pandas as pd
from datetime import datetime

now = datetime.now()

calls_df,  = pd.read_html('https://myfin.by/currency/cb-rf')
print("Время запроса информации: ")
print(now.strftime("%Y-%m-%d"))
print(calls_df)
print(calls_df. to_csv("save_data_exchange.csv", index=False))

calls_df.describe()

with open('save_data_exchange_log.csv', 'w', encoding='utf-8') as my_file:
   my_file.write("Время запроса информации: " +now.strftime("%Y-%m-%d" ))

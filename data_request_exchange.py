import pandas as pd
# from datetime import datetime as dt
import save_data_exchange_log as sdel

def get_data_request_exchange(data):
   
   # calls_df, = pd.read_html('https://myfin.by/currency/cb-rf')
   calls_df, = pd.read_html(data)
   sdel.get_save_data_exchange_log()
   return calls_df,



# now = dt.now()
# calls_df, = pd.read_html('https://myfin.by/currency/cb-rf')
# print("Время запроса информации: " + 
#                      (now.strftime("%Y-%m-%d")) + (now.strftime('%H:%M')))
# print(calls_df)
# print(calls_df. to_csv("save_data_exchange.csv", index=False))

# calls_df.describe()

# with open('save_data_exchange_log.csv', 'a', encoding='utf-8') as my_file:
#    my_file.write('{} запрос информации {}\n'
#                     .format(now.strftime("%Y-%m-%d"), now.strftime('%H:%M')))

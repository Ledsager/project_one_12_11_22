import pandas as pd
import requests
# from datetime import datetime as dt
import save_data_exchange_log as sdel

# запрос информации с сайта в html виде
def get_data_request_exchange_html():
   data = 'https://myfin.by/currency/cb-rf'
   data_fr, = pd.read_html(data)
   data_fr_in = [i for i in data_fr.values.tolist()] # преобразование dataframe в список
   # for list_element in data_fr_in:
   #    list_element.pop(2) #  удаление 3го столбца списка
      # calls_df_data1=[['Доллар', 60.3741, '60.7379 +0.36', 'USD', 1], ['Евро', 62.4484, '62.1245 -0.32', 'EUR', 1], ['Украинская гривна', 16.3495, '16.4459 +0.1', 'UAH', 10], ['Белорусский рубль', 25.0754, '25.0921 +0.02', 'BYN', 1], ['Казахстанский тенге', 13.152, '13.2315 +0.08', 'KZT', 100], ['Китайский юань', 8.472, '8.4756 0', 'CNY', 1]]
   data_fr_out = [i for i in data_fr_in 
                     if ('USD' in i) or ('EUR' in i) or ('KZT' in i) or ('TRY' in i) or ('UZS' in i) or ('AZN' in i)]
   
   sdel.get_save_data_exchange_log()
   return data_fr_out

def get_data_request_exchange_api():
   API_KEY = 'fa5dec1241aa18580ecb2909'
   url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/RUB'

   # 
   response = requests.get(f'{url}').json()
   # 
   currencies = dict(response['conversion_rates'])
   currencies = [list(i) for i in currencies.items()
                           if ('USD' in i) or ('EUR' in i) or ('KZT' in i) or ('TRY' in i) or ('UZS' in i) or ('AZN' in i)]

   return currencies

# get_data_request_exchange_html()
# get_data_request_exchange_api()


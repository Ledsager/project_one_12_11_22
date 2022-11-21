import csv
from datetime import datetime as dt
import pathlib

# import pandas as pd
# from datetime import datetime as dt


# def get_save_data_exchange(data):
# # print("Время запроса информации: " +
# #                     (now.strftime("%Y-%m-%d")) + (now.strftime('%H:%M')))
# # print(calls_df)
#    print(data)

#    print(data.to_csv("save_data_exchange.csv", index=False))

def a_save_data(data,header_file_csv=None):
   if header_file_csv==None:
      with open("save_data_exchange.csv", 'a', newline='', encoding='utf-8') as f:
         writer = csv.writer(f)
         writer.writerows(data)
         writer.writerow('')
   else:
      with open("save_data_exchange.csv", 'a', newline='', encoding='utf-8') as f:
         writer = csv.writer(f)
         writer.writerow(header_file_csv)
         writer.writerows(data)
         writer.writerow('')


def get_save_data_exchange(data):

   time_now = dt.now().strftime('%H:%M')
   date_now = dt.now().strftime('%Y-%m-%d %H:%M')
   print(time_now + ' ' + date_now)
   # data = [
   #      ['доллар', 60.37, 'USD', 1],
   #      ['Евро', 62.44, 'EUR', 1],
   #      ['Казахстанский тенге', 13.1520, 'KZT', 100],
   #      ['Турецкая лира', 3.2437, 'TRY', 1],
   #      ['Узбекский сум', 53.8661, 'UZS', 10000],
   #      ['Азербайджанский манат', 35.5142, 'AZN', 1]
   #  ]

   # i=0
   # for list_element in data:
   #    if i==0:
   #       list_element.insert(0, date_now)
   #    else:
   #       list_element.insert(0, '')
   #    i+=1


   header_file_csv = ['Валюта', 'Курс', 'Код', 'Единиц']

   print(data)

   path = pathlib.Path('save_data_exchange.csv')  # путь к файлу
   # проверка существование файла
   if path.exists(): 
      with open("save_data_exchange.csv",'r', encoding='utf-8') as f:
         header = f.readline()
         # print(header)
      if header == ('Дата,Валюта,Курс,Код,Единиц\n'):
         a_save_data(data)
      else:
         a_save_data(data,header_file_csv)
   else:
      a_save_data(data,header_file_csv)


# # get_save_data_exchange()


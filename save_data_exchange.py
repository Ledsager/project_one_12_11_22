import copy
import csv
from datetime import datetime as dt
import pathlib


def a_save_data(data, path, header_file_csv=None):
   if header_file_csv == None:
      print (path)
      with open(path, 'a', newline='', encoding='utf-8') as f:
         writer = csv.writer(f)
         writer.writerows(data)
         writer.writerow('')
   else:
      with open(path, 'a', newline='', encoding='utf-8') as f:
         writer = csv.writer(f)
         writer.writerow(header_file_csv)
         writer.writerows(data)
         writer.writerow('')


def get_save_data_exchange(data):
   data_exchange=copy.deepcopy(data)
   time_now = dt.now().strftime('%H:%M')
   date_now = dt.now().strftime('%Y-%m-%d %H:%M')
   print(time_now + ' ' + date_now)
   i=0
   for list_element in data_exchange:
      if i==0:
         list_element.insert(0, date_now)
      else:
         list_element.insert(0, '')
      i+=1
   # if len(data_exchange[0])>3:
   #    header_file_csv = ['Дата', 'Валюта', 'Курс', 'Код', 'Единиц']
   # else:
   #    header_file_csv = ['Код валюты', 'Курс']
   if len(data_exchange[0]) > 3:
      path = pathlib.Path('save_data_for_html.csv')  # путь к файлу
      path_csv="save_data_for_html.csv"
   # проверка существование файла
      a_save_data(data_exchange, path_csv)
   else:
      path = pathlib.Path('save_data_for_api.csv')  # путь к файлу
      path_csv="save_data_for_api.csv"
      # проверка существование файла
      a_save_data(data_exchange, path_csv)

   # path = pathlib.Path('save_data_exchange.csv')  # путь к файлу
   # проверка существование файла
   # if path.exists():
   #    a_save_data(data_exchange)
   #    with open("save_data_exchange.csv",'r', encoding='utf-8') as f:
   #       header = f.readline()
   #       # print(header)
   #    if header == ('Дата,Валюта,Курс,Код,Единиц\n'):
   #       a_save_data(data_exchange)
   #    else:
   #       a_save_data(data_exchange,header_file_csv)
   # else:
   #    a_save_data(data_exchange,header_file_csv)

# # get_save_data_exchange()

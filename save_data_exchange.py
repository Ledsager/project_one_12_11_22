import copy
import csv
from datetime import datetime as dt
import pathlib


def a_save_data(data, path, header_file_csv=None):
   
   if header_file_csv == None:
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
   
   for list_element in data_exchange:
      list_element.insert(0, '')
     
   if len(data_exchange[0])>3:
      header_file_csv = ['Код', 'Курс', 'Единиц']
      header_file_csv.insert(0, date_now)
      path_csv = ''
      path_csv="save_data_for_html.csv"

   else: # len(data_exchange[0]) > 2:
      header_file_csv = ['Код валюты', 'Курс']
      header_file_csv.insert(0, date_now)
      path_csv = ''
      path_csv="save_data_for_api.csv"
   print(path_csv)
   path = pathlib.Path(path_csv)  # путь к файлу
   # проверка существование файла
   if path.exists():
      
      with open(path_csv,'r', encoding='utf-8') as f:
         header = f.readline()
      # print(header)
      if ('Код,Курс,Единиц' in header) or ('Код валюты,Курс' in header):
         a_save_data(data_exchange, path_csv)
      else:
         a_save_data(data_exchange, path_csv, header_file_csv)
   else:
      a_save_data(data_exchange, path_csv, header_file_csv)

# get_save_data_exchange()

from datetime import datetime as dt

def get_save_data_exchange_log():
   now = dt.now()
   with open('save_data_exchange_log.csv', 'a', encoding='utf-8') as my_file:
      my_file.write('{} запрос информации {}\n'
                     .format(now.strftime("%Y-%m-%d"), now.strftime('%H:%M')))
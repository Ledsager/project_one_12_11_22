# import pandas as pd
# from datetime import datetime as dt


def get_save_data_exchange(date):
# print("Время запроса информации: " + 
#                     (now.strftime("%Y-%m-%d")) + (now.strftime('%H:%M')))
# print(calls_df)
   print(date.to_csv("save_data_exchange.csv", index=False))
import data_request_exchange as dre
import save_data_exchange as sde
# import save_data_exchange_log as sdel


data='https://myfin.by/currency/cb-rf'
calls_df, = dre.get_data_request_exchange(data)
print(calls_df)
sde.get_save_data_exchange(calls_df)

# sdel.get_save_data_exchange_log()
import data_request_exchange as dre
import save_data_exchange as sde
import data_viewer_output as dvo
import data_processing_request as dpr
import data_output_somewhere as dos

# import save_data_exchange_log as sdel


data_url = 'https://myfin.by/currency/cb-rf'
data_fr, = dre.get_data_request_exchange(data_url)
data = dpr.get_data_processing_request(data_fr)
print(data)
sde.get_save_data_exchange(data)
dvo.get_data_viewer_output(data)

# test1 = [['доллар', 60.37, 'USD', 1], ['Евро', 62.44, 'EUR', 1], ['Казахстанский тенге', 13.1520, 'KZT', 100], ['Турецкая лира', 3.2437, 'TRY', 1], ['Узбекский сум', 53.8661, 'UZS',10000], ['Азербайджанский манат', 35.5142, 'AZN', 1]]
# sde.get_save_data_exchange(test1)
# dvo.get_data_viewer_output(test1)

# sdel.get_save_data_exchange_log()

import pandas as pd

def data_processing_request():
    amount = ''
    valid = False
    while not valid:
        try:
            amount = input('Для конвертации в рубли одну из валют вышеприведённого списка, для начало введите сумму: ')
            if amount < 0:
                print('Введите положительные числа!!!')
            else:
                amount = float(amount)
                valid = True
        except:
            print('Введите числовое значение')
    
    currency_course = ''
    valid = False
    while not valid:
        try:
            currency_course = input('Введите курс иностранной валюты из вышеприведённого списка, которую хотите конвертировать: ')
            if currency_course < 0:
                print('Введите положительные числа!!!')
            else:
                currency_course = float(currency_course)
                valid = True
        except:
            print('Введите числовое значение')

    quality = ''
    valid = False
    while not valid:
        try:
            quality = input('Введите количество единиц выбранной валюты из вышеприведённого списка(последнее значение в списке валют)') 
            if quality < 0:
                print('Введите положительные числа!!!')
            else:
                quality = float(quality)
                valid = True
        except:
            print('Введите числовое значение')

# Выбор валют с которыми мы будем работать
# def get_data_processing_request(data_fr):

#     data_fr_in=[i for i in data_fr.values.tolist()] # преобразование dataframe в список
#     for list_element in data_fr_in:
#         list_element.pop(2) #  удаление 3го столбца списка
#     # calls_df_data1=[['Доллар', 60.3741, '60.7379 +0.36', 'USD', 1], ['Евро', 62.4484, '62.1245 -0.32', 'EUR', 1], ['Украинская гривна', 16.3495, '16.4459 +0.1', 'UAH', 10], ['Белорусский рубль', 25.0754, '25.0921 +0.02', 'BYN', 1], ['Казахстанский тенге', 13.152, '13.2315 +0.08', 'KZT', 100], ['Китайский юань', 8.472, '8.4756 0', 'CNY', 1]]
#     data_fr_out=[i for i in data_fr_in # выбор валют для работы с ними
#                     if ('USD' in i) or ('EUR' in i) or ('KZT' in i) or ('TRY' in i) or ('UZS' in i) or ('AZN' in i)]
#     # for i in calls_df_data1:
#     #      for elem in i:
#     #         print(elem)
#     return (data_fr_out)

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


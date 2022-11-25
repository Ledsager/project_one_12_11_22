import csv
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.ttk import Combobox
import pandas as pd
from tkinter import *

import requests

def data_processing_request():
    data=[['USD', 60.3866], ['EUR', 62.7814], ['KZT', 13.0523], ['TRY', 3.2426], ['UZS', 53.808], ['AZN', 35.5215]]
    window = Tk()  
    window.title("Добро пожаловать в приложение PythonRu")  
    window.geometry('400x250')  
    combo1 = Combobox(window)
    combo2 = Combobox(window)  
    combo1['values'] = data[0:] # (1, 2, 3, 4, 5, "Текст")  
    combo2['values'] = data[0:] # 1, 2, 3, 4, 5, "Текст")
    combo1.current(1)  # установите вариант по умолчанию  
    combo2.current(2)
    combo1.pack(side=LEFT)
    combo2.pack(side=RIGHT)

    window.mainloop()

# data_processing_request()  
# API_KEY = 'fa5dec1241aa18580ecb2909'
# url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'


# response = requests.get(f'{url}').json()
# currencies = dict(response['conversion_rates'])

# with open('meintest.csv', 'w', newline='') as csvfile:
#     header_key = ['Currency', 'Exchange Rate']
#     new_val = csv.DictWriter(csvfile, fieldnames=header_key)

#     new_val.writeheader()
#     for new_k in currencies:
#         new_val.writerow({'Currency': new_k, 'Exchange Rate': currencies[new_k]})  

def convert_currency():
    print(data)
    # will execute the code when everything is ok
    try:
        # getting currency from first combobox
        source = [i[1] for i in data if from_currency_combo.get() == i[0]]
        # for i in data:
        #     print (from_currency_combo.get())
        # getting currency from second combobox
        destination = to_currency_combo.get()
        # getting amound from amount_entry
        amount = amount_entry.get()
        print(amount)
        print(destination)
        print(source)
        # formatted_result = f'{amount} {source} = {converted_result} {destination}'
        # adding text to the empty result label
        # result = (source / destination) * amount
        result_label.config(text='расчет тут')
    # will catch all the errors that might occur
    # ConnectionTimeOut, JSONDecodeError etc
    except:
        showerror(title='Ошибка',
                  message="An error occurred!!. Fill all the required field or check your internet connection.")


window = Tk()
window.geometry('300x300+500+200')
data=[['USD', 60.3866], ['EUR', 62.7814], ['KZT', 13.0523], ['TRY', 3.2426], ['UZS', 53.808], ['AZN', 35.5215]]

# df = pd.DataFrame(data)[0].tolist()
# print(df)

window.title('Перевод валют')
# фиксируем размер окна
window.resizable(height=FALSE, width=FALSE)

primary = '#C1C1FF'
secondary = '#0083FF'
white = '#FFFFFF'
optional = '#ff4800'

# the top frame
top_frame = Frame(window, bg=primary, width=300, height=80)
top_frame.grid(row=0, column=0)

# label for the text Currency Converter
name_label = Label(top_frame, text='Перевод валют', bg=primary, fg=white, pady=30, padx=24, justify=CENTER,
                   font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)

# the bottom frame
bottom_frame = Frame(window, width=300, height=250)
bottom_frame.grid(row=1, column=0)

# widgets inside the bottom frame
from_currency_label = Label(bottom_frame, text='Какая валюта:', font=('Poppins 10 bold'), justify=LEFT)
from_currency_label.place(x=5, y=10)

to_currency_label = Label(bottom_frame, text='В какую:', font=('Poppins 10 bold'), justify=RIGHT)
to_currency_label.place(x=160, y=10)

# this is the combobox for holding from_currencies
from_currency_combo = ttk.Combobox(bottom_frame, values=pd.DataFrame(data)[0].tolist(), width=14, font=('Poppins 10 bold'))
from_currency_combo.place(x=5, y=30)

# this is the combobox for holding to_currencies
to_currency_combo = ttk.Combobox(bottom_frame, values=pd.DataFrame(data)[0].tolist(), width=14, font=('Poppins 10 bold'))
to_currency_combo.place(x=160, y=30)

# the label for AMOUNT
amount_label = Label(bottom_frame, text='Количество валюты:', font=('Poppins 10 bold'))
amount_label.place(x=5, y=55)

# entry for amount
amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
amount_entry.place(x=5, y=80)

# an empty label for displaying the result
result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
result_label.place(x=5, y=115)

# an empty label for displaying the time
time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
time_label.place(x=5, y=135)

# the clickable button for converting the currency
convert_button = Button(bottom_frame, text="Расчитать", bg=secondary, fg=white, font=('Poppins 10 bold'),
                        command=convert_currency)
convert_button.place(x=5, y=165)

quit_button = Button(bottom_frame, text='Выход', bg=optional, fg=white, font=('Poppins 10 bold'),
                     command=window.destroy)
quit_button.place(x=235, y=165)

window.mainloop()

from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.ttk import Combobox
import pandas as pd
from tkinter import *


def convert_currency():

    data=[['USD', 60.3866], ['EUR', 62.7814], ['KZT', 13.0523], ['TRY', 3.2426], ['UZS', 53.808], ['AZN', 35.5215]]
    # 
    try:
        # 
        source = from_currency_combo.get()
        # source_f = [i[1] for i in data if dvo.from_currency_combo.get() == i[0]]
        source_f = [i[1] for i in data if source == i[0]]

        
        destination = to_currency_combo.get()
        # destination_f = [i[1] for i in data if dvo.to_currency_combo.get() == i[0]]
        destination_f = [i[1] for i in data if destination == i[0]]
        # 
        amount = amount_entry.get()
        # amount_f = float(dvo.amount_entry.get())
        amount_f = float(amount)
        
        result = (source_f[0] / destination_f[0]) * amount_f

        print(amount_f)
        print(destination_f)
        print(source_f)
        formatted_result = f'{amount} {source} = {result} {destination}'
        print(formatted_result)
        # выводим результат в окно конвертора
        result_label.config(text=formatted_result)
    except:
        showerror(title='Ошибка',
                  message="An error occurred!!. Fill all the required field or check your internet connection.")

def main_test(data=None):
    global  from_currency_combo
    global to_currency_combo
    global amount_entry
    global result_label
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


    top_frame = Frame(window, bg=primary, width=300, height=80)
    top_frame.grid(row=0, column=0)


    name_label = Label(top_frame, text='Перевод валют', bg=primary, fg=white, pady=30, padx=24, justify=CENTER,
                    font=('Poppins 20 bold'))
    name_label.grid(row=0, column=0)


    bottom_frame = Frame(window, width=300, height=250)
    bottom_frame.grid(row=1, column=0)


    from_currency_label = Label(bottom_frame, text='Какая валюта:', font=('Poppins 10 bold'), justify=LEFT)
    from_currency_label.place(x=5, y=10)

    to_currency_label = Label(bottom_frame, text='В какую:', font=('Poppins 10 bold'), justify=RIGHT)
    to_currency_label.place(x=160, y=10)


    from_currency_combo = ttk.Combobox(bottom_frame, values=pd.DataFrame(data)[0].tolist(), width=14, font=('Poppins 10 bold'))
    from_currency_combo.place(x=5, y=30)


    to_currency_combo = ttk.Combobox(bottom_frame, values=pd.DataFrame(data)[0].tolist(), width=14, font=('Poppins 10 bold'))
    to_currency_combo.place(x=160, y=30)


    amount_label = Label(bottom_frame, text='Количество валюты:', font=('Poppins 10 bold'))
    amount_label.place(x=5, y=55)


    amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
    amount_entry.place(x=5, y=80)


    result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
    result_label.place(x=5, y=115)


    time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
    time_label.place(x=5, y=135)


    convert_button = Button(bottom_frame, text="Расчитать", bg=secondary, fg=white, font=('Poppins 10 bold'),
                            command=convert_currency)
    convert_button.place(x=5, y=165)

    quit_button = Button(bottom_frame, text='Выход', bg=optional, fg=white, font=('Poppins 10 bold'),
                        command=window.destroy)
    quit_button.place(x=235, y=165)

    window.mainloop()

if __name__== '__main__':
    main_test()


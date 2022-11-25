import tkinter
import csv
from datetime import datetime as dt
from tkinter import *

def exchange_convert_t():
    print("В разработке")
    pass


def get_data_viewer_output(data):

    date_now = dt.now().strftime('%Y-%m-%d %H:%M')
    root = Tk()
    # root.geometry('250x250')
    root.title(f'Курс валют на сегодня - {date_now}')
    frame_color ='#4ca8ff' # палитра или рал цвета
    # btn2 = Button(root, width=40, text="Перевод валют", command=exchange_convert_t)  
    # btn2.pack(side=TOP, padx=10, pady=10)
    #r и c указывают нам место расположения меток
    r = 0
    for col in data:
        c = 0
        for row in col:
            #добавил стиль в меню и цвет
            print(row)
            lbl = Label(root, width = 20, height = 2, \
                                    text=row, relief = RIDGE, bg=frame_color)
            # label = Label(root, width = 20, height = 2, \
                                #   text = row, relief = RIDGE, bg=frame_color)
            lbl.grid(column=c, row=r)
            c += 1
        r += 1
    txt = Entry(root,width=20)
    # txt = Button(root, width=40, text="Перевод валют", command=exchange_convert_t)  
    # txt.grid(column=c+1, row=r+10)
    root.mainloop()

# data = [['Доллар', 60.3741, '60.7379 +0.36', 'USD', 1], ['Евро', 62.4484, '62.1245 -0.32', 'EUR', 1], ['Украинская гривна', 16.3495, '16.4459 +0.1', 'UAH', 10], ['Белорусский рубль', 25.0754, '25.0921 +0.02', 'BYN', 1], ['Казахстанский тенге', 13.152, '13.2315 +0.08', 'KZT', 100], ['Китайский юань', 8.472, '8.4756 0', 'CNY', 1]]
data = [['Доллар', 'USD'], ['Евро', 'EUR'], ['Украинская гривна', 'UAH'], ['Белорусский рубль', 'BYN'], ['Казахстанский тенге', 'KZT'], ['Китайский юань', 'CNY']]

get_data_viewer_output(data)
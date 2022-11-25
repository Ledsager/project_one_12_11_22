import tkinter
import csv
from datetime import datetime as dt
from tkinter import *

def exchange_convert_t():
    print("В разработке")
    pass


def get_data_viewer_output(data):

    date_now = dt.now().strftime('%Y-%m-%d %H:%M')
    root = tkinter.Tk()
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

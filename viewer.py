import tkinter
import csv
from datetime import datetime as dt

time_now = dt.now().strftime('%H:%M')
date_now = dt.now().strftime('%Y-%m-%d %H:%M')
root = tkinter.Tk()
root.title(f'Курс валют ЦБ РФ на сегодня - {date_now}')
frame_color ='#4ca8ff' # палитра или рал цвета

# open file
with open("save_data_exchange.csv", newline = "", encoding='utf-8') as file:
   reader = csv.reader(file)

   # r and c tell us where to grid the labels/r и c указывают нам место расположения меток
   r = 0
   for col in reader:
      c = 0
      for row in col:
        #добавил стиль в меню и цвет
         label = tkinter.Label(root, width = 20, height = 2, \
                               text = row, relief = tkinter.RIDGE, bg=frame_color)
         label.grid(row = r, column = c)
         c += 1
      r += 1

root.mainloop()
from argparse import OPTIONAL
from sre_parse import WHITESPACE
import data_request_exchange as dre
import save_data_exchange as sde
import data_viewer_output as dvo
import data_processing_request as dpr
import data_output_somewhere as dos
from flask import Flask
import save_data_exchange_log as sdel
from tkinter import *  
  
  
def exchange_html():
    data = dre.get_data_request_exchange_html()
    dvo.get_data_viewer_output(data)
    sde.get_save_data_exchange(data)
    # res = "Привет {}".format(txt.get())
    # lbl.configure(text=res)
    sde.get_save_data_exchange(data)

def exchange_api():
    data = dre.get_data_request_exchange_api()
    dvo.get_data_viewer_output(data)
    sde.get_save_data_exchange(data)

def exchange_convert():
    
    print("В разработке")
    pass

def button_menu():
    window = Tk()  
    window.title("Меню")  
    window.geometry('250x250')  
    # lbl = Label(window, text="Привет")  
    # lbl.grid(column=0, row=0)  
    # txt = Entry(window,width=10)  
    # txt.grid(column=2, row=0)  
    btn = Button(window, width=40, text="Запрос html (сайт myfin)", command=exchange_html)  
    btn.pack(side=TOP, padx=10, pady=10)
    btn1 = Button(window, width=40, text="Запрос api (сайт ...)", command=exchange_api)  
    btn1.pack(side=TOP, padx=10, pady=10)
    btn2 = Button(window, width=40, text="Перевод валют", command=exchange_convert)  
    btn2.pack(side=TOP, padx=10, pady=10)
    quit_button = Button(window, text='close', font=('Poppins 10 bold'),
                        command=window.destroy)
    quit_button.pack(side=TOP, padx=10, pady=10)
    window.mainloop()


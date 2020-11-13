from tkinter import *
from tkinter import messagebox
import datetime
from CreatePass import CreatePassword
from MessageTelegram import MessageTelegramBot


def Check(root):
    root=root
    
    root.geometry("300x500")
    root.title("Проверка кода")
    text_enter_code=Label(text="Введите код который пришел вам в мессенджер")
    enter_code=Entry()
    button_enter=Button(text="Проверить код",command=lambda: CheckCode())

    code=CreatePassword(6)
    finish_login=datetime.datetime.now()+datetime.timedelta(seconds=30)
    MessageTelegramBot(457498036,code)#Отправка кода в мессенджер#
    
    text_enter_code.pack()
    enter_code.pack()
    button_enter.pack()

    def CheckCode():
        if finish_login<datetime.datetime.now():
            messagebox.showerror("Плохо","Время на ввод кода вышло")
        else:
            if enter_code.get()==code:
                messagebox.showinfo("Отлично","Код верный")
            else:
                messagebox.showerror("Плохо","Код неверный")
    









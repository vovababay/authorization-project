from tkinter import *
from tkinter import messagebox
import datetime
from CreatePass import CreatePasswordForTelegram
from MessageTelegram import MessageTelegramBot
import config
from FaceAuthentication import webcam_face_recognizer

def Check(root, login):
    con=config.con
    cur=con.cursor()
    cur.execute(f"SELECT id_user_messenger FROM users WHERE login='{login}';")
    id_user=cur.fetchone()[0]
    root=root
    
    root.geometry("380x500")
    root.resizable(width=False, height=False)
    root.title("Проверка кода")
    text_enter_code=Label(text="Введите код который пришел вам в мессенджер")
    enter_code=Entry()
    button_enter=Button(text="Проверить код",command=lambda: CheckCode())

    code=CreatePasswordForTelegram(6)
    finish_login=datetime.datetime.now()+datetime.timedelta(seconds=30)
    MessageTelegramBot(id_user,code)#Отправка кода в мессенджер#
    
    text_enter_code.pack()
    enter_code.pack()
    button_enter.pack()

    def clear_code_check_form():
        text_enter_code.pack_forget()
        enter_code.pack_forget()
        button_enter.pack_forget()



    def CheckCode():
        if finish_login<datetime.datetime.now():
            messagebox.showerror("Плохо","Время на ввод кода вышло")
        else:
            if enter_code.get()==code:
                messagebox.showinfo("Отлично","Код верный, нажмите ок и посмотрите в камеру")
                temp = webcam_face_recognizer(login)
                #print(temp)
                if temp == True:
                    messagebox.showinfo('Удачно','Вы успешно авторизовались')
                    raise SystemExit
                else:
                    messagebox.showerror('Ошибка', 'Вы не прошли авторизацию')
                    raise SystemExit
            else:
                messagebox.showerror("Плохо","Код неверный")
    









from tkinter import *
from tkinter import messagebox
from AttemptsAccount import Authentify
import datetime
from CodeCheck import Check
from CreatePass import CreatePassword
from IsTodayLoginMessenger import ChekTodayLoginInMessenger
from ResetBoolDay import ResetBool
import time
from multiprocessing import *
import schedule











try:
    
    
    f=open("login.log","r")
    now_date=datetime.datetime.now()
    last_line = f.readlines()[-1]

    last_year=int(last_line[0:10].split('-')[0])
    last_month=int(last_line[0:10].split('-')[1])
    last_day=int(last_line[0:10].split('-')[2])

    if datetime.date(last_year,last_month,last_day)<now_date.date():
        ResetBool()
    
except:
    print("Не получилось сбросить день")
f.close()
f=open("login.log","a")
f.write("\n")
f.write(f"-----------------------------------------------------------------\n")
f.write(f"{datetime.datetime.now()} The program login is running\n")
f.close()

root=Tk()
root.geometry("300x500")
root.title("Войти в систему")








def login():
    
    f=open("login.log","a")
    f.write(f"{datetime.datetime.now()} The login window is open\n")
    f.close()
    text_enter_login=Label(text="Введите ваш логин:")
    enter_login=Entry()
    text_enter_password=Label(text="Введите ваш пароль:")
    enter_password=Entry(show="*")
    button_enter=Button(text="Войти",command=lambda: log_pass())

    
    
    text_enter_login.pack()
    
    enter_login.pack()
    
    text_enter_password.pack()
    
    enter_password.pack()
    
    button_enter.pack()

    
    def clear_login_form():
        text_enter_login.pack_forget()
        enter_login.pack_forget()

        text_enter_password.pack_forget()
        enter_password.pack_forget()

        button_enter.pack_forget()



    def log_pass():

        temp_bool=Authentify(enter_login.get(),enter_password.get())
        print(temp_bool)
        f=open("login.log","a")
        
            
        if ChekTodayLoginInMessenger(enter_login.get())==False:
            messagebox.showerror("Ошибка","Авторизуйтесь в телеграм боте и повторите авторизацию заного")

        else:

            if temp_bool==True:
                messagebox.showinfo("Успешно","Авторизация через логин и пароль прошла успешно")
                f.write(f"{datetime.datetime.now()} Successful login to your account '{enter_login.get()}'\n")
                clear_login_form()
                Check(root)
            else:
                messagebox.showerror("Ошибка","Неверный логин или пароль")
                f.write(f"{datetime.datetime.now()} Unsuccessful login to your account '{enter_login.get()}'\n")

                

        




login()

root.mainloop()





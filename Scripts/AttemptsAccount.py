from CreatePass import CreatePassword
import config

con = config.con


#ВВод логина и пароля и проверка пароля на подлинность.
def Authentify(login,password):
    
    cur=con.cursor()
    login=login
    password=password

    
    cur.execute(f"SELECT * from users where login='{login}';") #Поиск пользователя в базе данных
    
    
    

    try:
        is_password=cur.fetchone()[2] #Выбираем из данных пароль
        
        if str(password)==str(is_password): 
            con.commit()
            return True
        else:
            con.commit()
            return False
        
        
    except:
        con.commit()
        return False
    
        





def AddKeyMessenger(login):
    
    key_messenger=CreatePassword(6)
    
    
    cur=con.cursor()
    cur.execute(f"UPDATE users SET key_messenger='{key_messenger}' WHERE login='{login}';") #Поиск пользователя в базе данных
    con.commit()
    cur.close()
    return key_messenger

    
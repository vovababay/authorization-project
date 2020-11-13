import config

con=config.con


def reg(login,password,messenger):
    
    
    cur=con.cursor()
    login=login
    password=password
    cur.execute(f"select * from users where login='{login}';")
    if (cur.fetchone()==None):
        cur.execute(f"insert into users(login,paswrd,messenger,is_login_today) values('{login}','{password}','{messenger}',false);") #Добавление пользователя в бд
        con.commit()
        return "Успешно"
    elif login=="" or password=="":
        return "Пустой ввод"
    else:
        return "Аккаунт существует"
    
    
    cur.close()
    



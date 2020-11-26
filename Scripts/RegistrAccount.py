import config

con=config.con


def reg(login,password,messenger,face,full_name):
    
    
    cur=con.cursor()
    login=login
    password=password
    cur.execute(f"select * from users where login='{login}';")
    if (cur.fetchone()==None):
        cur.execute(f"insert into users(login,paswrd,messenger,is_login_today,face,first_name,lock_accaunt) values('{login}','{password}','{messenger}',false,"+"'{"+f"{face}"+"}'"+f",'{full_name}'),false;")
        #print(f"insert into users(login,paswrd,messenger,is_login_today,face) values('{login}','{password}','{messenger}',false,"+"'{"+f"{face}"+"}');")#Добавление пользователя в бд
        con.commit()
        return "Успешно"
    elif login=="" or password=="":
        return "Пустой ввод"
    else:
        return "Аккаунт существует"
    
    
    cur.close()
    




import config

con=config.con



def ChekTodayLoginInMessenger(login):

    cur = con.cursor()
    cur.execute(f"SELECT is_login_today FROM users where login='{login}';")
    result=cur.fetchone()
    cur.close()
    return result[0]




import eel
from Scripts.main_reg import start_reg
from Scripts.main_key import start_key
#функця вызываемая из html на кнопку входа
@eel.expose
def enter(login, password):
	print(login, password)
	start_key()
#функця вызываемая из html на кнопку регистрации
@eel.expose
def registration(registr):
	start_reg()

eel.init("web-auto")
eel.start("main-auto.html", size=(650, 600),port=8000)
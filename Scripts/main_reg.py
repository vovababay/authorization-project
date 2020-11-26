import eel
from Scripts.main_uspeh import start_uspeh
#функця вызываемая из html на кнопку регистрации
@eel.expose
def register(name, login, password, rep_password):
	print(name, login, password, rep_password)
	start_uspeh()
#функця вызываемая из html на кнопку выбора фотографии
@eel.expose
def photography(photo):
	print(photo)
#функця вызываемая из html на кнопку выбора мессенджера
@eel.expose
def messenger(messenger):
	if messenger != "Выбрать мессенджер":
		print(messenger)

def start_reg():
	eel.init("web-reg")
	eel.start("main-reg.html", size=(650, 700),port=8001)
import eel
from Scripts.main_vhod import start_vhod
#функця вызываемая из html на кнопку Готово
@eel.expose
def enter_key(key):
	print(key)
	start_vhod()

def start_key():
	eel.init("web-key")
	eel.start("main-key.html", size=(440, 350),port=8002)
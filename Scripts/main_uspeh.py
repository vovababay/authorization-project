import eel 
#функця вызываемая из html на кнопку Готово
def start_uspeh():
	eel.init("web-uspeh")
	eel.start("main-uspeh.html", size=(350, 220),port=8004)
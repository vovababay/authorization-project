import eel 
#функця вызываемая из html на кнопку Готово
@eel.expose
def enter_key(key):
	print(key)

eel.init("web-uspeh")
eel.start("main-uspeh.html", size=(350, 220),port=8004)
import eel 
#функця вызываемая из html на кнопку Готово
def start_vhod():
	eel.init("web-vhod")
	eel.start("main-vhod.html", size=(220, 190),port=8089)
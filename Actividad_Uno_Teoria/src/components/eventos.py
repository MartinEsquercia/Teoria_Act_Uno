from src.windows import  ventanas
from src.handlers import handlers

def start():
    """Lanza ejecucion de ventana de menu """
    window = loop()
    window.close()

def loop():
    """ Loop de la ventana de menu  que capta los eventos al apretar las opciones """
    window = ventanas.build()

    while True:
        event, values = window.read()

        if event == "-exit-":
            break

        if event == "-top10selva-":
            handlers.paisSelva()
            print(event)
        if event == "-paisesmas60-":
            print(event)
            handlers.paisRural()                   

          
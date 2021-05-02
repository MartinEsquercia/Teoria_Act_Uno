import PySimpleGUI as sg
from src.handlers import handlers

def build():
    """ Construye la ventana de menu del juego """

    layout = [
        [sg.Button('Las 10 regiones con mayor porcentaje de tierra cubierta por selva en 2018', size=(60, 2), key="-top10selva-")],
        [sg.Button('Regiones que sobrepasan las 60 millones de personas que viven en areas rurales en 2019', size=(60,2), key = "-paisesmas60-")],
        [sg.Button('Salir', size=(60, 2), key="-exit-")]
    ]

    board = sg.Window('ActividadUno').Layout(layout)

    return board

def selva():
    """ Construye la ventana de paises con mayor cantidad de selva"""

    layout=[
        [sg.Text(handlers.paisSelva())],
        [sg.Button("Salir", size=(50,2), key = "-exit-")]
    ]

    board = sg.Window("Los 10 paises con mayor porcentaje de tierra cubierta por selva en 2018").Layout(layout)

    return board

def rural():
    """ Construye la ventana de paises con mayor cantidad de personas en el area rural"""

    layout=[
        [sg.Text(handlers.paisRural())],
        [sg.Button("Salir", size=(50,2), key = "-exit-")]
    ]

    board = sg.Window("Lista de paises que sobrepasan las 60 millones de personas que viven en areas rurales en 2019").Layout(layout)

    return board

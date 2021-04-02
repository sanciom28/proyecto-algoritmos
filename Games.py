# ALL OF ESCAPEMET'S VARIOUS GAMES

from API import api
from Room import Room
from Object import Object
from Game import Game

from terminaltables import AsciiTable

import random

class WordSearch(Game):
    '''Sopa de letras.'''
    pass


class PythonQuestions(Game):
    '''Preguntas sobre Python.'''
    pass

class Hangman(Game):
    '''El ahorcado.'''
    def __init__(self):
        super().__init__()
    


def main():

    #CREATING ROOMS
    print('Cargando cuartos...')

    laboratorio = Room(api()[0]['name'], api()[0]['objects'])
    biblioteca = Room(api()[1]['name'], api()[1]['objects'])
    plaza = Room(api()[2]['name'], api()[2]['objects'])
    pasillo = Room(api()[3]['name'], api()[3]['objects'])
    servidores = Room(api()[4]['name'], api()[4]['objects'])

    #CREATING OBJECTS
    print('Cargando objetos...')

    #PLAZA RECTORADO OBJECTS
    saman = Object(plaza.objects[0]['name'],plaza.objects[0]['position'],plaza.objects[0]['game'])
    banco_1 = Object(plaza.objects[1]['name'],plaza.objects[1]['position'],plaza.objects[1]['game'])
    banco_2 = Object(plaza.objects[2]['name'],plaza.objects[2]['position'],plaza.objects[2]['game'])

    #BIBLIOTECA OBJECTS
    libros = Object(biblioteca.objects[0]['name'],biblioteca.objects[0]['position'],biblioteca.objects[0]['game'])
    sentarse = Object(biblioteca.objects[1]['name'],biblioteca.objects[1]['position'],biblioteca.objects[1]['game'])
    gavetas = Object(biblioteca.objects[2]['name'],biblioteca.objects[2]['position'],biblioteca.objects[2]['game'])
    
    #PASILLO OBJECTS
    puerta_pasillo = Object(pasillo.objects[0]['name'],pasillo.objects[0]['position'],pasillo.objects[0]['game'])

    #LABORATORIO SL001 OBJECTS
    pizarra = Object(laboratorio.objects[0]['name'],laboratorio.objects[0]['position'],laboratorio.objects[0]['game'])
    compu_1 = Object(laboratorio.objects[1]['name'],laboratorio.objects[1]['position'],laboratorio.objects[1]['game'])
    compu_2 = Object(laboratorio.objects[2]['name'],laboratorio.objects[2]['position'],laboratorio.objects[2]['game'])
    
    #CUARTO DE SERVIDORES OBJECTS
    puerta = Object(servidores.objects[0]['name'],servidores.objects[0]['position'],servidores.objects[0]['game'])
    rack = Object(servidores.objects[1]['name'],servidores.objects[1]['position'],servidores.objects[1]['game'])
    papelera = Object(servidores.objects[2]['name'],servidores.objects[2]['position'],servidores.objects[2]['game'])

    #CREATING GAMES
    print('Cargando juegos...')

    #LABORATORIO SL001 GAMES
    sopa_letras = pizarra.game
    preguntas_python = compu_1.game
    adivinanzas = compu_2.game

    #BIBLIOTECA GAMES
    ahorcado = libros.game
    preguntas_math = sentarse.game
    criptograma = gavetas.game

    #PLAZA RECTORADO GAMES
    encuentra_logica = saman.game
    quizizz_unimet = banco_1.game
    memoria = banco_2.game

    #PASILLO GAMES
    logica_booleana = puerta_pasillo.game

    #CUARTO DE SERVIDORES GAMES
    palabra_mezclada = rack.game
    escoge_numero_entre = papelera.game
    juego_libre = puerta.game


main()

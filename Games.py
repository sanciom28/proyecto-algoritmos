# ALL OF ESCAPEMET'S VARIOUS GAMES



from terminaltables import AsciiTable

import Game
import API

import random

class WordSearch(Game):
    '''Sopa de letras.'''
    def __init__(self, questions):
        super().__init__('sopa_letras', False, 'vida extra', 'pierde media vida por palabra incorrecta', questions)

    def play(self):
        '''Empezar a jugar.'''

        board = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ]
        
        table = AsciiTable(board)
        print(table.table)

        word_1 = 'Claudia'
        word_2 = 'Matteo'
        word_3 = 'NicoleGarcia'


word = WordSearch('aaaa')
print(word.questions)
word.play()


class PythonQuestions(Game):
    '''Juego de preguntas sobre Python.'''
    def __init__(self, questions):
        super().__init__("Preguntas sobre python", "cable HDMI", "carnet", "pierde media vida por cada prueba incorrecta",questions)

    def play(self):
        '''Jugar'''
        pass


class Hangman(Game):
    '''Ahorcado. Se juega en el mueble de libros.'''
    def __init__(self, questions):
        super().__init__('ahocado', False, 'cable HDMI', 'pierde un cuarto de vida por letra incorrecta')
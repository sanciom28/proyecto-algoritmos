#TODO: OPTIMIZE CLUE USAGE

import random
import time
import os
import pickle

from ProjectFunctions import *

from Text import *
from Player import *

from API import api
from Room import Room
from Object import Object
from Game import Game
from Inventory import Inventory

def main():
    '''ESCAPEMET.'''

    #VARIABLES
    players_list = []
    player = Player('test','000000','20','2')
    start_game = False

    #READ FILES
    players_list = txt_receiver('/Users/matteosancio/Documents/UNIMET/VIII/Algoritmos./Proyecto/proyecto-algoritmos/datos.txt', players_list)

    #START MENU
    logo.p()
    while not start_game:

        option = menu(4)

        if option == '1':
            player = option_1(players_list,player)
            start_game = True
        elif option == '2':
            option_2()
        elif option == '3':
            option_3(players_list)
        else:
            option_4()

    #LOAD ROOM, OBJECT AND GAME OBJECTS
    print('Inicializando objetos, esto tomará un momento...\n')

    #CREATING ROOMS
    laboratorio = Room(api()[0]['name'], api()[0]['objects'])
    biblioteca = Room(api()[1]['name'], api()[1]['objects'])
    plaza = Room(api()[2]['name'], api()[2]['objects'])
    pasillo = Room(api()[3]['name'], api()[3]['objects'])
    servidores = Room(api()[4]['name'], api()[4]['objects'])

    #CREATING OBJECTS

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

    #LABORATORIO SL001 GAMES
    sopa_letras = Game(pizarra.game.get('message_requirement'),pizarra.game['requirement'],pizarra.game['name'],pizarra.game['award'],pizarra.game['rules'],pizarra.game['questions'])
    preguntas_python = Game(compu_1.game.get('message_requirement'),compu_1.game['requirement'],compu_1.game['name'],compu_1.game['award'],compu_1.game['rules'],compu_1.game['questions'])
    adivinanzas = Game(compu_2.game.get('message_requirement'),compu_2.game['requirement'],compu_2.game['name'],compu_2.game['award'],compu_2.game['rules'],compu_2.game['questions'])
    
    #BIBLIOTECA GAMES
    ahorcado = Game(libros.game.get('message_requirement'),libros.game['requirement'],libros.game['name'],libros.game['award'],libros.game['rules'],libros.game['questions'])
    preguntas_math = Game(sentarse.game.get('message_requirement'),sentarse.game['requirement'],sentarse.game['name'],sentarse.game['award'],sentarse.game['rules'],sentarse.game['questions'])
    criptograma = Game(gavetas.game.get('message_requirement'),gavetas.game['requirement'],gavetas.game['name'],gavetas.game['award'],gavetas.game['rules'],gavetas.game['questions'])

    #PLAZA RECTORADO GAMES
    encuentra_logica = Game(saman.game.get('message_requirement'),saman.game['requirement'],saman.game['name'],saman.game['award'],saman.game['rules'],saman.game['questions'])
    quizizz_unimet = Game(banco_1.game.get('message_requirement'),banco_1.game['requirement'],banco_1.game['name'],banco_1.game['award'],banco_1.game['rules'],banco_1.game['questions'])
    memoria = Game(banco_2.game.get('message_requirement'),banco_2.game['requirement'],banco_2.game['name'],banco_2.game['award'],banco_2.game['rules'],banco_2.game['questions'])

    #PASILLO GAMES
    logica_booleana = Game(puerta_pasillo.game.get('message_requirement'),puerta_pasillo.game['requirement'],puerta_pasillo.game['name'],puerta_pasillo.game['award'],puerta_pasillo.game['rules'],puerta_pasillo.game['questions'])

    #CUARTO DE SERVIDORES GAMES
    palabra_mezclada = Game(rack.game.get('message_requirement'),rack.game['requirement'],rack.game['name'],rack.game['award'],rack.game['rules'],rack.game['questions'])
    escoge_numero_entre = Game(papelera.game.get('message_requirement'),papelera.game['requirement'],papelera.game['name'],papelera.game['award'],papelera.game['rules'],papelera.game['questions'])
    juego_libre = Game(puerta.game.get('message_requirement'),puerta.game['requirement'],puerta.game['name'],puerta.game['award'],puerta.game['rules'],puerta.game['questions'])

    #PLAYER VARIABLES
    username = player.username
    avatar = player.avatar
    lives = player.lives
    clues = player.clues
    timer = player.timer
    player.start_time = time.time()
    inventario = Inventory()
    player.current_room = biblioteca
    lab_access = False

    pregame()

    narr_2.p()
    proceed()

    while True:

        player.current_time = time.time()
        if player.check_time():
            out_of_time()

        lives = inventario.check(lives)

        timer = ((player.timer*60) - (player.current_time - player.start_time))/60
        if timer < 10:
            timer = seconds_calc(timer)
            timer = timer[0:4].replace('.',':')
 
        else:
            timer = seconds_calc(timer)
            timer = timer[0:5].replace('.',':')

        if player.current_room == biblioteca:
            #BIBLIOTECA
            wipe()
            print(biblioteca_drawing(lives,clues,timer))
            option = select.t().lower()

            if option == '1':
                #MUEBLE DE SENTARSE / PREGUNTAS MATEMATICA
                option = sentarse.interact(inventario.bag)
                if option:
                    if not preguntas_math.played:
                        q = create_q_list(preguntas_math.questions,len(preguntas_math.questions),1)
                        c_list = create_c_list(preguntas_math.questions,len(preguntas_math.questions),2)
                        item,lives,clues = preguntas_math.play_preguntas_math(lives,clues,q,c_list)
                        inventario.add(item)
                        preguntas_math.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == '2':
                #MUEBLE DE LIBROS / AHORCADO
                option = libros.interact(inventario.bag)
                if option:
                    if not ahorcado.played:
                        q_list = create_q_list(ahorcado.questions,len(ahorcado.questions),2)
                        q = q_list[0]
                        a = q_list[1]
                        c_list = create_c_list(ahorcado.questions,len(ahorcado.questions),2)
                        item,lives,clues = ahorcado.play_ahorcado(lives,clues,q,a,c_list)
                        inventario.add(item)
                        ahorcado.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == '3':
                #MUEBLE DE GAVETAS / CRIPTOGRAMA
                option = gavetas.interact(inventario.bag)
                if option:
                    if not criptograma.played:
                        q = create_q_list(criptograma.questions,len(criptograma.questions),1)[0]
                        item,lives = criptograma.play_criptograma(lives,q)
                        inventario.add(item)
                        criptograma.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == 'l':
                player.move(plaza)

            elif option == 'r':
                if lab_access:
                    player.move(laboratorio)
                else:
                    player.move(pasillo)

            elif option == 'i':
                print(inventario.show())
                proceed()

        elif player.current_room == plaza:
            #PLAZA RECTORADO
            wipe()
            print(plaza_drawing(lives,clues,timer))
            option = select.t().lower()

            if option == '1':
                #BANCO 1 / QUIZIZZ
                option = banco_1.interact(inventario.bag)
                if option:
                    if not quizizz_unimet.played:
                        item,lives,clues = quizizz_unimet.play_quizizz_unimet(lives,clues,quizizz_unimet.questions)
                        inventario.add(item)
                        quizizz_unimet.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == '2':
                #SAMAN / LOGICA EMOJIS
                if 'titulo universitario' and 'mensaje' not in inventario.bag:
                    lives = lose_lives(lives,1)
                option = saman.interact(inventario.bag)
                if option:
                    if not encuentra_logica.played:
                        q = create_q_list(encuentra_logica.questions,len(encuentra_logica.questions),1)[0]
                        item,lives = encuentra_logica.play_encuentra_logica(lives,q)
                        inventario.add(item)
                        encuentra_logica.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == '3':
                #BANCO 2 / MEMORIA
                option = banco_2.interact(inventario.bag)
                if option:
                    if not memoria.played:
                        q = create_q_list(memoria.questions,len(memoria.questions),1)[0]
                        item,lives = memoria.play_memoria(lives,q)
                        inventario.add(item)
                        memoria.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == 'l':
                give_up()

            elif option == 'r':
                player.move(biblioteca)

            elif option == 'i':
                print(inventario.show())
                proceed()

        elif player.current_room == pasillo:
            #PASILLO
            wipe()
            print(pasillo_drawing(lives,clues,timer))
            option = select.t().lower()

            if option == '1':
                #PUERTA PASILLO
                option = puerta_pasillo.interact(inventario.bag)
                if option:
                    if not logica_booleana.played:
                        q_list = create_q_list(logica_booleana.questions,len(logica_booleana.questions),2)
                        q = q_list[0]
                        a = q_list[1]
                        item,lives = logica_booleana.play_logica_booleana(lives,q,a)
                        inventario.add(item)
                        logica_booleana.played = True
                        lab_access = True
                        player.move(laboratorio)
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == 'i':
                print(inventario.show())
                proceed()

            else:
                player.move(biblioteca)

        elif player.current_room == laboratorio:
            #LABORATORIO
            wipe()
            print(laboratorio_drawing(lives,clues,timer))
            option = select.t().lower()

            if option == '1':
                #COMPUTADORA 1 / PREGUNTAS PYTHON
                if option:
                    if not preguntas_python.played:
                        q_list = create_q_list(preguntas_python.questions,len(preguntas_python.questions),2)
                        q = q_list[0]
                        a = q_list[1]
                        c_list = create_c_list(preguntas_python.questions,len(preguntas_python.questions),2)
                        item,lives,clues = preguntas_python.play_preguntas_python(lives,clues,q,a,c_list)
                        inventario.add(item)
                        preguntas_python.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == '2':
                #PIZARRA / SOPA DE LETRAS
                option = pizarra.interact(inventario.bag)
                if option:
                    if not sopa_letras.played:
                        q_list = create_q_list(sopa_letras.questions,len(sopa_letras.questions),3)
                        c_list = create_c_list(sopa_letras.questions,len(sopa_letras.questions),3)
                        item = sopa_letras.play_sopa_letras(lives,clues,q_list,c_list)
                        inventario.add(item)
                        sopa_letras.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == '3':
                #COMPUTADORA 2 / ADIVINANZAS
                if option:
                    if not adivinanzas.played:
                        q_list = create_q_list(adivinanzas.questions,len(adivinanzas.questions),2)
                        q = q_list[0]
                        a = q_list[1]
                        c_list = create_c_list(adivinanzas.questions,len(adivinanzas.questions),2)
                        item,lives,clues = adivinanzas.play_adivinanzas(lives,clues,q,a,c_list)
                        inventario.add(item)
                        adivinanzas.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == 'l':
                player.move(servidores)

            elif option == 'r':
                player.move(biblioteca)

            elif option == 'i':
                print(inventario.show())
                proceed()

        elif player.current_room == servidores:
            #SERVIDORES
            wipe()
            print(servidores_drawing(lives,clues,timer))
            option = select.t().lower()

            if option == '1':
                #RACK / PALABRA MEZCLADA
                option = rack.interact(inventario.bag)
                if option:
                    if not palabra_mezclada.played:
                        q_list = create_q_list(palabra_mezclada.questions,len(palabra_mezclada.questions),3)
                        q = q_list[0]
                        c = q_list[1]
                        a = q_list[2]
                        item,lives = palabra_mezclada.play_palabra_mezclada(lives,q,c,a,scramble(a))
                        inventario.add(item)
                        palabra_mezclada.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == '2':
                #PUERTA / %(K7~L"P2>+_=
                option = puerta.interact(inventario.bag)
                print('HI4TUVE9WCU8HRUN8XEUHFD87EFUHD\n')

            elif option == '3':
                #PAPELERA / ESCOGE NUMERO
                option = papelera.interact(inventario.bag)
                if option:
                    if not escoge_numero_entre.played:
                        q_list = create_q_list(escoge_numero_entre.questions,len(escoge_numero_entre.questions),1)
                        q = q_list[0]
                        item,lives,clues = escoge_numero_entre.play_escoge_numero_entre(lives,q,random.randint(1,15))
                        inventario.add(item)
                        escoge_numero_entre.played = True
                        proceed()
                    else:
                        already_played()
                else:
                    proceed()

            elif option == 'r':
                player.move(laboratorio)

            elif option == 'i':
                print(inventario.show())
                proceed()
    


main()
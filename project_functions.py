from Player import *
from Text import *

import time
import pickle
import os

players_list = []

#SERIALIZACION
def txt_receiver(txt_name, db):
    '''Receiving data from .txt file.'''
    binary_read = open(txt_name, 'rb')
    if os.stat(txt_name).st_size != 0:
        db = pickle.load(binary_read)
    binary_read.close()
    return db
def txt_loader(txt_name, db):
    '''Loading data to a .txt file.'''
    binary_write = open(txt_name, 'wb')
    db = pickle.dump(db, binary_write)
    binary_write.close()

#READING TEXT FILE
players_list = txt_receiver('/Users/matteosancio/Documents/UNIMET/VIII/Algoritmos./Proyecto/proyecto-algoritmos/datos.txt', players_list)

def menu():
    '''Main game menu'''
    print('''
    █▀▀ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▄▀█ █▀▀ ▀▀█▀▀
    █▀▀ ▀▀█ █░░ █▄▄█ █░░█ █▀▀ █░▀░█ █▀▀ ░░█░░
    ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ░░▀░░
    ''')

    #time.sleep(1)
    
    select = input('''
    Bienvenid@s a Escapemet 🔐
    
    1. Comenzar Nueva Partida
    2. Ver Instrucciones
    3. Ver Récords
    4. Salir
    
    > ''')

    return select
def return_to_menu(option):
    while option!='s' or option!='n':
        option = input('Quieres regresar al menú principal?\n(S/N)\n> ').lower()
    return option

#NARRATIVES
narr_1 = 'Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {tiempo_según_dificultad} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?'
narr_2 = 'Bienvenido {nombre_avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.'

#BASIC PROCEDURES FOR AESTHETIC PURPOSES 
def blank():
    print('\n')
def msg_error():
    return 'Error, intente de nuevo.\n> '
def thanks():
    print('\nGracias por jugar.\n-MS\n')

#USER REGISTERING INPUT VALIDATIONS
def enter_username(word,msg_1,msg_2):
    '''Verifying that an input is alphanumeric.'''
    word=input(msg_1)
    while not word.isalnum():
        word = input(msg_2)
    return word
def enter_password(word,msg_1,msg_2):
    '''Verifying password.'''
    word=input(msg_1)
    while len(word) < 6:
        word = input(msg_2)
    return word
def enter_age(n,msg_1,msg_2):
    '''Verifying age.'''
    while True:
        try:
            n=int(input(msg_1))
            if not 101>n>=13:
                raise Exception
            break
        except:
            print(msg_2)
    return n
def enter_avatar(n,msg_1,msg_2,arr):
    '''Choosing an avatar.'''
    print(msg_1)
    while True:
        try:
            n=int(input('> '))
            if not 1<=n<=5:
                raise Exception
            break
        except:
            print(msg_2)
    return arr[n-1]

def register(db):
    '''Register a new player.'''

    #MESSAGES
    msg_username = 'Ingrese su nuevo usuario:\n- Solo letras y números.\n> '
    msg_psw = 'Ingrese su contraseña:\n- Mínimo 6 caracteres.\n> '
    msg_age = 'Ingrese su edad:\n> '
    msg_avatar = 'Ingrese el número del avatar que desea usar.\n\n\t1. Scharifker\n\t2. Eugenio Mendoza\n\t3. Pelusa\n\t4. Gandhi\n\t5. Cachito de Jamón\n'
    msg_age_error = 'Error, ingresar una edad válida de 13 años o más.'
    msg_avatar_error = 'Error, ingresar el índice del avatar que desee.'
    msg_dato_invalido = 'Dato ingresado inválido, intente de nuevo:\n> '

    #VARIABLES
    username = ''
    psw = ''
    age = ''
    avatar = ''
    avatar_list = ['Scharifker','Eugenio Mendoza','Pelusa','Gandhi','Cachito de Jamón']

    #START REGISTERING PROCESS
    blank()
    username = enter_username(username, msg_username, msg_dato_invalido)
    print(f'Usuario "{username}" disponible.')
    blank()
    psw = enter_password(psw, msg_psw, msg_dato_invalido)
    print('Contraseña guardada.')
    blank()
    age = enter_age(age, msg_age, msg_age_error)
    print(f'Su edad es {age}')
    blank()
    avatar = enter_avatar(avatar, msg_avatar, msg_avatar_error, avatar_list)
    print(f'Su avatar es {avatar}')
    blank()

    #CREATING NEW PLAYER OBJECT
    new_player = Player(username, psw, age, avatar)
    print('Usuario creado.')

    #REGISTERING INTO FILE
    db.append(new_player)
    print('Usuario registrado.')

    return db #upon called, load data into txt with txt_loader()

def authenticate(user,pw,db,msg_1,msg_2,msg_3):
    '''Authenticate user's credentials.'''
    while True:
        user = input(msg_1)
        pw = input(msg_2)
        for i in range(len(db)):
            if db[i].username == user:
                if db[i].psw == pw:
                    return db[i]
        print(msg_3)

def login(db):
    '''Log in as an existing player.'''

    #MESSAGES
    msg_username = 'Ingrese su usuario:\n> '
    msg_psw = 'Ingrese su contraseña:\n> '
    msg_incorrect = 'Usuario o constraseña incorrecta.'

    #VARIABLES
    username = ''
    psw = ''

    #START LOGIN PROCESS
    blank()
    login_key = authenticate(username,psw,db,msg_username,msg_psw,msg_incorrect)
    print('Ingresado al sistema correctamente.')

def difficulty():
    '''Choosing the game's difficulty.'''

    diff = input('''
    Seleccionar dificultad:
    
    1. Fácil 😃
        - 5 Vidas
        - 5 Pistas
        - 60 Minutos

    2. Medio 😌
        - 3 Vidas
        - 3 Pistas
        - 40 Minutos
    
    3. Difícil 😈
        - 1 Vida
        - 2 Pistas
        - 20 Minutos
    
    > ''')

def option_1():
    '''1st option from main menu.'''

    option = input('''
    1. Ingresar
    2. Registrarse
    3. Volver al menú

    > ''')

    while True:

        if option == '1':
            login(players_list)
            difficulty()

        elif option == '2':
            register(players_list)
            txt_loader('/Users/matteosancio/Documents/UNIMET/VIII/Algoritmos./Proyecto/proyecto-algoritmos/datos.txt',players_list)
            break

        elif option == '3':
            break

        else:
            option = input(msg_error())

    main_alpha()

def option_2():
    '''2nd option from main menu.'''

    blank()
    instructions = Text('Escapemet es un juego que se gana al lograr escaparse del mismo.\n\nEl juego consta de diferentes cuartos. Cada cuarto tiene objetos y cada objeto tiene un acertijo a resolver.\n\nCada vez que se gana un juego se obtiene una recompensa que puede servir para resolver la problemática del juego.\n\nExisten 3 dificultades, y dependiendo de cada una se tienen una cierta cantidad de vidas y de pistas.\n\nSe pierde el juego si se agotan las vidas, o se acaba el tiempo.\n')
    instructions.show()
    instructions.proceed()
    main_alpha()

def option_3():
    '''3rd option from main menu.'''
    
    pass

def main_alpha():
    '''temporary main()'''
    option = menu()
    while True:

        if option == '1':
            option_1()

        elif option == '2':
            option_2()

        elif option == '3':
            option_3()

        elif option == '4':
            thanks()
            exit()
        
        else:
            option = input(msg_error())

main_alpha()

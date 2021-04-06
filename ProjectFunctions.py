#USEFUL ESCAPEMET FUNCTIONS
import pickle
import os
import time
import random
from Text import *
from Player import *

#FUNCTIONS FOR AESTHETIC PURPOSES
def blank():
    print('\n')
def msg_error():
    return 'Error, intente de nuevo.\n> '
def thanks():
    print('\nGracias por jugar.\n-MS\n\n')
def pregame():
    narr_1.p()
    proceed()
    blank()
    print('El juego iniciará pronto. Buena suerte!!')
    for i in range(0,10):
        print(f'{10-(i)}...')
        time.sleep(1)
    blank()
def proceed():
    return input('Presiona ENTER para continuar.')
def correct():
    print('Respuesta correcta!')
def incorrect():
    print('Respuesta incorrecta.')
def no_more_clues():
    print('No hay más pistas disponibles aquí.')
def you_won(game):
    print(f'{game} completado!')
def wipe():
    print('\n'*70)
def give_up():
    print('Deseas acabar esta partida?\n  S: Sí    N: No')
    option = select.t().lower()
    if option == 's' or option == 'si':
        print('\nEstás seguro?\n  S: Sí    N: No')
        option = select.t().lower()
        if option == 's' or option == 'si':
            blank()
            thanks()
            exit()
def wait():
    time.sleep(2)
def out_of_time():
    print('\nLo siento, te has quedado sin tiempo. 😪\n')
    thanks()
    exit()
def already_played():
    print('\nYa jugaste este juego.')
    proceed()

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

#USER ADMINISTRATION
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
    blank()
    print('Ingresado al sistema correctamente.')

    return login_key

#MENU TAMPERING
def option_1_1(player):
    '''Choosing the game's difficulty.'''

    diff = menu_1_1.t()

    while True:

        if diff == '1':
            player.difficulty = 'Fácil'
            player.lives = 5.0
            player.clues = 5
            player.timer = 60.00
            break

        elif diff == '2':
            player.difficulty = 'Medio'
            player.lives = 3.0
            player.clues = 3
            player.timer = 40.00
            break

        elif diff == '3':
            player.difficulty = 'Difícil'
            player.lives = 1.0
            player.clues = 2
            player.timer = 20.00
            break

        elif diff == '4':
            #EXTREME DIFFICULTY (SECRET)
            player.difficulty = 'Imposible'
            player.lives = 0.5
            player.clues = 0
            player.timer = 10.00
            break
            
        else:
            diff = error.t()

    print(f'Dificultad puesta a "{player.difficulty}".')
    blank()
    return player
def menu(n):
    option_list = [str(i+1) for i in range(n)]
    main_menu.p()
    option = select.t()

    while option not in option_list:
        option = error.t()

    return option
def option_1(db,player):
    '''1st option from main menu.'''

    menu_1.p()
    option = select.t()

    while True:

        if option == '1':
            player = login(db)
            #STARTING GAME
            blank()
            player = option_1_1(player)
            return player

        elif option == '2':
            register(db)
            txt_loader('/Users/matteosancio/Documents/UNIMET/VIII/Algoritmos./Proyecto/proyecto-algoritmos/datos.txt',db)
            #RECURSIVE
            return option_1(db,player)

        else:
            option = error.t()
def option_2():
    '''2nd option from main menu.'''

    blank()
    instructions.p()
    proceed()
def option_3(db):
    '''3rd option from main menu.'''

    blank()
    print('Usuarios Registrados:\n')
    for i in range(len(db)):
        print(f'{1+i}. {db[i].username}')
    blank()
def option_4():
    thanks()
    exit()

#ROOM DRAWINGS
def biblioteca_drawing(lives,clues,timer):
    return f'''
    V I D A S : {lives}                                         T I E M P O : {timer}
    P I S T A S : {clues}                                  I N V E N T A R I O  ( I )

    ----------------------------- B I B L I O T E C A --------------------------
    |   |                                                                  |   |
    |   |                           _______________                        |   |
    | /||           ( 1 )           |    ( 2 )    |          ( 3 )         ||\ |
    || ||                           |_____________|                        || ||
    || ||       ____________        |             |                        || ||
    || ||   ___|   .    .   |___    |_____________|     _______________    || ||
    || ||   |  |   .    .   |  |    |             |     |     ___     |    || ||
    || ||   |  |____________|  |    |_____________|     |_____________|    || ||
    || ||___|  |            |  |____|             |_____|  __  |  __  |____|| ||
    || /    |__|____________|__|    |_____________|     |______|______|     \ ||
    ||/                                                                      \||
    |/________________________________________________________________________\|

    ← P L A Z A  ( L )                            ( R )  L A B O R A T O R I O →

    '''
def plaza_drawing(lives,clues,timer):
    return f'''
    V I D A S : {lives}                                         T I E M P O : {timer}
    P I S T A S : {clues}                                  I N V E N T A R I O  ( I )

    -------------------------------- P L A Z A ---------------------------------
    |                                                                          |
    |                                   ____                                   |
    |                             ____/      \____                             |
    |                         __/                  \__                         |
    |          ( 1 )        /          ( 2 )           \        ( 3 )          |
    |                       \__________________________/                       |
    |                                 |      |                                 |
    |    _________________            |      |            _________________    |
    |   |_________________|           |      |           |_________________|   |
    |___ | |           | | ____      /        \      ____ | |           | | ___|
    |                          "ºººººººººººººººººººº"                          |
    |__________________________________________________________________________|

    ← R E N D I R S E  ( L )                        ( R )  B I B L I O T E C A →

    '''
def laboratorio_drawing(lives,clues,timer):
    return f'''
    V I D A S : {lives}                                         T I E M P O : {timer}
    P I S T A S : {clues}                                  I N V E N T A R I O  ( I )

    -------------------------- L A B O R A T O R I O ---------------------------
    |   |                                                                  |   |
    |   |                     ________________________                     |   |
    | /||       ( 1 )         |                      |         ( 3 )       ||\ |
    || ||     __________      |        ( 2 )         |      __________     || ||
    || ||    |          |     |                      |     |          |    || ||
    || ||    |          |     |______________________|     |          |    || ||
    || ||    |__________|                                  |__________|    || ||
    || ||    ___/____\___                                  ___/____\___    || ||
    || ||____||        || _________________________________||        ||____|| ||
    || /     ||________||                                  ||________||     \ ||
    ||/                                                                      \||
    |/________________________________________________________________________\|

    ← S E R V I D O R E S  ( L )                    ( R )  B I B L I O T E C A →

    '''
def servidores_drawing(lives,clues,timer):
    return f'''
    V I D A S : {lives}                                         T I E M P O : {timer}
    P I S T A S : {clues}                                  I N V E N T A R I O  ( I )

    ------------------- C U A R T O  D E  S E R V I D O R E S ------------------
    |   |                                                                  |   |
    |   |                          ______________                          |   |
    |   |         ( 1 )           |              |          ( 3 )          ||\ |
    |   |     _____________       |     ( 2 )    |                         || ||
    |   |    |_____________|      |           _  |         _______         || ||
    |   |    |_____________|      |          |o| |        |       |        || ||
    |   |    |_____________|      |          |_| |        |_______|        || ||
    |   |    |_____________|      |              |        |^^^^^^^|        || ||
    |   |____|_____________|______|______________|________|       |________|| ||
    |  /     |_____________|                              |_______|         \ ||
    | /                                                                      \||
    |/________________________________________________________________________\|

                                                  ( R )  L A B O R A T O R I O →

    '''
def pasillo_drawing(lives,clues,timer):
    return f'''
    V I D A S : {lives}
    P I S T A S : {clues}
    T I E M P O : {timer}
    I N V E N T A R I O  ( I )

    ------ P A S I L L O ------
    |\                       /|
    |  \                   /  |
    |    \     ( 1 )     /    |
    |      \__________ /      |
    |       |         |       |
    |       |         |       |
    |       |         |       |
    |       |       O |       |
    |       |         |       |
    |       |         |       |
    |       |         |       |
    |       |_________|       |
    |     _/___________\_     |
    |   _/_______________\_   |
    | _/___________________\_ |
    |/_______________________\|

       ↓  V O L V E R  ( B )

    '''

#LIVES/CLUES MODIFIERS
def lose_lives(m,n):
    '''Lose n amount of lives.'''

    if n == 0.25:
        print('Has perdido un cuarto de vida. 🙃')            
    elif n == 0.5:
        print('Has perdido media vida. 😟')            
    elif n == 1:
        print('Has perdido una vida. 😔')

    if m > n:
        return m - n

    print('Te has quedado sin vidas. 😭\n')
    #TODO: SAVE GAME
    print('Muchas gracias por jugar!')
    print('-MS')
    exit()
def use_clue(clues):
    '''Use a clue.'''

    if clues < 0:
        print('No hay pistas disponibles aquí.')
        return clues

    elif clues == 0:
        print('Ya usaste todas tus pistas. 😕')
        return clues

    clues-=1

    print('Has usado una pista.')
    if clues > 0:
        return clues

    print('Ya no te quedan más pistas. 😭')
    return clues

#OTHER FUNCTIONS
def scramble(arr):
    '''Scramble a list of words' letters.'''

    for i, word in enumerate(arr):
        new_word = ''
        scrambled = list(word)
        scrambled = random.sample(scrambled, k=len(scrambled))
        for letter in scrambled:
            new_word += letter
        arr[i] = new_word

    new_arr = []
    for i in arr:
        new_arr.append(i)

    return new_arr
def smash_att(inv):
    if 'martillo' in inv:
        print('Has conseguido un martillo. Quizá podrás romper el seguro de la puerta con él.')
        proceed()
        wipe()
        print('CRASH!!!!!\n\n\n')
        time.sleep(1)
        print('has roto la puerta.')
        return True
    return False

#BEGIN GAME
def create_q_list(db,q,n):
    '''Creates a list of question parameters.'''

    db = db[random.randrange(q)]
    arr = [_ for _ in db.values()]
    arr = arr[0:n]
    return arr
def create_c_list(db,q,n):
    '''Creates a list of clue parameters.'''

    db = db[random.randrange(q)]
    arr = [_ for _ in db.values()]
    for i in range(n):
        arr.pop(0)
    return arr

#TIME FUNCTIONS
def seconds_calc(timer):
    '''Calculate seconds.'''
    if timer < 10:
        min = str(timer)[:2]
        sec = str(timer)[2:]
    else:
        min = str(timer)[:3]
        sec = str(timer)[3:]

    sec = (int(sec) / 100) * 60
    timer = min + str(sec)

    return timer


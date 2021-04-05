
class Text:
    '''Any body of text.'''
    def __init__(self, body):
        self.body = body

    def p(self):
        #PRINT
        print(self.body)

    def r(self):
        #RETURN
        return self.body

    def t(self):
        #INPUT
        return input(self.body)


logo = Text('''
    █▀▀ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▄▀█ █▀▀ ▀▀█▀▀
    █▀▀ ▀▀█ █░░ █▄▄█ █░░█ █▀▀ █░▀░█ █▀▀ ░░█░░
    ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ░░▀░░
    ''')

main_menu = Text('''
        Bienvenid@s a Escapemet 🔐
        
        1. Comenzar Nueva Partida
        2. Ver Instrucciones
        3. Ver Récords
        4. Salir
        ''')

menu_1 = Text('''
        1. Ingresar
        2. Registrarse
        ''')

menu_1_1 = Text('''
           1                  2                   3
        E A S Y          M E D I U M           H A R D

       5 vidas          3 vidas               1 vida
       5 pistas         3 pistas              2 pistas
       60 minutos       40 minutos            20 minutos


ingrese el número de la dificultad que desee.
''')


instructions = Text('Escapemet es un juego que se gana al lograr escaparse del mismo.\n\nEl juego consta de diferentes cuartos. Cada cuarto tiene objetos y cada objeto tiene un acertijo a resolver.\n\nCada vez que se gana un juego se obtiene una recompensa que puede servir para resolver la problemática del juego.\n\nExisten 3 dificultades, y dependiendo de cada una se tienen una cierta cantidad de vidas y de pistas.\n\nSe pierde el juego si se agotan las vidas, o se acaba el tiempo.\n')

select = Text('> ')

error = Text('\nError, intente de nuevo.\n> ')
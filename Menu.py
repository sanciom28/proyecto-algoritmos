
class Menu:
    '''Project's various menus. Here the user chooses what to do.'''
    
    def __init__(self):
        
        self.header = '''
        █▀▀ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▄▀█ █▀▀ ▀▀█▀▀
        █▀▀ ▀▀█ █░░ █▄▄█ █░░█ █▀▀ █░▀░█ █▀▀ ░░█░░
        ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ░░▀░░
        '''
        self.main_menu = '''
        Bienvenid@s a Escapemet 🔐
        
        1. Comenzar Nueva Partida
        2. Ver Instrucciones
        3. Ver Récords
        4. Salir
        
        > '''
        self.menu_1 = '''
        1. Ingresar
        2. Registrarse
        3. Volver al menú

        > '''
        self.error = 'Error, intente de nuevo.\n> '

    def get_header(self):
        print(self.header)

    def get_main_menu(self):
        print(self.main_menu)

    def get_option(self,select,*args):
        '''Returns a determined function depending on the user's choice'''
        for i, func in enumerate(args):
            if select == str(i+1):
                print('Elegida opción {}'.format(i+1))
                return func
        return self.error


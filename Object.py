
class Object:
    '''Escapemet's objects blueprint.'''
    def __init__(self, name, position, game):
        self.name = name
        self.position = position
        self.game = game


    def interact(self):
        print('\nObjeto actual: {}\nJuego: {}\n'.format(self.name,self.game['name']))
        if not self.game['requirement']:
            option = input("Quieres jugar? (S/N)\n> ").lower()
            if option == 's':
                return True
            return False
        input('Aún no puedes jugar.')
        return False

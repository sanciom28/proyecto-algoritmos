
class Object:
    '''Escapemet's objects blueprint.'''
    def __init__(self, name, position, game):
        self.name = name
        self.position = position
        self.game = game


    def show(self):
        return 'Objeto actual: {}\nPosición: {}\nJuego: {}'.format(self.name,self.position,self.game['name'])

    def interact(self):
        pass #TODO



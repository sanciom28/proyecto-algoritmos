
class Object:
    '''Escapemet's objects blueprint.'''
    def __init__(self, name, position, game):
        self.name = name
        self.position = position
        self.game = game


    def interact(self,inv=[]):
        print('\nObjeto actual: {}\nJuego: {}\n'.format(self.name,self.game['name']))
        
        req = self.game['requirement']

        if not req:
            option = input("Quieres jugar? (S/N)\n> ").lower()
            if option == 's':
                return True
            return False

        if inv:
            for item in inv:
                if req.lower() == item.lower():
                    print(f'Has usado: {item}.')
                    print('Juego desbloqueado!\n')
                    self.game['requirement'] = False
                    
                    return self.game['requirement']

        print(self.game['message_requirement'])
        return False

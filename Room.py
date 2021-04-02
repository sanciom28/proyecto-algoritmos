
from API import api

class Room:
    '''Escapemet's rooms blueprint.'''
    def __init__(self, name, objects):
        self.name = name
        self.objects = objects

def main():
    print('Cargando cuartos...')
    laboratorio = Room(api()[0]['name'], api()[0]['objects'])
    biblioteca = Room(api()[1]['name'], api()[1]['objects'])
    plaza = Room(api()[2]['name'], api()[2]['objects'])
    pasillo = Room(api()[3]['name'], api()[3]['objects'])
    servidores = Room(api()[4]['name'], api()[4]['objects'])

main()
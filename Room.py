
from API import api

class Room:
    '''Escapemet's rooms blueprint.'''
    def __init__(self, name, objects):
        self.name = name
        self.objects = objects

    def objects_count(self):
        return len(self.objects)

    def show(self):
        return f'Cuarto actual: {self.name}\nObjetos disponibles: {len(self.objects)}'

def main():
    pass

main()
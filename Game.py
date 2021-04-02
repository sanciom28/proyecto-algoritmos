# ABSTRACT CLASS
from abc import ABC, abstractmethod

class Game(ABC):
    '''Escapemet game blueprint.'''
    def __init__(self, name, requirement, award, rules, questions, message_requirement):
        self.name = name
        self.requirement = requirement
        self.award = award
        self.rules = rules
        self.questions = questions
        self.message_requirement = message_requirement
    
    # def show(self):
    #     '''Show game description'''
    #     return f'Nombre del juego: {self.name}'

    @abstractmethod
    def play(self):
        pass
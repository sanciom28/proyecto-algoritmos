class Player:
    '''Escapemet player blueprint.'''
    
    def __init__(self, username, psw, age, avatar):
        self.username = username
        self.psw = psw
        self.age = age
        self.avatar = avatar
        self.times = []
        self.difficulty = difficulty
        self.lives = 0.0
        self.clues = 0
        self.timer = 60.00
        self.current_room = 'Biblioteca'

    def show(self):
        return f'{self.username},{self.psw},{self.age},{self.avatar},{self.times},{self.lives},{self.clues}'


    def move(self):
        pass

    def touch(self):
        pass

    def save_item(self):
        pass

    def use_item(self):
        pass

    def use_clue(self):
        pass

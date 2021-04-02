class Player:
    '''Escapemet player blueprint.'''
    
    def __init__(self, username, psw, age, avatar):
        self.username = username
        self.psw = psw
        self.age = age
        self.avatar = avatar
        self.times = []
        self.lives = 0.0
        self.clues = 0

    def show(self):
        return f'{self.username},{self.psw},{self.age},{self.avatar},{self.times},{self.lives},{self.clues}'


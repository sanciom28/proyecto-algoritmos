class Player:
    '''Escapemet player blueprint.'''
    
    def __init__(self, username, psw, age, avatar):
        self.username = username
        self.psw = psw
        self.age = age
        self.avatar = avatar
        self.times = []
        self.difficulty = 'Dificultad'
        self.lives = 0.0
        self.clues = 0
        self.timer = 60.00
        self.current_room = ''
        self.start_time = 0
        self.current_time = 0

    def show(self):
        return f'{self.username}, {self.psw}, {self.age}, {self.avatar}, {self.times}, {self.difficulty},{self.lives}, {self.clues},{self.timer},{self.current_room}'


    def move(self,room):
        '''Move to another room.'''
        self.current_room = room
        return self.current_room

    def check_time(self):
        '''Checks if'''
        if self.current_time - self.start_time > self.timer*60:
            return True
        return False

    def save_item(self):
        pass

    def use_item(self):
        pass


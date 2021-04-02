
class Text:
    '''Any body of text.'''
    def __init__(self, body):
        self.body = body

    def show(self):
        print(self.body)

    def proceed(self):
        return input('Presiona ENTER para continuar.')
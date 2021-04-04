#USEFUL GAME FUNCTIONS
import random

#MESSAGES
def correct():
    print('Respuesta correcta!')
def incorrect():
    print('Respuesta incorrecta.')
def no_more_clues():
    print('No hay más pistas disponibles aquí.')
def blank():
    print('\n')
def you_won(game):
    print(f'{game} completado!')

def lose_lives(m,n):
    '''Lose n amount of lives.'''

    if n == 0.25:
        print('Has perdido un cuarto de vida. 🙃')            
    elif n == 0.5:
        print('Has perdido media vida. 😟')            
    elif n == 1:
        print('Has perdido una vida. 😔')

    if m > n:
        return m - n

    print('Te has quedado sin vidas. 😭\n')
    #TODO: THIS ALREADY EXISTS AS thanks()
    print('Muchas gracias por jugar!')
    print('-MS')
    exit()


def use_clue(clues):
    '''Use a clue.'''

    if clues <= 0:
        print('Ya usaste todas tus pistas. 😕')
        return clues

    clues-=1

    print('Has usado una pista.')
    if clues > 0:
        return clues

    print('Ya no te quedan más pistas. 😭')
    return clues






#FUNCTIONS FOR SPECIFIC GAMES

def how_close_clue(a,b):
    '''Tells the player how close number A is from number B.'''

    if not str(a).isnumeric():
        return None

    elif 0 < int(a)-b < 4:
        print('Estás un poco arriba.')

    elif 0 > int(a)-b > -4:
        print('Estás un poco abajo.')

    elif 4 <= int(a)-b <= 14:
        print('Estás muy arriba.')

    else:
        print('Estás muy abajo.')

def scramble(arr):
    '''Scramble a list of words' letters.'''

    for i, word in enumerate(arr):
        new_word = ''
        scrambled = list(word)
        scrambled = random.sample(scrambled, k=len(scrambled))
        for letter in scrambled:
            new_word += letter
        arr[i] = new_word

    new_arr = []
    for i in arr:
        new_arr.append(i)

    return new_arr


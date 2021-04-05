import time
import random

from sympy import Derivative, Subs, symbols, Function, init_printing
from math import pi

from GameFunctions import *

class Game:
    '''Escapemet game blueprint.'''
    def __init__(self, message_requirement, requirement, name, award, rules, questions):
        self.message_requirement = message_requirement
        self.requirement = requirement
        self.name = name
        self.award = award
        self.rules = rules
        self.questions = questions
        
    def show(self):
        '''Show game description'''
        return f'Nombre del juego: {self.name}'


    #TODO: DIFFERENT GAME METHODS (12/13)

    def play_sopa_letras(self,lives,clues,words,clue_list):
        '''Sopa de letras.'''

        #VARIABLES
        size = 15
        board = [['_' for i in range(size)] for i in range(size)]
        d = ['-','|','/','\\']
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        count = 0

        #PRINTS BOARD
        def show_board():
            for i in range(size):
                print('\t' + ' '.join(board[i]))

        #PLACING WORDS
        for word in words:

            #RANDOMLY CHOOSING TO FLIP THE WORD
            flip = random.randrange(2)
            if flip == 1:
                word = word[::-1]
            word = word.upper()

            fit = False
            while not fit:
                direction = random.choice(d)

                if direction == d[0]:
                    #HORIZONTAL
                    x = 1
                    y = 0

                elif direction == d[1]:
                    #VERTICAL
                    x = 0
                    y = 1

                elif direction == d[2]:
                    #DIAGONAL UP
                    x = 1
                    y = 1

                else:
                    #DIAGONAL DOWN
                    x = 1
                    y = -1

                #STARTING POINT
                start_x = random.randrange(size)
                start_y = random.randrange(size)

                #CHECKING IF IT FITS
                end_x = start_x + len(word)*x
                end_y = start_y + len(word)*y

                if end_x < 0 or end_x >= size:
                    continue
                if end_y < 0 or end_y >= size:
                    continue

                fail = False

                for i in range(len(word)):

                    next_x = start_x + i*x
                    next_y = start_y + i*y

                    new_char = board[next_x][next_y]
                    #CHECK IF A LETTER IS ALREADY ON THAT SPACE
                    if new_char != '_':
                        if new_char == word[i]:
                            continue
                        else:
                            fail = True
                            break

                if fail:
                    continue

                else:
                    for i in range(len(word)):
                        next_x = start_x + i*x
                        next_y = start_y + i*y
                        board[next_x][next_y] = word[i]

                    fit = True

        #FILLING THE REST OF THE BOARD
        for i in range(size):
            for j in range(size):
                if board[i][j] == '_':
                    board[i][j] = random.choice(alphabet).upper()

        while True:

            if len(words) == 0:
                break

            blank()
            show_board()
            blank()
            print('Ingrese las palabras aquí.')
            x = input('> ').lower()

            if x == 'clue':
                if count == len(clue_list):
                    no_more_clues()
                    blank()
                    continue
                use_clue(clues)
                blank()
                print(clue_list[count])
                count+=1
                continue

            found = False
            for i,word in enumerate(words):
                if x == word.lower():
                    blank()
                    correct()
                    found = True
                    print(f'La palabra era: {word}')
                    words.pop(i)
                    time.sleep(2)
                    wipe()
                    break

            if not found:
                blank()
                incorrect()
                lives = lose_lives(lives,0.5)
                time.sleep(2)

        blank()
        you_won(self.name)

        return self.award

    def play_preguntas_python(self,lives,clues,q,a,clue_list):
        '''Preguntas sobre Python.'''

        count = 0

        #DETECTING WHICH QUESTION WAS CHOSEN
        if a == 'Validar en python que de el siguiente resultado: 50.00 en formato entero':
            #QUESTION 1
            qa = 1
            frase  = 'tengo en mi cuenta 50,00 $'
            a = 50
            key = "int(float(frase.replace(',','.').split(' ')[4]))"
        else:
            #QUESTION 2
            qa = 2
            frase = 'oidutse ne al ortem aireinegni ed sametsis'
            a = 'estudio en la metro ingenieria de sistemas'
            key = "frase_v = ' '.join(w[::-1] for w in frase.split(' '))"

        while True:
            print(q)
            x = input('> ')

            #USER USES A CLUE
            if x.lower() == 'clue':
                if count == len(clue_list):
                    no_more_clues()
                    blank()
                    continue
                use_clue(clues)
                blank()
                print(clue_list[count])
                blank()
                count+=1
                continue

            if qa == 1:
                try:
                    if 'replace' in x and 'split' in x and 'int' in x and eval(x) == a:
                        #QUESTION 1 CORRECT
                        break
                except:
                    blank()
            
            elif qa == 2:
                try:
                    if 'split' in x and eval(x) == a:
                        #QUESTION 2 CORRECT
                        break
                except:
                    blank()

            incorrect()
            lives = lose_lives(lives,0.5)
        
        blank()
        correct()
        you_won(self.name)

        return self.award

    def play_adivinanzas(self,lives,clues,q,a,clue_list):
        '''Adivinanzas.'''

        count = 0

        while True:
            print(q)
            x = input('> ')
            #USER USES A CLUE
            if x.lower() == 'clue':
                if count == len(clue_list):
                    no_more_clues()
                    blank()
                    continue
                use_clue(clues)
                blank()
                print(clue_list[count])
                blank()
                count+=1
                continue
            #INCORRECT ANSWER
            if x not in a:
                incorrect()
                lives = lose_lives(lives,0.5)
                blank()
                continue
            #CORRECT ANSWER
            break

        blank()
        correct()
        you_won(self.name)
        
        return self.award

    def play_ahorcado(self,lives,clues,q,a,clue_list):
        '''El ahorcado.'''

        #VARIABLES

        letter_list = list(a.upper())
        blanks = ['_' for i in letter_list]
        start_hint = random.randrange(len(a))
        blanks[start_hint] = letter_list[start_hint]
        blanks
        used_letters = []
        wrong_letters = []
        fails = 0
        count = 0
        already_tried_hint = False

        b = [' ' for i in range(6)]
        f = ['😵', '👕', '/', '\\', '-', '-']

        while True:

            blank_word = ' '.join(blanks)

            print('''
            ______
            |   {}                   Letras incorrectas: {}
            |  {}{}{}
            |   {}{}
            /\\
            '''.format(b[0],wrong_letters,b[4],b[1],b[5],b[2],b[3]))
            print('\t' + blank_word)
            blank()

            if fails == 6:
                #ALREADY LOST
                print('Has ahorcado al muñeco. 😵')
                print(f'La palabra era {a}.')
                blank()
                break

            elif '_' not in blanks:
                #ALREADY WON
                correct()
                print(f'La palabra era {a}.')
                blank()
                break

            print(q)
            x = input('> ').upper()

            #USER USES A CLUE
            if x == 'CLUE':
                if count == len(clue_list):
                    no_more_clues()
                    blank()
                    continue
                use_clue(clues)
                blank()
                print(clue_list[count])
                count+=1
                continue

            #USER ENTERED THE LETTER HINT, WHICH ONLY APPEARS ONCE
            elif x == letter_list[start_hint] and letter_list.count(x) == 1 and not already_tried_hint:
                print('La letra dada al inicio no aparece más en la palabra.')
                used_letters.append(x)
                already_tried_hint = True

            #ALREADY USED LETTER
            elif x in used_letters:
                print('Ya usaste esta letra.')

            #CORRECT LETTER
            elif x in letter_list:
                used_letters.append(x)
                blank()
                correct()
                blank()
                for i in range(len(letter_list)):
                    if x == letter_list[i]:
                        blanks[i] = letter_list[i]
                
            #INCORRECT INPUT
            else:
                #INCORRECT LETTER
                if x.isalpha() and len(x) == 1:
                    used_letters.append(x)
                    wrong_letters.append(x)

                #MODIFYING DOLL
                b[fails] = f[fails]

                fails += 1
                blank()
                incorrect()
                lives = lose_lives(lives,0.25)
                blank()

        you_won(self.name)
        blank()

        return self.award

    def play_preguntas_math(self,lives,clues,q,clue_list): #TODO: INCOMPLETE
        '''Preguntas matemáticas.'''

        #VARIABLES
        a = 'a'
        eq = q.split('f(x)=')[1]
        evaluada = 'test'
        count = 0
        

        #CALCULATE DERIVATIVE RESULT
        x, y, z = symbols('x y z')
        init_printing(use_unicode=True)
        f, g = symbols('f g', cls=Function)
        a = Derivative(eq,x,evaluate=pi)
        a.subs(x,y)
        
        while True:
            print(q)
            x = input('> ')

            #USER USES A CLUE
            if x.lower() == 'clue':
                if count == len(clue_list):
                    no_more_clues()
                    blank()
                    continue
                blank()
                use_clue(clues)
                print(clue_list[count])
                blank()
                count+=1
                continue

            if x == a:
                break

            blank()
            incorrect()
            lives = lose_lives(lives,0.25)
            blank()

        blank()
        correct()
        you_won(self.name)

        return self.award

    def play_criptograma(self,lives,q):
        '''Criptograma.'''

        #VARIABLES
        d = q['desplazamiento']
        q = q['question'].replace('á','a')
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alphabet_d = []

        #CREATING CYPHERED ALPHABET
        for i,letter in enumerate(alphabet):
            if i >= d:
                alphabet_d.append(letter)
        for letter in alphabet:
            if letter in alphabet_d:
                break
            alphabet_d.append(letter)

        #CYPHERING MESSAGE
        q_d = ''
        for char in q:
            for i,letter in enumerate(alphabet):
                if char.lower() == letter:
                    q_d += alphabet_d[i]
                    break
            else:
                q_d += char

        while True:

            blank()
            print(str(alphabet).upper().replace("'","").replace(", ","-").replace("[","").replace("]",""))
            print(str(alphabet_d).upper().replace("'","").replace(", ","-").replace("[","").replace("]",""))
            blank()
            print('Descifra el siguiente mensaje:')
            print(q_d)
            blank()
            x = input('> ').lower()

            if x == 'clue':
                print('No hay pistas aquí.')
                continue

            if x == q_d:
                blank()
                correct()
                break

            blank()
            incorrect()
            lives = lose_lives(lives,1)

        blank()
        you_won(self.name)

        return self.award

    def play_encuentra_logica(self,lives,q):
        '''Lógica booleana.'''

        #VARIABLES
        emoji_list = []
        results_list = []
        operations_list = []

        #CREATING EMOJI-ONLY LIST
        for i in q:
            if not i.isascii() and i != '\n' and i not in emoji_list:
                emoji_list.append(i)

        #CREATING RESULT-ONLY LIST
        for i,n in enumerate(q):
            if n.isnumeric():

                if q[i-1].isnumeric():
                    continue

                result = n
                j = 1
                while q[i+j].isnumeric():
                    result += q[i+j]
                    j += 1
                results_list.append(int(result))

        #CREATING MATH OPERATIONS LIST
        for i in q.split(' \n '):
            operations_list.append(i)
            
        #ACABO DE LEER EL DOC Y VI QUE ESTAS PREGUNTAS NO SE MODIFICARAN 🤡
        #IGUAL DEJO LO ANTERIOR, ME FAJE MUCHO PARA BORRARLO 🥲

        if results_list[0] == 45:
            a = 67
        elif results_list[0] == 27:
            a = 41

        blank()
        while True:
            try:
                for i in operations_list:
                    print(i)
                blank()
                x = input('> ')
                if x.lower() == 'clue':
                    blank()
                    use_clue(-1)
                    blank()
                    continue
                if int(x) != a:
                    raise Exception
                break
            except:
                blank()
                incorrect()
                lives = lose_lives(lives,0.5)
                blank()
        
        blank()
        correct()
        you_won(self.name)
        
        return self.award

    def play_quizizz_unimet(self,lives,clues,db):
        '''Quizziz de cultura general UNIMET.'''

        #CORRECT ANSWERS COUNTER
        ca = 0
        tq = len(db)

        while True:

            #STOP CONDITION
            if not db:
                blank()
                print(f'Has respondido {ca}/{tq} preguntas correctamente.')
                break

            #CHOOSE RANDOM QUESTION
            n = random.randrange(len(db))

            #VARIABLES
            dbn = db[n]
            q = dbn['question']
            a = dbn['correct_answer']
            f = [dbn['answer_2'], dbn['answer_3'], dbn['answer_4']]
            fa = [a,f[0],f[1],f[2]]
            fa = random.sample(fa,k=len(fa))
            clue = dbn['clue_1']

            #REMOVE QUESTION FROM LIST
            db.pop(n)

            #ASK QUESTION
            blank()
            print(q)
            blank()
            for i,opt in enumerate(fa):
                print(f'{i+1}. {opt}')
                #INDEXING CORRECT ANSWER
                if opt == a:
                    index = str(i+1)
            blank()
            x = input('Ingrese el número de la respuesta correcta.\n> ')

            #CHECK IF USER WANTS A CLUE
            if x.lower() == 'clue':
                use_clue(clues)
                blank()
                print(clue)
                blank()
                x = input('> ')

            #CHECK IF INPUT IS CORRECT
            if x == index:
                correct()
                ca += 1

            #LOSE SCENARIO
            else:
                incorrect()
                lives = lose_lives(lives,0.5)

        
        you_won(self.name)
        blank()

        return self.award

        while True:
            pass

    def play_memoria(self,lives,q):
        '''Memoria.'''

        #TRANSFORM STRING INTO LIST
        q = eval(q)

        #BOARD FUNCTIONS
        def board(arr):
            b = f'''
            [{arr[0]}][{arr[1]}][{arr[2]}][{arr[3]}]
            [{arr[4]}][{arr[5]}][{arr[6]}][{arr[7]}]
            [{arr[8]}][{arr[9]}][{arr[10]}][{arr[11]}]
            [{arr[12]}][{arr[13]}][{arr[14]}][{arr[15]}]
            '''
            return b

        #VARIABLES
        guesses = ['3','4','5','6','E','R','T','Y','D','F','G','H','C','V','B','N']
        el = []
        for i in q:
            for j in i:
                el.append(j)
        kl = list(guesses)
        matches = 0

        while matches < 8:

            print(board(kl))
            x = input('Ingresa el número o letra de la primera carta:\n> ').upper()
            while x not in guesses:
                x = input('Intenta de nuevo.\n> ').upper()
            for i in range(len(kl)):
                if x == kl[i]:
                    #SHOW CARD
                    first = el[i]
                    first_index = i
                    kl[i] = el[i]
            
            print(board(kl))
            y = input('Ingresa el número o letra de la segunda carta:\n> ').upper()
            while y not in guesses or y == x:
                y = input('Intenta de nuevo.\n> ').upper()
            for i in range(len(kl)):
                if y == kl[i]:
                    #SHOW CARD
                    second = el[i]
                    second_index = i
                    kl[i] = el[i]

            print(board(kl))
            kl = list(guesses)

            if first == second:
                correct()
                matches += 1
                guesses[first_index] = first
                guesses[second_index] = second
                kl = list(guesses)
            
            else:
                incorrect()
                lives = lose_lives(lives, 0.25)

            time.sleep(2)
            first = 'a'
            second = 'b'
            wipe()

        blank()
        you_won(self.name)

        return self.award
        
    def play_logica_booleana(self,lives,q,a):
        '''lógica booleana.'''

        while True:
            x = input(q).capitalize()
            if x == 'Clue':
                use_clue(-1)
                blank()
                continue
            if x != a:
                incorrect()
                lives = lose_lives(lives,0.5)
                blank()
                continue
            break

        blank()
        correct()
        
        return self.award

    def play_palabra_mezclada(self,lives,q,c,a,f): #TODO: correct answer list bugs
        '''Descifrar varias palabras revueltas.'''

        #PRINT QUESTION
        print(q)
        blank()

        while True:

            #STOP CONDITION
            if not f:
                break

            #PRINTING LIST OF SCRAMBLED WORDS
            print(c)
            for i in range(len(f)):
                print('- ' + f[i])
            blank()
            x = input('> ').lower()

            #USER ATTEMPTS TO USE CLUE
            if x == 'clue':
                use_clue(-1)
                blank()
                continue

            #CHECKING IF INPUT IS IN LIST
            found = False
            for i in range(len(a)):
                if x == a[i]:
                    found = True
                    correct()
                    print(f'La palabra era {a[i]}.')
                    blank()
                    a.pop(i)
                    f.pop(i)
                    break
            
            #LOSE SCENARIO
            if not found:
                lives = lose_lives(lives,0.5)
                blank()

        you_won(self.name)
        blank()

        return self.award

    def play_escoge_numero_entre(self,lives,q,a):
        '''Escoger un número entre 1 y 15.'''

        att = 0
        while True:
            try:
                x = input(q)
                if int(x) != a:
                    raise Exception
                break
            except:
                blank()
                incorrect()
                att += 1
                if att != 0 and att % 3 == 0:
                    lives = lose_lives(lives,0.25)
                how_close_clue(x,a)

        blank()
        correct()
        you_won(self.name)

        return self.award

    def play_juego_libre(self):
        '''Aquí es cuando rompo la cuarta pared.'''

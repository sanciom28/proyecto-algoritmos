import time
import random
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


    #TODO: DIFFERENT GAME METHODS (7/13)

    def play_sopa_letras(self):
        pass

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

    def play_preguntas_math(self):
        pass

    def play_criptograma(self):
        pass

    def play_encuentra_logica(self):
        pass

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

    def play_memoria(self):
        pass

    def play_logica_booleana(self,lives,q,a):
        '''lógica booleana.'''

        while True:
            x = input(q).capitalize()
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
                x = int(input(q))
                if x != a:
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

        return self.award

    def play_juego_libre(self):
        pass


db_test = [
{
"question": "Me encuentro en la entrada de la Universidad",
"answer": "Metromix",
"clue_1": "sitio de comida",
"clue_2": "al lado de las copias",
"clue_3": "Comienza por Metro"
},
{
"question": "Me buscan y nunca me encuentran en la Universidad",
"answer": "Piscina",
"clue_1": "Es rectangular",
"clue_2": "Tiene agua",
"clue_3": "Se puede nadar"
},
{
"question": "Tienes que subir muchos pisos para llegar a mi",
"answer": "Rectorado",
"clue_1": "Esta en el Eugenio Mendoza",
"clue_2": "Ultimo piso del Eugenio",
"clue_3": "Oficina del Rector"
}
]

#RANDOM QUESTION INDEX
nn = random.randint(0,2)
#CLUE LIST
cl = [w for w in db_test[nn].values()]
cl.pop(0)
cl.pop(0)

game_test = Game(2,2,'Juego de prueba',2,2,2)

game_test.play_ahorcado(1,3,db_test[nn]['question'],db_test[nn]['answer'],cl)

from time import sleep
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

languages: tuple = ('english', 'spanish', 'italian', 'russian')
language: dict = {}
english: dict = {
    'selectedlanguage' : 'The selected language is English',
    'errortypetxt' : 'Invalid input',
    'errorvaltxt' : 'Invalid input',
    'asklifes' : 'Enter the number of lives(from 1 to 5), or Random: ',
    'askplayers' : 'Enter the number of players(from 1 to 4): ',
    'answerlifes' : 'Lifes per player',
    'askname' : 'Enter the name of',
    'isdead' : 'is dead!',
    'haswon' : 'has won!',
    'projregen' : 'Bullet Regeneration',
    'falseproj' : 'Empty Bullets',
    'trueproj' : 'Real Bullets',
    'totproj' : 'Total Projectiles',
    'recieved' : 'recieved',
    'cigarettes' : 'a pack of cigarettes',
    'handcuffs' : 'a pair of handcuffs',
    'beer' : 'a beer',
    'handsaw' : 'a handsaw',
    'glass' : "a magnifying glass",
    'inverter' : 'an inverter',
    'phone' : 'a phone',

}

spanish: dict = {
    'selectedlanguage' : "El idioma seleccionado es el Español",
}

italian: dict = {
    'selectedlanguage' : "La lingua selezionata è l'Italiano",
    'errortypetxt' : 'Input non valido',
    'errorvaltxt' : 'Input non valido',
    'asklifes' : 'Inserisci il numero di vite(da 1 a 5), oppure Random: ',
    'askplayers' : 'Inserisci Numero Giocatori(da 1 a 4): ',
    'answerlifes' : 'Numero vite per player',
    'askname' : 'Inserisci il nome di',
    'isdead' : 'è morto!',
    'haswon' : 'ha vinto!',
    'projregen' : 'Rigenerazione Proiettili',
    'falseproj' : 'Proiettili Pieni',
    'trueproj' : 'Proiettili Vuoti',
    'totproj' : 'Proiettili Totali',
    'recieved' : 'ha ricevuto',
    'cigarettes' : 'un pacchetto di sigarette',
    'handcuffs' : 'un paio di manette',
    'beer' : 'una birra',
    'handsaw' : 'un seghettino',
    'glass' : "una lente d'ingradimento",
    'inverter' : 'un invertitore',
    'phone' : 'un telefono',
}

russian: dict = {
    'selectedlanguage' : "Выбран Pусский язык",
}


def animation1(text, timer=0.5):  #-> None
    print(text, end='')
    sleep(timer)


def animation2(text, timer=0.5):  #-> None
    print(text)
    sleep(timer)

def asklanguage():
    global language
    animation2('Available Languages: ')
    for num, language in enumerate(languages):
        animation2(f'{num + 1}. {language.capitalize()}')
    while 1:
        animation1('Type here your selection: ')
        input0 = fixtext(input())
        try:
            if 1 <= int(input0) <= len(languages):
                input0 = languages[int(input0)-1]
        except ValueError: pass
        if input0 == languages[0]:
            language = english
        elif input0 == languages[1]:
            language = spanish
        elif input0 == languages[2]:
            language = italian
        elif input0 == languages[3]:
            language = russian
        if input0 in languages: break
        else: animation2('Invalid input')
    animation2('\n'+language['selectedlanguage'])
    sleep(1)
    cls()
    print('\n')
    return language

def inputint(text, min=0, max=100000000000, timer=0.5, errortypetxt=None,
            errorvaltxt=None):  #-> int
    if errortypetxt is None: errortypetxt = language['errortypetxt']
    if errorvaltxt is None: errorvaltxt = language['errorvaltxt']
    while True:
        while True:
            animation1(text, timer)
            try:
                Input = int(input())
                break
            except ValueError:
                animation2(errortypetxt, timer)
        if max >= Input >= min:
            sleep(0.5)
            return Input
        else:
            animation2(errorvaltxt, timer)


def fixtext(text):  #-> str
    return text.strip().lower()


def controllo(projectiles, iprojectile):
    breakval = 0
    try:
        projectiles[iprojectile[4]] = projectiles[iprojectile[4]]
    except IndexError:
        breakval = 1
    return breakval

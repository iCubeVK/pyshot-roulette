from time import sleep


def animation1(text, timer=0.5):  #-> None
    print(text, end='')
    sleep(timer)


def animation2(text, timer=0.5):  #-> None
    print(text)
    sleep(timer)


def inputint(text, min=0, max=100000000000, timer=0.5, errortypetxt='Input non valido', errorvaltxt='Input non valido'):  #-> int
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

def colori(colore):
    global colors
    colors = {
        'grassetto' : "\033[01m",
        'verde' : "\033[42m",
        'giallo' : "\033[43m",
        'rosso' : "\033[41m",
        'reset' : "\033[0m" }